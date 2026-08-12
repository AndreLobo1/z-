import json
import os
import shutil
import subprocess
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path


GITLAB_URL = "https://git.inteli.edu.br"
TZ_OFFSET = "-03:00"
REPO_PATH = Path("/tmp/sindusfarma-work")
SRC_DIR = Path(__file__).resolve().parent / "src"
PLAN_PATH = Path(__file__).resolve().parent / "sprint1_plan.json"
ENV_PATH = Path(__file__).resolve().parent / ".env"
WORKFLOW_LABELS = {
    "in_progress": [os.environ.get("BOARD_LABEL_DOING", "Doing")],
    "awaiting_review": [os.environ.get("BOARD_LABEL_WAITING_REVIEW", "Waiting Review")],
}
TRANSIENT_LABELS = {
    os.environ.get("BOARD_LABEL_BACKLOG", "Backlog"),
    os.environ.get("BOARD_LABEL_DOING", "Doing"),
    os.environ.get("BOARD_LABEL_WAITING_REVIEW", "Waiting Review"),
    os.environ.get("BOARD_LABEL_REVIEW", "Review"),
}


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#") or "=" not in raw:
            continue
        key, value = raw.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'").strip('"'))


load_dotenv(ENV_PATH)

PROJECT_PATH = os.environ["GITLAB_PROJECT_PATH"]
PROJECT_ID = os.environ.get("GITLAB_PROJECT_ID")
GITLAB_TOKEN = os.environ["GITLAB_TOKEN"]
SCHEDULE_START = os.environ.get("SCHEDULE_START", "2026-08-12T12:00:00-03:00")
GITLAB_REPO = os.environ.get(
    "GITLAB_REPO",
    f"https://oauth2:{GITLAB_TOKEN}@git.inteli.edu.br/{PROJECT_PATH}.git",
)


def now_local() -> datetime:
    return datetime.fromisoformat(datetime.now().astimezone().isoformat())


def parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value)


def ts() -> str:
    return now_local().strftime("%Y-%m-%d %H:%M:%S")


def api(path: str, method: str = "GET", data=None):
    project_ref = PROJECT_ID or urllib.parse.quote_plus(PROJECT_PATH)
    url = f"{GITLAB_URL}/api/v4/projects/{project_ref}/{path}"
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN, "Content-Type": "application/json"}
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode() if data is not None else None,
        headers=headers,
        method=method,
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def git(args, cwd=REPO_PATH):
    res = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {res.stderr.strip()}")
    return res.stdout.strip()


def reset_workspace() -> None:
    if REPO_PATH.exists():
        shutil.rmtree(REPO_PATH)
    subprocess.run(["git", "clone", GITLAB_REPO, str(REPO_PATH)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(REPO_PATH), "config", "user.name", os.environ.get("GIT_AUTHOR_NAME", "Andre Lobo")], check=True)
    subprocess.run(["git", "-C", str(REPO_PATH), "config", "user.email", os.environ.get("GIT_AUTHOR_EMAIL", "andre.paula@sou.inteli.edu.br")], check=True)


def keep_non_workflow_labels(labels):
    return [label for label in labels if label not in TRANSIENT_LABELS]


def set_workflow_labels(issue, state: str):
    labels = keep_non_workflow_labels(issue.get("labels", [])) + WORKFLOW_LABELS[state]
    api(f"issues/{issue['iid']}", "PUT", {"labels": ",".join(labels)})
    print(f"[{ts()}] Issue #{issue['iid']} -> {state}")


def find_note(notes, marker: str):
    for note in notes:
        if marker in note.get("body", ""):
            return note
    return None


def ensure_note(issue_iid: int, marker: str, body: str):
    notes = api(f"issues/{issue_iid}/notes")
    note = find_note(notes, marker)
    if note:
        return note
    return api(f"issues/{issue_iid}/notes", "POST", {"body": body})


