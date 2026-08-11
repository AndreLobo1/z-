"""
Gera gráficos complementares para o relatório:
- status_pesquisas.png     (barras horizontais)
- tipo_pesquisas.png       (barras horizontais)
- associado_empresas.png   (barras)
- departamentos_top8.png   (barras horizontais)
- tipo_questoes.png        (barras horizontais)
- outliers_combined.png    (strip plot + boxplot lado a lado)
"""
import os, sys
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMG_DIR  = os.path.join(BASE_DIR, "docs", "images")
CSV_DIR  = os.path.join(BASE_DIR, "DADOS")
os.makedirs(IMG_DIR, exist_ok=True)

BLUE   = "#2563eb"
LBLUE  = "#93c5fd"
GREEN  = "#16a34a"
RED    = "#ef4444"
GREY   = "#94a3b8"
AMBER  = "#f59e0b"

plt.rcParams.update({"font.family": "DejaVu Sans",
                     "axes.spines.top": False,
                     "axes.spines.right": False,
                     "figure.facecolor": "white"})

def load(name):
    return pd.read_csv(os.path.join(CSV_DIR, name), sep=";", encoding="utf-8", low_memory=False)

df_p = load("pesquisas.csv")
df_e = load("empresas.csv")
df_c = load("clientes.csv")
df_q = load("questoes.csv")

# ── helper ─────────────────────────────────────────────────────────────────
def horiz_bar(series, title, filename, color=BLUE, n=None):
    vc  = series.value_counts() if n is None else series.value_counts().head(n)
    pct = (vc / series.count() * 100).round(1)
    fig, ax = plt.subplots(figsize=(9, max(3, len(vc) * 0.55 + 0.8)))
    bars = ax.barh(vc.index[::-1], vc.values[::-1], color=color, alpha=0.85, edgecolor="white")
    for bar, p, v in zip(bars, pct.values[::-1], vc.values[::-1]):
        ax.text(bar.get_width() + vc.max() * 0.01,
                bar.get_y() + bar.get_height() / 2,
                f"{v:,}  ({p}%)", va="center", fontsize=9, color="#1e293b")
    ax.set_title(title, fontsize=11, fontweight="bold", pad=10)
    ax.set_xlabel("Frequência absoluta")
    ax.set_xlim(0, vc.max() * 1.22)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, filename), dpi=130, bbox_inches="tight")
    plt.close()
    print(f"✅ {filename}")

# ── Gráfico 1 — status ──────────────────────────────────────────────────────
horiz_bar(df_p["status"], "Status das Pesquisas (pesquisas.csv)", "status_pesquisas.png", BLUE)

# ── Gráfico 2 — tipo de pesquisa ────────────────────────────────────────────
horiz_bar(df_p["tipo"], "Tipo de Pesquisa (pesquisas.csv)", "tipo_pesquisas.png", LBLUE)

# ── Gráfico 3 — Associado ────────────────────────────────────────────────────
assoc = df_e["Associado"].map(lambda x: "Sim" if str(x).strip().lower() == "sim" else "Não")
vc = assoc.value_counts()
pct = (vc / vc.sum() * 100).round(1)
fig, ax = plt.subplots(figsize=(5, 3))
colors = [GREEN if k == "Sim" else GREY for k in vc.index]
bars = ax.bar(vc.index, vc.values, color=colors, alpha=0.87, edgecolor="white", width=0.5)
for bar, p, v in zip(bars, pct.values, vc.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 4,
            f"{v:,}\n({p}%)", ha="center", fontsize=10, color="#1e293b")
ax.set_title("Empresas Associadas (empresas.csv)", fontsize=11, fontweight="bold")
ax.set_ylabel("Frequência")
ax.set_ylim(0, vc.max() * 1.22)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "associado_empresas.png"), dpi=130, bbox_inches="tight")
plt.close()
print("✅ associado_empresas.png")

# ── Gráfico 4 — Departamentos top 8 ─────────────────────────────────────────
horiz_bar(df_c["departamento"], "Top 8 Departamentos dos Contatos (clientes.csv)",
          "departamentos_top8.png", BLUE, n=8)

# ── Gráfico 5 — tipo de questão ─────────────────────────────────────────────
horiz_bar(df_q["tipo"], "Tipo de Questão (questoes.csv)", "tipo_questoes.png", LBLUE)

# ── Gráfico 6 — Outliers: boxplot + strip chart por variável ────────────────
num_cols = {
    "participantes":           ("Participantes", 335),
    "tempo_preenchimento":     ("Tempo Preench. (min)", 231),
    "dias_uteis_para_entrega": ("Dias Úteis Entrega", 331),
}

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Distribuição e Outliers (IQR) — Variáveis Numéricas de Pesquisas",
             fontsize=12, fontweight="bold")

for ax, (col, (label, n)) in zip(axes, num_cols.items()):
    s = pd.to_numeric(df_p[col], errors="coerce").dropna()
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    ls  = q3 + 1.5 * iqr
    li  = max(0, q1 - 1.5 * iqr)
    inliers  = s[(s >= li) & (s <= ls)]
    out_high = s[s > ls]
    out_low  = s[s < li]

    # strip chart
    jitter = np.random.default_rng(42).uniform(-0.12, 0.12, len(s))
    ax.scatter(np.ones(len(inliers))  + jitter[:len(inliers)],  inliers,
               color=BLUE, alpha=0.35, s=14, zorder=2)
    ax.scatter(np.ones(len(out_high)) + jitter[len(inliers):len(inliers)+len(out_high)], out_high,
               color=RED, alpha=0.8, s=22, zorder=3, label=f"Outlier sup. (n={len(out_high)})")
    if len(out_low):
        ax.scatter(np.ones(len(out_low)) + jitter[-len(out_low):], out_low,
                   color=AMBER, alpha=0.8, s=22, zorder=3, label=f"Outlier inf. (n={len(out_low)})")

    # boxplot overlay
    bp = ax.boxplot(s, positions=[1], widths=0.35, patch_artist=True,
                    boxprops=dict(facecolor="#dbeafe", color=BLUE, alpha=0.5),
                    medianprops=dict(color="#1d4ed8", linewidth=2.5),
                    whiskerprops=dict(color=BLUE, linestyle="--"),
                    capprops=dict(color=BLUE),
                    flierprops=dict(marker="", color=RED))
    ax.axhline(ls, color=RED, linestyle=":", linewidth=1.2, alpha=0.7)
    ax.set_title(f"{label}\nN={n}  |  LS={ls:.1f}  |  Q1={q1}  Q3={q3}", fontsize=9)
    ax.set_xticks([])
    ax.set_ylabel(label, fontsize=8)
    if len(out_high) or len(out_low):
        ax.legend(fontsize=8, loc="upper right")

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "outliers_combined.png"), dpi=130, bbox_inches="tight")
plt.close()
print("✅ outliers_combined.png")

print("\nTodos os gráficos gerados.")
