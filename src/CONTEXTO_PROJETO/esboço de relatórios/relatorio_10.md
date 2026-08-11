# Report 10 - Benchmark Setorial

- Título: `Benchmark Setorial`
- Objetivo de negócio: comparar uma empresa com a média ou distribuição do setor.
- Público: externo.
- Cards/KPIs:
  - posição da empresa vs. setor
  - quartil
  - diferença para a média
  - quantidade de indicadores comparados
- Visuais:
  - comparação empresa x média do setor
  - dispersão de posicionamento
  - tabela de pontos fortes e fracos
- Dados necessários:
  - `respostas.id_empresa`
  - `respostas.valor`
  - `questoes`
  - regras para transformar respostas em indicadores comparáveis
- Status de viabilidade com a base atual: `Parcial`
- Principais lacunas/riscos:
  - a base tem microdados por empresa, mas nem toda pergunta vira indicador benchmarkável.
  - a lógica de benchmark depende de padronização por tema/pergunta e de regras de negócio adicionais.
  - a pergunta do mockup “onde eu estou nesse gráfico?” exige destaque explícito da empresa-alvo.

