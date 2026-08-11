# Report 03 - Ciclo de Vida da Pesquisa

- Título: `Ciclo de Vida da Pesquisa`
- Objetivo de negócio: medir avanço e travas em cada etapa do funil da pesquisa.
- Público: interno.
- Cards/KPIs:
  - solicitações
  - aprovadas
  - divulgadas
  - taxa de conclusão
- Visuais:
  - funil de etapas do ciclo
  - barras de tempo por etapa
  - tabela de paradas em cada fase
- Dados necessários:
  - `pesquisas.data_solicitacao`
  - `pesquisas.data_aprov`
  - `pesquisas.data_divulgacao`
  - `pesquisas.status`
- Status de viabilidade com a base atual: `Parcial`
- Principais lacunas/riscos:
  - `data_aprov` tem só 5,5% de preenchimento; a etapa de aprovação não sustenta análise confiável.
  - não há campo explícito de cancelamento ou motivo de parada.
  - o funil completo fica comprometido porque nem toda etapa operacional é registrada de forma consistente.

