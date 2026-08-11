# ADR-001: Arquitetura Desacoplada do Pipeline de Análise Quantitativa e Qualidade de Dados

* **Status:** Accepted
* **Data:** 2026-08-06
* **Autor:** Antigravity Data & Software Engineering Team

## Contexto

A solução analítica da Central de Pesquisas do Sidusfarma requer o processamento e auditoria de 6 datasets relacionais em CSV (`clientes`, `empresas`, `pesquisas`, `questoes`, `respondentes`, `respostas`). É necessário garantir que as regras de qualidade DAMA-DMBOK e os cálculos estatísticos sejam isolados, testáveis e reprodutíveis antes da carga no Data Warehouse.

## Decisão

Adotar uma arquitetura modular desacoplada em 3 camadas independentes:

1. **Camada 1 - Ingestão e Auditoria DAMA-DMBOK (`scripts/data_quality/`):** Validação de completude, unicidade, integridade referencial (PK/FK), consistência e variância.
2. **Camada 2 - Engine Estatística e Cálculo de KPIs (`scripts/metrics/`):** Apuração de medidas de tendência central, dispersão, limites de outliers ($IQR$) e fichas matemáticas de indicadores.
3. **Camada 3 - Orquestração e Exportação de Contratos (`scripts/runners/`):** Geração de artefatos estáticos (`quality_report.json`, `kpis_summary.json`, gráficos PNG em `docs/images/`) e publicação da documentação em Markdown/MkDocs.

## Justificativa

* **Modularidade e Testabilidade:** Permite testes unitários isolados para auditoria de dados e cálculo estatístico sem dependência de interfaces visuais.
* **Conformidade com SDD:** Os contratos JSON atuam como a interface autoritária entre o pipeline de processamento e a camada de documentação estática em Markdown/MkDocs.
* **Preparação para DW:** A separação em módulos facilita a futura migração das regras de qualidade e transformação para SQL/dbt nas sprints de Data Warehouse.

## Consequências

* **Positivas:** Reutilização total de código, execução via CLI/pytest e 0% de acoplamento entre regras de cálculo e renderização gráfica.
* **Trade-offs:** Necessidade de manutenção e versionamento dos contratos de schema JSON intermediários.
