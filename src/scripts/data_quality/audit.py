"""
Módulo de Auditoria de Qualidade de Dados (DAMA-DMBOK)
Implementa verificações de Completude, Unicidade, Integridade Referencial, Consistência e Variância.
"""

import pandas as pd
import numpy as np

def audit_dataset(df: pd.DataFrame, dataset_name: str) -> dict:
    """Executa auditoria de completude, unicidade e dimensões básicas de um DataFrame."""
    total_rows = len(df)
    total_cols = len(df.columns)
    
    completeness_pct = {}
    null_counts = {}
    
    for col in df.columns:
        null_count = int(df[col].isnull().sum())
        null_counts[col] = null_count
        comp = ((total_rows - null_count) / total_rows * 100.0) if total_rows > 0 else 100.0
        completeness_pct[col] = round(float(comp), 2)
        
    overall_completeness = round(float(np.mean(list(completeness_pct.values()))), 2) if completeness_pct else 100.0
    duplicate_rows = int(df.duplicated().sum())
    
    # Detecção de colunas com variância zero (constantes)
    constant_cols = [str(col) for col in df.columns if df[col].nunique(dropna=True) <= 1 and total_rows > 1]
    
    return {
        "dataset_name": dataset_name,
        "row_count": total_rows,
        "col_count": total_cols,
        "overall_completeness_pct": overall_completeness,
        "completeness_pct": completeness_pct,
        "null_counts": null_counts,
        "duplicate_rows": duplicate_rows,
        "constant_columns": constant_cols
    }

def audit_referential_integrity(df_parent: pd.DataFrame, df_child: pd.DataFrame, parent_pk: str, child_fk: str) -> dict:
    """Valida se todas as chaves estrangeiras na tabela filha possuem correspondente na tabela pai (FK orphans)."""
    if parent_pk not in df_parent.columns or child_fk not in df_child.columns:
        return {"parent_pk": parent_pk, "child_fk": child_fk, "orphan_count": 0, "orphan_keys": [], "error": "Chaves não encontradas"}
        
    parent_keys = set(df_parent[parent_pk].dropna().unique())
    child_keys = df_child[child_fk].dropna().unique()
    
    orphans = [int(key) if isinstance(key, (int, np.integer)) else float(key) if isinstance(key, (float, np.floating)) else str(key)
               for key in child_keys if key not in parent_keys]
    
    return {
        "parent_pk": parent_pk,
        "child_fk": child_fk,
        "orphan_count": len(orphans),
        "orphan_keys": orphans[:20]  # Limitar a 20 exemplos no JSON para concisão
    }
