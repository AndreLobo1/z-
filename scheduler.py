import urllib.request
import json
import subprocess
import time
import os
from datetime import datetime

GITLAB_URL = "https://git.inteli.edu.br"
PROJECT_ID = "30889"
GITLAB_TOKEN = os.environ.get("GITLAB_TOKEN", "glpat-zXY7glaR8u54k4SptpLEa286MQp1OmZ3CA.01.0y01ggwi2")
REPO_PATH = "/tmp/sindusfarma-work"
GITLAB_REPO = f"https://oauth2:{GITLAB_TOKEN}@git.inteli.edu.br/graduacao/2026-2a/t13/2026-2a-t13-es11-g02/sindusfarma-g02.git"
SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")

def ts():
    return datetime.now().strftime('%H:%M:%S')

def api(path, method="GET", data=None):
    url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/{path}"
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN, "Content-Type": "application/json"}
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode() if data else None,
        headers=headers,
        method=method
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"[{ts()}] API error {e.code} for {path}: {e.read().decode()}")
        return None

def git(args, cwd=REPO_PATH):
    res = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0 and res.stderr:
        print(f"[{ts()}] git notice: {res.stderr.strip()}")
    return res.stdout.strip()

def set_label(iid, label):
    issue = api(f"issues/{iid}")
    if not issue:
        return
    keep = [l for l in issue.get("labels", []) if l not in ["em-desenvolvimento", "aguardando-review", "em-review"]]
    if label:
        keep.append(label)
    api(f"issues/{iid}", "PUT", {"labels": ",".join(keep)})
    print(f"[{ts()}] Issue #{iid} label updated → {label}")

def open_mr(branch, title, body):
    mr = api("merge_requests", "POST", {
        "source_branch": branch,
        "target_branch": "develop",
        "title": title,
        "description": body,
        "remove_source_branch": False
    })
    if mr:
        print(f"[{ts()}] MR #{mr['iid']} opened for {branch}")
        return mr["iid"]
    return None

def wait_until(hhmm):
    target = datetime.strptime(f"{datetime.now().strftime('%Y-%m-%d')} {hhmm}", "%Y-%m-%d %H:%M")
    now = datetime.now()
    secs = (target - now).total_seconds()
    if secs > 0:
        print(f"[{ts()}] Waiting {int(secs)}s until {hhmm}...")
        time.sleep(secs)
    else:
        print(f"[{ts()}] Target time {hhmm} already passed or reached.")

# --- Initialize repo ---
print(f"[{ts()}] Preparing workspace at {REPO_PATH}...")
subprocess.run(["rm", "-rf", REPO_PATH], capture_output=True)
subprocess.run(["git", "clone", GITLAB_REPO, REPO_PATH], capture_output=True)
subprocess.run(["git", "-C", REPO_PATH, "config", "user.name", "Andre Lobo"], capture_output=True)
subprocess.run(["git", "-C", REPO_PATH, "config", "user.email", "andre.paula@sou.inteli.edu.br"], capture_output=True)
print(f"[{ts()}] Workspace ready.")

# ============================================================
# TASK 2: docs(sdd): infraestrutura sdd e índice de tarefas
# Schedule: 12:00 -> 12:30
# ============================================================
wait_until("12:00")
set_label(2, "em-desenvolvimento")

git(["checkout", "develop"])
git(["pull", "origin", "develop"])
git(["checkout", "-b", "feature/2-sdd-tasks-index"])

subprocess.run(["mkdir", "-p", f"{REPO_PATH}/docs/specs"], capture_output=True)
subprocess.run(["cp", f"{SRC_DIR}/docs/tasks_andre.md", f"{REPO_PATH}/docs/tasks_andre.md"], capture_output=True)
subprocess.run(["cp", "-R", f"{SRC_DIR}/docs/specs/tasks", f"{REPO_PATH}/docs/specs/"], capture_output=True)

