# Report 05 - Carga & Demanda por Área

- Título: `Carga & Demanda por Área`
- Objetivo de negócio: mostrar quem mais demanda e como isso pesa na equipe.
- Público: interno.
- Cards/KPIs:
  - volume da área líder
  - volume regulatórios
  - volume business support
  - complexidade comum
- Visuais:
  - barras de demanda por área
  - donut por complexidade
  - dispersão complexidade x prazo
- Dados necessários:
  - `pesquisas.area`
  - `pesquisas.complexidade`
  - `pesquisas.dias_uteis_para_entrega`
  - `pesquisas.data_solicitacao`
- Status de viabilidade com a base atual: `Parcial`
- Principais lacunas/riscos:
  - a carga por área é viável, mas os blocos de complexidade não são robustos por causa do preenchimento de 24,6%.
  - a relação entre complexidade e prazo fica enviesada porque só 65 registros têm os dois campos válidos.

