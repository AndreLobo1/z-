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
REPO_PATH = Path("/tmp/sindusfarma-work")
SRC_DIR = Path(__file__).resolve().parent / "src"
PLAN_PATH = Path(__file__).resolve().parent / "sprint1_plan.json"
ENV_PATH = Path(__file__).resolve().parent / ".env"
WORKFLOW_LABELS = {
    "in_progress": os.environ.get("BOARD_LABEL_DOING", "Doing"),
    "awaiting_review": os.environ.get("BOARD_LABEL_WAITING_REVIEW", "Waiting Review"),
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
GITLAB_REPO = os.environ.get(
    "GITLAB_REPO",
    f"https://oauth2:{GITLAB_TOKEN}@git.inteli.edu.br/{PROJECT_PATH}.git",
)
TARGET_REPO_SOURCE = os.environ.get("TARGET_REPO_SOURCE")
JITTER_MINUTES = int(os.environ.get("JITTER_MINUTES", "5"))


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
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def git(args, cwd=REPO_PATH):
    res = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {res.stderr.strip()}")
    return res.stdout.strip()


def reset_workspace() -> None:
    if REPO_PATH.exists():
        shutil.rmtree(REPO_PATH)
    clone_source = TARGET_REPO_SOURCE or GITLAB_REPO
    subprocess.run(["git", "clone", clone_source, str(REPO_PATH)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(REPO_PATH), "remote", "set-url", "origin", GITLAB_REPO], check=True)
    subprocess.run(["git", "-C", str(REPO_PATH), "config", "user.name", os.environ.get("GIT_AUTHOR_NAME", "Andre Lobo")], check=True)
    subprocess.run(["git", "-C", str(REPO_PATH), "config", "user.email", os.environ.get("GIT_AUTHOR_EMAIL", "andre.paula@sou.inteli.edu.br")], check=True)


def keep_non_workflow_labels(labels):
    return [label for label in labels if label not in TRANSIENT_LABELS]


def set_workflow_labels(issue, state: str):
    labels = keep_non_workflow_labels(issue.get("labels", [])) + [WORKFLOW_LABELS[state]]
    api(f"issues/{issue['iid']}", "PUT", {"labels": ",".join(labels)})
    print(f"[{ts()}] Issue #{issue['iid']} -> {state}")


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
    duration_minutes: int
    depends_on: list
    commits: list
    mr_description: str


def load_plan():
    raw = json.loads(PLAN_PATH.read_text())
    return [Task(**task) for task in raw["tasks"]]


def deterministic_jitter(iid: int) -> int:
    span = (JITTER_MINUTES * 2) + 1
    return (iid % span) - JITTER_MINUTES


def due_at(started_at: datetime, duration_minutes: int, iid: int) -> datetime:
    duration = max(1, duration_minutes + deterministic_jitter(iid))
    return started_at + timedelta(minutes=duration)


def find_started_at(issue_iid: int) -> datetime | None:
    events = api(f"issues/{issue_iid}/resource_label_events")
    for event in reversed(events):
        label = event.get("label") or {}
        if event.get("action") == "add" and label.get("name") == WORKFLOW_LABELS["in_progress"]:
            return parse_dt(event["created_at"].replace("Z", "+00:00")).astimezone()
    return None


def dependencies_ready(task: Task):
    for dep_iid in task.depends_on:
        dep_issue = api(f"issues/{dep_iid}")
        labels = set(dep_issue.get("labels", []))
        if WORKFLOW_LABELS["awaiting_review"] not in labels:
            return False
    return True


def start_task(task: Task):
    issue = api(f"issues/{task.iid}")
    set_workflow_labels(issue, "in_progress")
    ensure_branch(task.branch)
    started_at = find_started_at(task.iid) or now_local()
    print(f"[{ts()}] Issue #{task.iid} started; due after {due_at(started_at, task.duration_minutes, task.iid).isoformat()}")


def finish_task(task: Task):
    issue = api(f"issues/{task.iid}")
    ensure_commits(task)
    mr = ensure_merge_request(task)
    set_workflow_labels(issue, "awaiting_review")
    print(f"[{ts()}] Issue #{task.iid} MR ready: {mr['web_url']}")


def main():
    tasks = load_plan()
    reset_workspace()
    now = now_local()
    print(f"[{ts()}] Scheduler tick started")

    # Finish due active tasks first.
    for task in tasks:
        issue = api(f"issues/{task.iid}")
        labels = set(issue.get("labels", []))
        if WORKFLOW_LABELS["in_progress"] not in labels:
            continue
        started_at = find_started_at(task.iid)
        if not started_at:
            print(f"[{ts()}] Issue #{task.iid} in progress but without start timestamp")
            continue
        due_time = due_at(started_at, task.duration_minutes, task.iid)
        print(f"[{ts()}] Issue #{task.iid} active since {started_at.isoformat()} due at {due_time.isoformat()}")
        if now >= due_time:
            finish_task(task)

    # Then start any ready tasks that have not started yet.
    for task in tasks:
        issue = api(f"issues/{task.iid}")
        labels = set(issue.get("labels", []))
        if WORKFLOW_LABELS["awaiting_review"] in labels or WORKFLOW_LABELS["in_progress"] in labels:
            continue
        if not dependencies_ready(task):
            continue
        start_task(task)

    print(f"[{ts()}] Scheduler tick finished")


if __name__ == "__main__":
    main()
