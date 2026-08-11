"""
Gera 4 gráficos para o relatório modelagem_quantitativa_de_dados_do_parceiro.md
Output: docs/images/*.png
"""
import os
import sys
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMG_DIR  = os.path.join(BASE_DIR, "docs", "images")
CSV_DIR  = os.path.join(BASE_DIR, "DADOS")
JSON_DIR = os.path.join(BASE_DIR, "docs", "data")
os.makedirs(IMG_DIR, exist_ok=True)

STYLE = {"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False}
plt.rcParams.update(STYLE)
BLUE  = "#2563eb"
GREY  = "#94a3b8"
RED   = "#ef4444"
GREEN = "#16a34a"

def load_csv(name):
    p = os.path.join(CSV_DIR, name)
    return pd.read_csv(p, sep=";", encoding="utf-8", low_memory=False) if os.path.exists(p) else pd.DataFrame()

df_pesquisas  = load_csv("pesquisas.csv")
df_empresas   = load_csv("empresas.csv")
df_clientes   = load_csv("clientes.csv")

with open(os.path.join(JSON_DIR, "quality_report.json")) as f:
    quality = json.load(f)

# ─────────────────────────────────────────────────────────────────────────────
# GRÁFICO 1 — Frequência de variáveis categóricas-chave
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Distribuição das Variáveis Categóricas Prioritárias", fontsize=13, fontweight="bold", y=1.01)

# status (pesquisas)
if "status" in df_pesquisas.columns:
    vc = df_pesquisas["status"].value_counts()
    pct = (vc / vc.sum() * 100).round(1)
    bars = axes[0].barh(vc.index, vc.values, color=BLUE, alpha=0.85)
    for bar, p in zip(bars, pct.values):
        axes[0].text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                     f"{p}%", va="center", fontsize=9)
    axes[0].set_title("status (pesquisas.csv)", fontsize=10)
    axes[0].set_xlabel("Frequência absoluta")

# Associado (empresas)
if "Associado" in df_empresas.columns:
    vc2 = df_empresas["Associado"].value_counts()
    pct2 = (vc2 / vc2.sum() * 100).round(1)
    colors = [GREEN if x == "Sim" else GREY for x in vc2.index]
    bars2 = axes[1].bar(vc2.index.astype(str), vc2.values, color=colors, alpha=0.85)
    for bar, p in zip(bars2, pct2.values):
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                     f"{p}%", ha="center", fontsize=10)
    axes[1].set_title("Associado (empresas.csv)", fontsize=10)
    axes[1].set_ylabel("Frequência")

# departamento — top 8 (clientes)
if "departamento" in df_clientes.columns:
    vc3 = df_clientes["departamento"].value_counts().head(8)
    pct3 = (vc3 / df_clientes["departamento"].count() * 100).round(1)
    bars3 = axes[2].barh(vc3.index[::-1], vc3.values[::-1], color=BLUE, alpha=0.75)
    for bar, p in zip(bars3, pct3.values[::-1]):
        axes[2].text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
                     f"{p}%", va="center", fontsize=8)
    axes[2].set_title("Top 8 Departamentos (clientes.csv)", fontsize=10)
    axes[2].set_xlabel("Frequência absoluta")

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "categoricas_frequencia.png"), dpi=130, bbox_inches="tight")
plt.close()
print("✅ categoricas_frequencia.png")

# ─────────────────────────────────────────────────────────────────────────────
# GRÁFICO 2 — Boxplot triplo das 3 variáveis numéricas + limites IQR
# ─────────────────────────────────────────────────────────────────────────────
num_vars = {
    "participantes":           "Participantes\n(n=335)",
    "tempo_preenchimento":     "Tempo Preench.\n(min, n=231)",
    "dias_uteis_para_entrega": "Dias Úteis Entrega\n(n=331)",
}
datasets = {}
for col, label in num_vars.items():
    if col in df_pesquisas.columns:
        s = pd.to_numeric(df_pesquisas[col], errors="coerce").dropna()
        datasets[label] = s.values

fig, axes = plt.subplots(1, len(datasets), figsize=(13, 5))
fig.suptitle("Boxplot IQR — Variáveis Numéricas de Pesquisas", fontsize=13, fontweight="bold")

