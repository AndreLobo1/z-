# Documentação Sidusfarma

Esta documentação passa a ser a superfície principal do projeto para leitura do relatório quantitativo, catálogo textual de reports, especificações e decisões arquiteturais.

## Estrutura

- [Relatório quantitativo principal](modelagem_quantitativa_de_dados_do_parceiro.md)
- [Catálogo textual dos reports](catalogo_reports/README.md)
- [Especificação da análise quantitativa](specs/spec-analise-quantitativa-dados.md)
- [ADR-001 do pipeline](specs/adr-001-pipeline-analise-quantitativa.md)

## Convenção adotada

O repositório passa a usar Markdown como fonte única de documentação, com renderização estática via MkDocs. A antiga visualização em Streamlit foi isolada em `legacy/streamlit/` e deixa de ser a interface principal do projeto.
