"""
Suíte de Testes Automatizados (TDD / BDD) - Pipeline de Análise Quantitativa
Derivado da especificação autoritária SPEC-001 (utilizando unittest standard library).
"""

import os
import sys
import unittest
import pandas as pd
import numpy as np

# Adicionar pasta raiz ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.data_quality.audit import audit_dataset, audit_referential_integrity
from scripts.metrics.descriptive import calculate_descriptive_stats, calculate_iqr_outliers
from scripts.metrics.kpi_calculator import calculate_kpis

class TestDataPipeline(unittest.TestCase):

    def setUp(self):
        """Fixture com dataset controlado para validação de fórmulas estatísticas."""
        self.sample_df = pd.DataFrame({
            "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "valor": [10.0, 12.0, 14.0, 15.0, 16.0, 18.0, 20.0, 22.0, 25.0, 100.0], # 100.0 é outlier
            "categoria": ["A", "A", "B", "B", "B", "C", "C", None, "A", "B"]
        })

    def test_audit_dataset_completeness(self):
        """Cenário 1 BDD: Valida se a completude por coluna e global são calculadas corretamente."""
        res = audit_dataset(self.sample_df, "sample")
        self.assertEqual(res["row_count"], 10)
        self.assertEqual(res["col_count"], 3)
        self.assertEqual(res["completeness_pct"]["valor"], 100.0)
        self.assertEqual(res["completeness_pct"]["categoria"], 90.0)
        self.assertEqual(res["duplicate_rows"], 0)

    def test_calculate_descriptive_stats(self):
        """Valida estatística descritiva: média, mediana, desvio padrão, CV."""
        stats = calculate_descriptive_stats(self.sample_df["valor"])
        self.assertEqual(stats["count"], 10)
        self.assertAlmostEqual(stats["mean"], 25.2, places=1)
        self.assertEqual(stats["median"], 17.0)
        self.assertEqual(stats["min"], 10.0)
        self.assertEqual(stats["max"], 100.0)
        self.assertGreater(stats["cv_pct"], 0)

    def test_calculate_iqr_outliers(self):
        """Cenário 3 BDD: Valida detecção de outliers via método IQR."""
        iqr_res = calculate_iqr_outliers(self.sample_df["valor"])
        self.assertEqual(iqr_res["q1"], 14.25)
        self.assertEqual(iqr_res["q3"], 21.5)
        self.assertEqual(iqr_res["iqr"], 7.25)
        self.assertAlmostEqual(iqr_res["lower_bound"], 3.375, places=3)
        self.assertAlmostEqual(iqr_res["upper_bound"], 32.375, places=3)
        # O valor 100.0 deve ser marcado como outlier superior
        self.assertEqual(len(iqr_res["outliers"]), 1)
        self.assertEqual(iqr_res["outliers"][0], 100.0)

    def test_audit_referential_integrity(self):
        """Cenário 2 BDD: Valida integridade referencial entre tabela pai e filha."""
        df_parent = pd.DataFrame({"id_pai": [101, 102, 103]})
        df_child = pd.DataFrame({"id_filho": [1, 2, 3], "id_pai": [101, 102, 999]}) # 999 é órfão

        orphans = audit_referential_integrity(df_parent, df_child, "id_pai", "id_pai")
        self.assertEqual(orphans["orphan_count"], 1)
        self.assertEqual(orphans["orphan_keys"], [999])

if __name__ == "__main__":
    unittest.main()
