"""
Módulo de Estatística Descritiva e Análise de Outliers (IQR)
Implementa cálculos de tendência central, dispersão e limites estatísticos.
"""

import pandas as pd
import numpy as np

def calculate_descriptive_stats(series: pd.Series) -> dict:
    """Calcula média, mediana, moda, variância, desvio padrão, min, max, amplitude e CV%."""
    s_clean = series.dropna()
    if len(s_clean) == 0:
        return {}
        
    mean_val = float(s_clean.mean())
    std_val = float(s_clean.std()) if len(s_clean) > 1 else 0.0
    cv_pct = float((std_val / mean_val) * 100.0) if mean_val != 0 else 0.0
    mode_val = s_clean.mode().iloc[0] if not s_clean.mode().empty else None
    
    return {
        "count": len(s_clean),
        "mean": round(mean_val, 4),
        "median": round(float(s_clean.median()), 4),
        "mode": mode_val if not isinstance(mode_val, (np.integer, np.floating)) else round(float(mode_val), 4),
        "variance": round(float(s_clean.var()), 4) if len(s_clean) > 1 else 0.0,
        "std_dev": round(std_val, 4),
        "min": round(float(s_clean.min()), 4),
        "max": round(float(s_clean.max()), 4),
        "range": round(float(s_clean.max() - s_clean.min()), 4),
        "cv_pct": round(cv_pct, 2)
    }

def calculate_iqr_outliers(series: pd.Series) -> dict:
    """Calcula os quartis Q1, Q3, o IQR e os limites inferior (LI) e superior (LS) de outliers."""
    s_clean = series.dropna()
    if len(s_clean) == 0:
        return {}
        
    q1 = float(s_clean.quantile(0.25))
    q3 = float(s_clean.quantile(0.75))
    iqr = float(q3 - q1)
    
    lower_bound = float(q1 - 1.5 * iqr)
    upper_bound = float(q3 + 1.5 * iqr)
    
    outliers = s_clean[(s_clean < lower_bound) | (s_clean > upper_bound)].tolist()
    
    return {
        "q1": round(q1, 4),
        "q3": round(q3, 4),
        "iqr": round(iqr, 4),
        "lower_bound": round(lower_bound, 4),
        "upper_bound": round(upper_bound, 4),
        "outlier_count": len(outliers),
        "outliers": [round(float(x), 4) for x in outliers]
    }