for ax, (label, vals) in zip(axes, datasets.items()):
    s = pd.Series(vals)
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    ls  = q3 + 1.5 * iqr
    li  = q1 - 1.5 * iqr
    outliers_s = s[s > ls]
    outliers_i = s[s < li]

    bp = ax.boxplot(vals, patch_artist=True,
                    boxprops=dict(facecolor="#dbeafe", color=BLUE),
                    medianprops=dict(color="#1d4ed8", linewidth=2),
                    whiskerprops=dict(color=BLUE, linewidth=1.2),
                    capprops=dict(color=BLUE, linewidth=1.5),
                    flierprops=dict(marker="o", color=RED, alpha=0.5, markersize=5))
    ax.axhline(ls, color=RED, linestyle="--", linewidth=1, label=f"LS={ls:.1f}")
    ax.axhline(li, color=GREY, linestyle=":", linewidth=1, label=f"LI={li:.1f}")
    ax.set_title(label, fontsize=9)
    ax.set_xticks([])
    ax.legend(fontsize=7)
    n_out = len(outliers_s) + len(outliers_i)
    ax.set_xlabel(f"{n_out} outlier(s) IQR", fontsize=8, color=RED)

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "boxplot_numericas.png"), dpi=130, bbox_inches="tight")
plt.close()
print("✅ boxplot_numericas.png")

# ─────────────────────────────────────────────────────────────────────────────
# GRÁFICO 3 — Série temporal: pesquisas por trimestre
# ─────────────────────────────────────────────────────────────────────────────
if "data_solicitacao" in df_pesquisas.columns:
    dates = pd.to_datetime(df_pesquisas["data_solicitacao"], errors="coerce").dropna()
    ts = dates.dt.to_period("Q").value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(13, 4))
    ax.bar(ts.index.astype(str), ts.values, color=BLUE, alpha=0.82, edgecolor="white")
    ax.set_title("Distribuição Temporal de Pesquisas por Trimestre (data_solicitacao)", fontsize=12, fontweight="bold")
    ax.set_xlabel("Trimestre")
    ax.set_ylabel("Nº de pesquisas solicitadas")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    for i, v in enumerate(ts.values):
        ax.text(i, v + 0.2, str(v), ha="center", fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "serie_temporal_pesquisas.png"), dpi=130, bbox_inches="tight")
    plt.close()
    print("✅ serie_temporal_pesquisas.png")

# ─────────────────────────────────────────────────────────────────────────────
# GRÁFICO 4 — Completude das variáveis críticas (barras horizontais)
# ─────────────────────────────────────────────────────────────────────────────
criticas = {
    "pesquisas / complexidade":       quality["datasets"]["pesquisas"]["completeness_pct"]["complexidade"],
    "pesquisas / tempo_preenchimento":quality["datasets"]["pesquisas"]["completeness_pct"]["tempo_preenchimento"],
    "pesquisas / data_aprov":         quality["datasets"]["pesquisas"]["completeness_pct"]["data_aprov"],
    "pesquisas / participantes":      quality["datasets"]["pesquisas"]["completeness_pct"]["participantes"],
    "questoes / linhas_matriz":       quality["datasets"]["questoes"]["completeness_pct"]["linhas_matriz"],
    "questoes / observacoes":         quality["datasets"]["questoes"]["completeness_pct"]["observacoes"],
    "respondentes / hora_inicio":     quality["datasets"]["respondentes"]["completeness_pct"]["hora_inicio"],
    "respostas / valor":              quality["datasets"]["respostas"]["completeness_pct"]["valor"],
    "respostas / alternativa":        quality["datasets"]["respostas"]["completeness_pct"]["alternativa"],
    "empresas / Nacionalidade":       quality["datasets"]["empresas"]["completeness_pct"]["Nacionalidade"],
}
labels_c = list(criticas.keys())
values_c = list(criticas.values())
colors_c = [GREEN if v >= 80 else (RED if v < 30 else "#f59e0b") for v in values_c]

fig, ax = plt.subplots(figsize=(11, 6))
bars = ax.barh(labels_c[::-1], values_c[::-1], color=colors_c[::-1], alpha=0.87, edgecolor="white")
ax.axvline(80, color=GREY, linestyle="--", linewidth=1, label="Limiar 80% (aceitável)")
for bar, v in zip(bars, values_c[::-1]):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f"{v:.1f}%", va="center", fontsize=9)
ax.set_xlim(0, 110)
ax.set_title("Completude das Variáveis Críticas para o Projeto", fontsize=12, fontweight="bold")
ax.set_xlabel("Completude (%)")
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "completude_variaveis_criticas.png"), dpi=130, bbox_inches="tight")
plt.close()
print("✅ completude_variaveis_criticas.png")

print("\nTodos os gráficos gerados em docs/images/")