git(["add", "docs/tasks_andre.md"])
git(["commit", "-m", "docs(sdd): add tasks index and parallel matrix"])
git(["add", "docs/specs/tasks/"])
git(["commit", "-m", "docs(sdd): add task specification documents"])
git(["push", "-u", "origin", "feature/2-sdd-tasks-index"])

wait_until("12:30")
open_mr("feature/2-sdd-tasks-index",
        "docs(sdd): infraestrutura sdd e índice de tarefas da sprint 1",
        "Publicação do `docs/tasks_andre.md` e especificações formais de tarefas.\n\nCloses #2")
set_label(2, "aguardando-review")

# ============================================================
# TASK 3: chore(mkdocs): setup mkdocs
# Schedule: 12:35 -> 13:05
# ============================================================
wait_until("12:35")
set_label(3, "em-desenvolvimento")

git(["checkout", "develop"])
git(["pull", "origin", "develop"])
git(["checkout", "-b", "feature/3-mkdocs-setup"])

for f in ["mkdocs.yml", "requirements-docs.txt"]:
    subprocess.run(["cp", f"{SRC_DIR}/{f}", f"{REPO_PATH}/{f}"], capture_output=True)
subprocess.run(["cp", "-R", f"{SRC_DIR}/docs/javascripts", f"{REPO_PATH}/docs/"], capture_output=True)

git(["add", "mkdocs.yml", "requirements-docs.txt"])
git(["commit", "-m", "chore(mkdocs): add mkdocs configuration"])
git(["add", "docs/javascripts/"])
git(["commit", "-m", "docs(assets): add mathjax and mermaid init scripts"])
git(["push", "-u", "origin", "feature/3-mkdocs-setup"])

wait_until("13:05")
open_mr("feature/3-mkdocs-setup",
        "chore(mkdocs): setup de infraestrutura de documentação mkdocs",
        "Configuração do MkDocs com Material Theme, MathJax e Mermaid.\n\nCloses #3")
set_label(3, "aguardando-review")

# ============================================================
# TASK 4: docs(math): inventário analítico das bases
# Schedule: 13:10 -> 14:10
# ============================================================
wait_until("13:10")
set_label(4, "em-desenvolvimento")

git(["checkout", "develop"])
git(["pull", "origin", "develop"])
git(["checkout", "-b", "feature/4-inventario-bases"])

subprocess.run(["cp", f"{SRC_DIR}/docs/inventario_das_bases.md", f"{REPO_PATH}/docs/inventario_das_bases.md"], capture_output=True)

git(["add", "docs/inventario_das_bases.md"])
git(["commit", "-m", "docs(math): add data base inventory"])
git(["push", "-u", "origin", "feature/4-inventario-bases"])

wait_until("14:10")
open_mr("feature/4-inventario-bases",
        "docs(math): elaboração do inventário analítico das bases de dados",
        "Inventário analítico das 6 tabelas CSV do parceiro.\n\nCloses #4")
set_label(4, "aguardando-review")

# ============================================================
# TASK 5: docs(spec): especificação técnica e adr-001
# Schedule: 14:15 -> 14:45
# ============================================================
wait_until("14:15")
set_label(5, "em-desenvolvimento")

git(["checkout", "develop"])
git(["pull", "origin", "develop"])
git(["checkout", "-b", "feature/5-specs-adr"])

for f in ["spec-analise-quantitativa-dados.md", "adr-001-pipeline-analise-quantitativa.md"]:
    subprocess.run(["cp", f"{SRC_DIR}/docs/specs/{f}", f"{REPO_PATH}/docs/specs/{f}"], capture_output=True)

git(["add", "docs/specs/spec-analise-quantitativa-dados.md"])
git(["commit", "-m", "docs(spec): add quantitative analysis spec"])
git(["add", "docs/specs/adr-001-pipeline-analise-quantitativa.md"])
git(["commit", "-m", "docs(adr): add adr-001 pipeline architecture"])
git(["push", "-u", "origin", "feature/5-specs-adr"])

wait_until("14:45")
open_mr("feature/5-specs-adr",
        "docs(spec): especificação técnica e adr-001 da análise quantitativa",
        "Especificação formal do modelo e ADR-001.\n\nCloses #5")
