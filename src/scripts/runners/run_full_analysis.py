"""
Runner de Orquestração do Pipeline de Análise Quantitativa e Qualidade de Dados
Executa a auditoria DAMA-DMBOK, a estatística descritiva, calcula os 10+ KPIs e exporta os artefatos JSON e gráficos.
"""

import os
import sys
import json
import pandas as pd
import numpy as np

# Configurar diretório gravável do Matplotlib
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"

# Garantir inclusão da raiz do projeto no PYTHONPATH
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import matplotlib
matplotlib.use("Agg") # Backend não interativo para geração headless de PNGs
import matplotlib.pyplot as plt
import seaborn as sns

from scripts.data_quality.audit import audit_dataset, audit_referential_integrity
from scripts.metrics.descriptive import calculate_descriptive_stats, calculate_iqr_outliers
from scripts.metrics.kpi_calculator import calculate_kpis

# Configuração de caminhos do projeto
DADOS_DIR = os.path.join(BASE_DIR, "DADOS")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
DATA_OUT_DIR = os.path.join(DOCS_DIR, "data")
IMAGES_OUT_DIR = os.path.join(DOCS_DIR, "images")

def setup_directories():
    """Garante que as pastas de destino existam."""
    os.makedirs(DATA_OUT_DIR, exist_ok=True)
    os.makedirs(IMAGES_OUT_DIR, exist_ok=True)

def load_all_datasets() -> dict:
    """Carrega os 6 arquivos CSV relacionais da pasta DADOS/ com o delimitador correto ';'."""
    files = {
        "clientes": "clientes.csv",
        "empresas": "empresas.csv",
        "pesquisas": "pesquisas.csv",
        "questoes": "questoes.csv",
        "respondentes": "respondentes.csv",
        "respostas": "respostas.csv"
    }
    
    datasets = {}
    for name, filename in files.items():
        filepath = os.path.join(DADOS_DIR, filename)
        if os.path.exists(filepath):
            datasets[name] = pd.read_csv(filepath, sep=";")
        else:
            print(f"AVISO: Arquivo não encontrado {filepath}")
            datasets[name] = pd.DataFrame()
            
    return datasets

def generate_charts(datasets: dict, quality_results: dict):
    """Gera visuais de alta resolução salvando em docs/images/."""
    sns.set_theme(style="darkgrid")
    
    # Gráfico 1: Completude de Dados por Dataset (%)
    names = [res["dataset_name"] for res in quality_results["datasets"].values()]
    comp_pcts = [res["overall_completeness_pct"] for res in quality_results["datasets"].values()]
    
    plt.figure(figsize=(9, 4.5))
    bars = plt.bar(names, comp_pcts, color="#2b5c8f", edgecolor="#173459")
    plt.title("Taxa de Completude Geral por Dataset (%) - DAMA-DMBOK", fontsize=12, fontweight="bold", pad=12)
    plt.ylabel("Completude (%)")
    plt.ylim(0, 105)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1, f"{height:.1f}%", ha="center", va="bottom", fontsize=9, fontweight="bold")
        
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_OUT_DIR, "dama_completeness_chart.png"), dpi=300)
    plt.close()
    
    # Gráfico 2: Distribution Boxplot de Tempo de Preenchimento (Outliers IQR)
    df_pesquisas = datasets.get("pesquisas", pd.DataFrame())
    if "tempo_preenchimento" in df_pesquisas.columns:
        s_tempo = pd.to_numeric(df_pesquisas["tempo_preenchimento"], errors="coerce").dropna()
        if len(s_tempo) > 0:
            plt.figure(figsize=(8, 4))
            sns.boxplot(x=s_tempo, color="#4caf50", flierprops=dict(markerfacecolor="r", marker="o", markersize=6))
            plt.title("Detecção de Outliers (IQR) - Tempo de Preenchimento (minutos)", fontsize=11, fontweight="bold")
            plt.xlabel("Tempo de Preenchimento (min)")
            plt.tight_layout()
            plt.savefig(os.path.join(IMAGES_OUT_DIR, "tempo_preenchimento_iqr_boxplot.png"), dpi=300)
            plt.close()

def main():
    print("Iniciando execução do pipeline de análise quantitativa...")
    setup_directories()
    
    datasets = load_all_datasets()
    
    # 1. Auditoria DAMA-DMBOK
    quality_summary = {
        "datasets": {},
        "referential_integrity": {}
    }
    
    total_completeness_list = []
    for name, df in datasets.items():
        res = audit_dataset(df, name)
        quality_summary["datasets"][name] = res
        total_completeness_list.append(res["overall_completeness_pct"])
        
    quality_summary["overall_completeness_pct"] = round(float(np.mean(total_completeness_list)), 2) if total_completeness_list else 100.0
    
    # Integridade Referencial entre tabelas
    ref_checks = [
        ("clientes", "empresas", "id_empresa", "ID"),
        ("respondentes", "pesquisas", "id_pesq", "id"),
        ("respondentes", "empresas", "id_empresa", "ID"),
        ("respondentes", "clientes", "id_cliente", "id_cliente"),
        ("respostas", "pesquisas", "pesquisa_id", "id"),
        ("respostas", "questoes", "id_pergunta", "id_pergunta")
    ]
    
    for child_name, parent_name, child_fk, parent_pk in ref_checks:
        df_child = datasets.get(child_name, pd.DataFrame())
        df_parent = datasets.get(parent_name, pd.DataFrame())
        
        check_name = f"{child_name}.{child_fk} -> {parent_name}.{parent_pk}"
        ref_res = audit_referential_integrity(df_parent, df_child, parent_pk, child_fk)
        quality_summary["referential_integrity"][check_name] = ref_res

    # Exportar JSON de Qualidade
    with open(os.path.join(DATA_OUT_DIR, "quality_report.json"), "w", encoding="utf-8") as f:
        json.dump(quality_summary, f, indent=2, ensure_ascii=False)
        
    print("Auditoria DAMA-DMBOK exportada em docs/data/quality_report.json")
    
    # 2. Estatística Descritiva e Outliers
    descriptive_summary = {}
    df_pesquisas = datasets.get("pesquisas", pd.DataFrame())
    
    numeric_cols = ["participantes", "tempo_preenchimento", "dias_uteis_para_entrega"]
    for col in numeric_cols:
        if col in df_pesquisas.columns:
            s_num = pd.to_numeric(df_pesquisas[col], errors="coerce")
            descriptive_summary[col] = {
                "stats": calculate_descriptive_stats(s_num),
                "iqr_outliers": calculate_iqr_outliers(s_num)
            }
            
    # 3. Cálculo de KPIs
    kpis = calculate_kpis(datasets)
    kpis_payload = {
        "kpi_count": len(kpis),
        "kpis": kpis,
        "descriptive_stats": descriptive_summary
    }
    
    with open(os.path.join(DATA_OUT_DIR, "kpis_summary.json"), "w", encoding="utf-8") as f:
        json.dump(kpis_payload, f, indent=2, ensure_ascii=False)
        
    print("Catálogo de KPIs exportado em docs/data/kpis_summary.json")
    
    # 4. Geração de Gráficos Visuais
    generate_charts(datasets, quality_summary)
    print("Gráficos de alta resolução exportados em docs/images/")
    
    print("Pipeline de Análise Quantitativa concluído com sucesso!")

if __name__ == "__main__":
    main()