def ensure_branch(branch: str):
    try:
        api(f"repository/branches/{urllib.parse.quote_plus(branch)}")
        return
    except Exception:
        git(["checkout", "develop"])
        git(["pull", "origin", "develop"])
        git(["checkout", "-b", branch])
        git(["push", "-u", "origin", branch])


def copy_paths(paths):
    for relative in paths:
        src = SRC_DIR / relative
        dst = REPO_PATH / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)


def ensure_commits(task):
    git(["checkout", task.branch])
    for commit in task.commits:
        copy_paths(commit["paths"])
        git(["add", *commit["paths"]])
        if git(["status", "--short"]):
            git(["commit", "-m", commit["message"]])
    git(["push", "-u", "origin", task.branch])


def ensure_merge_request(task):
    mrs = api(
        "merge_requests?state=opened&per_page=100"
        f"&source_branch={urllib.parse.quote_plus(task.branch)}"
    )
    if mrs:
        return mrs[0]
    return api(
        "merge_requests",
        "POST",
        {
            "source_branch": task.branch,
            "target_branch": "develop",
            "title": task.title,
            "description": task.mr_description,
            "remove_source_branch": False,
        },
    )


@dataclass
class Task:
    iid: int
    title: str
    branch: str
    offset_minutes: int
    duration_minutes: int
    depends_on: list
    commits: list
    mr_description: str

    @property
    def marker(self) -> str:
        return f"AUTOMATION:TASK:{self.iid}"

    def planned_start(self, anchor: datetime) -> datetime:
        return anchor + timedelta(minutes=self.offset_minutes)

    def planned_finish(self, anchor: datetime) -> datetime:
        return self.planned_start(anchor) + timedelta(minutes=self.duration_minutes)


def load_plan():
    raw = json.loads(PLAN_PATH.read_text())
    return [Task(**task) for task in raw["tasks"]]


def dependencies_ready(tasks_by_iid, anchor: datetime, task: Task):
    for dep_iid in task.depends_on:
        dep = tasks_by_iid[dep_iid]
        dep_issue = api(f"issues/{dep_iid}")
        if "aguardando-review" not in dep_issue.get("labels", []):
            return False
        if now_local() < dep.planned_finish(anchor):
            return False
    return True


def start_task(task: Task, anchor: datetime):
    issue = api(f"issues/{task.iid}")
    set_workflow_labels(issue, "in_progress")
    ensure_branch(task.branch)
    start_at = task.planned_start(anchor).isoformat()
    finish_at = task.planned_finish(anchor).isoformat()
    ensure_note(
        task.iid,
        task.marker,
        f"{task.marker}\nstarted_at={start_at}\nfinish_at={finish_at}\nbranch={task.branch}",
    )


def finish_task(task: Task):
    issue = api(f"issues/{task.iid}")
    ensure_commits(task)
    mr = ensure_merge_request(task)
    ensure_note(
        task.iid,
        f"{task.marker}:completed",
        f"{task.marker}:completed\nmr={mr['web_url']}\ncompleted_at={now_local().isoformat()}",
    )
    set_workflow_labels(issue, "awaiting_review")


def main():
    anchor = parse_dt(SCHEDULE_START)
    tasks = load_plan()
    tasks_by_iid = {task.iid: task for task in tasks}
    reset_workspace()
    now = now_local()
    print(f"[{ts()}] Scheduler tick started")
    for task in tasks:
        issue = api(f"issues/{task.iid}")
        labels = set(issue.get("labels", []))
        if "aguardando-review" in labels:
            continue
        if now < task.planned_start(anchor):
            continue
        if not dependencies_ready(tasks_by_iid, anchor, task):
            continue
        if "em-desenvolvimento" not in labels:
            start_task(task, anchor)
            continue
        if now >= task.planned_finish(anchor):
            finish_task(task)
    print(f"[{ts()}] Scheduler tick finished")


if __name__ == "__main__":
    main()
