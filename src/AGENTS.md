# Regras e Diretrizes do Projeto Sidusfarma para Agentes de IA

## Diretrizes Gerais
Bem-vindo ao repositório do projeto **Sidusfarma**. Todas as IAs e desenvolvedores atuando neste repositório devem seguir estritamente as regras de governança abaixo para garantir máxima eficiência de tokens, clareza e reprodutibilidade.

---

## 1. Processamento de Documentos e Economia de Tokens
- **Manipulação de Arquivos Brutos**: Todos os arquivos PDF, apresentações `.pptx`, documentos Word e planilhas devem ser convertidos em Markdown (`.md`) via **Microsoft MarkItDown** (motor principal) ou **IBM Docling** (fallback para PDFs complexos).
- **Regra Estrita de Leitura**: IAs devem trabalhar estritamente com os arquivos `.md`. A leitura de arquivos brutos/multimodais é estritamente proibida sem justificativa e **autorização humana prévia e explícita** no chat caso seja detectada perda de contexto.
- Detalhes completos da regra: [`raw_file_handling.md`](file:///Users/andrelobo/Downloads/Sidusfarma/.agents/rules/raw_file_handling.md).

---

## 2. Estrutura do Repositório
- `AULAS/`: Material didático em PDF e suas versões `.md`.
- `CONTEXTO_PROJETO/`: Apresentações e TAPI do projeto.
- `DADOS/`: Datasets em CSV para análise de dados e engenharia de software.
- `ARTEFATOS/`: Documentação e entregáveis das Sprints do projeto.
- `PONDERADAS/`: Avaliações ponderadas por Sprint.
- `scripts/`: Scripts utilitários de suporte (conversão de documentos, etc.).

