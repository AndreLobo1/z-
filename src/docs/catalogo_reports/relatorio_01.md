# Report 01 - Produção & Volume

- Título: `Produção & Volume`
- Objetivo de negócio: acompanhar quantas pesquisas a Central entregou no período e em que ritmo.
- Público: interno.
- Cards/KPIs:
  - pesquisas no ano
  - pesquisas em andamento
  - pesquisas finalizadas
  - variação vs. ano anterior
- Visuais:
  - barras de pesquisas por mês
  - donut por tipo
  - barras por área
- Dados necessários:
  - `pesquisas.status`
  - `pesquisas.data_solicitacao`
  - `pesquisas.data_divulgacao`
  - `pesquisas.tipo`
  - `pesquisas.area`
- Status de viabilidade com a base atual: `100% possível`
- Principais lacunas/riscos:
  - ausência de meta anual explícita na base; se houver meta no dashboard, ela terá de ser parametrizada fora dos CSVs.
  - diferença entre `data_solicitacao` e `data_divulgacao` precisa ser tratada com regra clara para definir “entregue no ano”.

