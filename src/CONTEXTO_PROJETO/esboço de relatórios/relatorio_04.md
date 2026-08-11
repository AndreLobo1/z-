# Report 04 - Qualidade & Governança

- Título: `Qualidade & Governança`
- Objetivo de negócio: monitorar a saúde do dado que sustenta os demais reports.
- Público: interno.
- Cards/KPIs:
  - percentual de campos completos
  - perguntas com confiança alta
  - percentual de registros inválidos
  - respostas descartadas
- Visuais:
  - completude por base
  - donut de confiança das perguntas
  - tabela de inconsistências abertas
- Dados necessários:
  - auditoria de completude por base
  - `questoes.confianca`
  - regras de integridade referencial
  - regras de descarte/quarentena
- Status de viabilidade com a base atual: `100% possível`
- Principais lacunas/riscos:
  - o conceito de “score de saúde do dado” precisa ser definido pelo grupo; não vem pronto da base.
  - “respostas descartadas” depende de política clara de limpeza/quarentena.

