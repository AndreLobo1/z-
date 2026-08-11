# Report 02 - Prazos & SLA

- Título: `Prazos & SLA`
- Objetivo de negócio: mostrar onde o tempo escapa entre solicitação e divulgação.
- Público: interno.
- Cards/KPIs:
  - ciclo médio
  - dias de tabulação
  - percentual de pesquisas prorrogadas
  - dias úteis aberta
- Visuais:
  - linha do tempo de ciclo ao longo do tempo
  - barras de tempo por complexidade
  - tabela de pesquisas fora do prazo
- Dados necessários:
  - `pesquisas.data_solicitacao`
  - `pesquisas.data_divulgacao`
  - `pesquisas.dias entre a solicitação e a divulgação`
  - `pesquisas.dias para tabulação`
  - `pesquisas.prorrogada_ate`
  - `pesquisas.dias úteis aberta`
  - `pesquisas.complexidade`
- Status de viabilidade com a base atual: `Parcial`
- Principais lacunas/riscos:
  - `complexidade` tem só 24,6% de preenchimento; o bloco “tempo por complexidade” fica fraco.
  - `prorrogada_ate` informa até quando houve prorrogação, mas não documenta motivo nem um flag binário nativo.
  - a base permite medir tempos agregados, mas não registra todas as microetapas do processo para afirmar gargalo com total segurança.