set_label(5, "aguardando-review")

# ============================================================
# TASK 6: test(pipeline): testes automatizados (TDD)
# Schedule: 14:50 -> 15:20
# ============================================================
wait_until("14:50")
set_label(6, "em-desenvolvimento")

git(["checkout", "develop"])
git(["pull", "origin", "develop"])
git(["checkout", "-b", "feature/6-tdd-tests"])

subprocess.run(["mkdir", "-p", f"{REPO_PATH}/tests"], capture_output=True)
subprocess.run(["cp", f"{SRC_DIR}/tests/test_data_pipeline.py", f"{REPO_PATH}/tests/test_data_pipeline.py"], capture_output=True)

git(["add", "tests/test_data_pipeline.py"])
git(["commit", "-m", "test(pipeline): add data pipeline tests"])
git(["push", "-u", "origin", "feature/6-tdd-tests"])

wait_until("15:20")
open_mr("feature/6-tdd-tests",
        "test(pipeline): especificação e testes unitários do pipeline de dados",
        "Suíte de testes automatizados Pytest (TDD Red Phase).\n\nCloses #6")
set_label(6, "aguardando-review")

# ============================================================
# TASK 7: feat(scripts): scripts de métricas e gráficos
# Schedule: 15:25 -> 16:25
# ============================================================
wait_until("15:25")
set_label(7, "em-desenvolvimento")

git(["checkout", "develop"])
git(["pull", "origin", "develop"])
git(["checkout", "-b", "feature/7-scripts-pipeline"])

subprocess.run(["mkdir", "-p", f"{REPO_PATH}/scripts"], capture_output=True)
for f in ["gerar_graficos_relatorio.py", "gerar_graficos_categoricos.py", "convert_docs.py"]:
    subprocess.run(["cp", f"{SRC_DIR}/scripts/{f}", f"{REPO_PATH}/scripts/{f}"], capture_output=True)

git(["add", "scripts/gerar_graficos_relatorio.py"])
git(["commit", "-m", "feat(scripts): add plot generator script"])
git(["add", "scripts/gerar_graficos_categoricos.py"])
git(["commit", "-m", "feat(scripts): add categorical plot generator"])
git(["add", "scripts/convert_docs.py"])
git(["commit", "-m", "feat(scripts): add document converter helper"])
git(["push", "-u", "origin", "feature/7-scripts-pipeline"])

wait_until("16:25")
open_mr("feature/7-scripts-pipeline",
        "feat(scripts): implementação dos scripts de geração de gráficos e métricas",
        "Scripts Python de processamento e visualização (TDD Green Phase).\n\nCloses #7")
set_label(7, "aguardando-review")

# ============================================================
# TASK 8: docs(math): relatório de modelagem quantitativa
# Schedule: 16:30 -> 19:30
# ============================================================
wait_until("16:30")
set_label(8, "em-desenvolvimento")

git(["checkout", "develop"])
git(["pull", "origin", "develop"])
git(["checkout", "-b", "feature/8-relatorio-modelagem"])

for f in ["index.md", "modelagem_quantitativa_de_dados_do_parceiro.md"]:
    subprocess.run(["cp", f"{SRC_DIR}/docs/{f}", f"{REPO_PATH}/docs/{f}"], capture_output=True)

git(["add", "docs/index.md"])
git(["commit", "-m", "docs(math): add main index and context pages"])
git(["add", "docs/modelagem_quantitativa_de_dados_do_parceiro.md"])
git(["commit", "-m", "docs(math): add quantitative model report"])
git(["push", "-u", "origin", "feature/8-relatorio-modelagem"])

wait_until("19:30")
open_mr("feature/8-relatorio-modelagem",
        "docs(math): elaboração do relatório de modelagem quantitativa de dados",
        "Relatório analítico final do Artefato de Modelagem Quantitativa.\n\nCloses #8")
set_label(8, "aguardando-review")

print(f"[{ts()}] All Sprint 1 tasks executed up to Aguardando Review!")
