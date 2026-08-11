# Report 08 - Perfil dos Participantes

- Título: `Perfil dos Participantes`
- Objetivo de negócio: mostrar quem respondeu uma pesquisa específica.
- Público: externo.
- Cards/KPIs:
  - empresas participantes
  - percentual de nacionais
  - região líder
  - cargo comum
- Visuais:
  - donut de nacionalidade
  - barras por cargo/departamento
  - mapa de distribuição geográfica
- Dados necessários:
  - `respondentes.id_empresa`
  - `respondentes.id_cliente`
  - `empresas.Nacionalidade`
  - `empresas.Estado`
  - `clientes.cargo`
  - `clientes.departamento`
- Status de viabilidade com a base atual: `100% possível`
- Principais lacunas/riscos:
  - há pequenas ausências em `Nacionalidade`, `Estado` e dados de contato, mas sem inviabilizar o report.
  - o recorte por cargo/departamento depende do vínculo correto entre `respondentes` e `clientes`.

