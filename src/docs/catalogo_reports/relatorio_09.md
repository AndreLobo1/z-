# Report 09 - Representatividade de Mercado

- Título: `Representatividade de Mercado`
- Objetivo de negócio: mostrar quanto do setor uma pesquisa realmente cobre.
- Público: externo.
- Cards/KPIs:
  - mercado coberto
  - variação vs. onda anterior
  - empresas top-share
  - confiabilidade
- Visuais:
  - linha de cobertura de mercado no tempo
  - barras de share dos participantes
  - donut coberto x não coberto
- Dados necessários:
  - `empresas.% de mercado`
  - `respondentes.id_empresa`
  - `pesquisas.data_solicitacao`
  - identificação da onda/período comparável
- Status de viabilidade com a base atual: `100% possível`
- Principais lacunas/riscos:
  - `% de mercado` está disponível para todas as empresas, mas muitos registros são `0,00%`; isso precisa de leitura cuidadosa.
  - “confiabilidade” não existe pronta; precisa ser definida como régua derivada pelo grupo.

