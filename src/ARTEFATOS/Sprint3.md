Documento de Especificação Técnica – Sistema ETL com Orquestração e Observabilidade


1. Objetivo


Este documento define a especificação técnica para o desenvolvimento do sistema de ETL (Extract, Transform, Load), responsável pela integração de dados entre múltiplas fontes e o Data Warehouse. O sistema será implementado em Python, orquestrado por um gerenciador de fluxos (DAG) e dotado de mecanismos de observabilidade para monitoramento de desempenho, disponibilidade e qualidade dos dados.


 O objetivo é entregar um pipeline confiável, modular, rastreável e alinhado às boas práticas de engenharia de software e operações modernas.


  
2. Escopo


O escopo do projeto inclui:


Desenvolvimento do módulo ETL em Python com arquitetura em camadas.
Instalação e configuração de um gerenciador de DAGs (ex: Apache Airflow, Prefect ou n8n).
Implementação de um pipeline de Integração Contínua (CI) para automação de testes e análise de código.
Implementação de observabilidade com coleta de métricas via Prometheus ou OpenTelemetry.
Documentação arquitetural com base nas visões da norma ISO/IEC 10746.
Modelagem UML dos principais componentes e fluxos.
Aplicação de boas práticas de codificação e manutenibilidade.
 
Observação: Este projeto contempla Integração Contínua (CI), mas não inclui Deploy Contínuo (CD). A liberação para ambientes superiores será manual após aprovação no CI.


  
3. Módulo de Processamento ETL


O módulo ETL será desenvolvido em Python e organizado em camadas:


Extração: Leitura de dados de APIs, bancos de dados e arquivos.
Transformação: Limpeza, validação, padronização e enriquecimento.
Carga: Ingestão dos dados processados no Data Warehouse.
 
A arquitetura em camadas garante modularidade, reutilização e facilidade de manutenção.


 
4. Gerenciador de DAGs (Orquestração)


Será instalado e configurado um gerenciador de fluxos de trabalho (DAG) para orquestrar a execução dos pipelines ETL. As opções consideradas são:


Apache Airflow
Prefect
n8n
 
O orquestrador será responsável por:


Definir e agendar DAGs (fluxos de tarefas).
Monitorar o status de execução de cada tarefa.
Registrar logs e permitir reinício de falhas.
Prover interface de visualização dos fluxos.
 
O ambiente será configurado com acesso controlado e documentação de instalação e operação.


 
5. Integração Contínua (CI)


Será implementado um pipeline de Integração Contínua (CI) acionado automaticamente a cada alteração no repositório (push ou pull request). O pipeline incluirá:


Checkout do código-fonte
Criação de ambiente isolado e instalação de dependências
Execução de testes automatizados (unitários e de integração)
Análise estática de código (linting com flake8 ou pylint)
Verificação de cobertura de testes
Geração de relatórios e feedback imediato
 
O CI será executado em plataforma como GitHub Actions ou GitLab CI, garantindo que apenas código válido e testado prossiga no ciclo de desenvolvimento.


 
6. Observabilidade


Para garantir rastreabilidade, diagnóstico e monitoramento contínuo, será implementado um sistema de observabilidade com coleta de métricas utilizando uma das seguintes soluções:


 Prometheus: Coleta ativa de métricas expostas pelo sistema.
OpenTelemetry: Instrumentação passiva para métricas, logs e traces.
 
Métricas a serem coletadas:
Tempo de execução de cada etapa (extração, transformação, carga).
Volume de dados processados (linhas, tamanho).
Status de execução (sucesso, falha, retry).
Disponibilidade do orquestrador e tarefas agendadas.
Latência em chamadas a APIs ou bancos de dados.
 
Essas métricas serão expostas pelo módulo ETL e/ou pelo orquestrador e poderão ser visualizadas em painéis (ex: Grafana) para acompanhamento operacional.


 
7. Testes Automatizados


Os testes serão automatizados com frameworks Python como pytest e unittest, com foco em:


Validação de funções individuais (testes unitários).
Integração entre módulos e com fontes externas (testes de integração).
Verificação da qualidade e consistência dos dados processados.
 
Os testes serão parte obrigatória do pipeline de CI, com cobertura mínima definida como critério de aprovação.


 
8. Entregáveis de Arquitetura e Modelagem


Serão entregues os seguintes artefatos técnicos:


8.1. Visões Arquiteturais (ISO/IEC 10746)


O sistema será descrito segundo as cinco visões da norma:


Visão de Negócio: Objetivos, stakeholders e escopo.
Visão de Informação: Estrutura, fluxo e regras de dados.
Visão Computacional: Componentes, interfaces e interações.
Visão de Engenharia: Infraestrutura, orquestração e execução.
Visão de Tecnologia: Stack tecnológica, protocolos e formatos.
 
8.2. Diagramas UML


Serão fornecidos:


Diagrama de Casos de Uso: Funcionalidades e interações com atores.
Diagrama de Componentes: Arquitetura modular e integração com o orquestrador.
Diagrama de Sequência: Fluxo de execução de um pipeline ETL desde o gatilho até o carregamento.
 
9. Boas Práticas de Código


O desenvolvimento seguirá boas práticas de engenharia de software, incluindo:


Código limpo, modular e bem documentado.
Tratamento de exceções e logs estruturados (ex: JSON).
Uso de ambientes virtuais e arquivo requirements.txt.
Versionamento com Git e processo de code review.
Padronização de nomenclatura e estrutura de projetos

CRITÉRIOS DE AVALIAÇÃO
Arquitetura e Modularidade – Separação clara de camadas, baixo acoplamento e reuso de componentes.
Qualidade do Pipeline – Validação, tratamento de falhas, consistência e retry automático.
Observabilidade – Métricas expostas (tempo, volume, status), integração com dashboards e alertas.
Orquestração – Clareza de DAGs, monitoramento, histórico e reinício de tarefas.
Integração Contínua – Automação de testes, linting, cobertura e bloqueio em falhas.
Testes Automatizados – Cobertura mínima, mocks adequados e cenários de borda.
Documentação Técnica – Conformidade com ISO/IEC 10746 e diagramas UML atualizados

---

Este documento define a abordagem de governança de dados adotada no contexto do projeto, com o objetivo de assegurar a qualidade, integridade, segurança, rastreabilidade e uso ético dos dados. A proposta visa alinhar-se às práticas reconhecidas de mercado e aos princípios apresentados em frameworks como, por exemplo, DAMA-DMBOK 2.0 e DCAM, promovendo uma gestão eficaz dos dados como ativos estratégicos.


Estrutura Esperada do Documento


O conteúdo deverá ser escrito no arquivo Governança-de Dados-do-Projeto.md na pasta docs do repositório do grupo.


1. Estrutura Organizacional da Governança de Dados


Nesta seção, o grupo deverá mapear e atribuir os papéis fundamentais no ciclo de governança de dados.


Instruções:



Defina os responsáveis pelas funções de:Data Owner: responsável final pelo domínio dos dados (ex: área do negócio);

Data Steward: responsável por garantir a qualidade e documentação dos dados;

Data Custodian: responsável técnico pela infraestrutura e segurança dos dados;

Identifique os responsáveis por metadados, catálogo, qualidade, segurança e compliance;

Inclua um organograma (se possível) com as responsabilidades.


 2. Política de Qualidade de Dados


Descreva os atributos de qualidade de dados que serão monitorados e as metas mínimas de aceitabilidade.


Instruções:



Liste os atributos adotados (ex: acurácia, completude, atualidade, consistência, unicidade);

Descreva como cada atributo será mensurado e reportado;

Identifique KPIs de qualidade de dados relevantes ao projeto;

Proponha ações corretivas a serem tomadas em caso de desvios.


3. Gestão de Metadados e Catálogo de Dados


Esta seção descreve como os dados e suas descrições serão organizados para promover reutilização, rastreabilidade e descoberta.


Instruções:



Descreva a ferramenta ou estratégia para catalogação dos dados;

Indique os metadados obrigatórios para tabelas de fato, dimensões e medidas (ex: nome, definição, fonte, periodicidade, sensibilidade);

Especifique os procedimentos para atualização e versionamento dos metadados;

Inclua uma tabela de exemplo com metadados de uma tabela do DW.


4. Classificação de Dados e Proteção


Apresente o plano de classificação e tratamento de dados sensíveis conforme boas práticas e normas (ex: LGPD).


Instruções:



Defina as categorias de dados (ex: público, interno, confidencial, sensível);

Indique critérios para classificação e exemplos por categoria;

Descreva os controles técnicos e organizacionais para dados classificados;

Explique como será feito o registro de consentimento e a rastreabilidade.


5. Segurança e Acesso aos Dados


Defina as políticas de acesso, autenticação e proteção da informação.


Instruções:



Especifique os perfis de acesso (ex: leitura, gravação, administração);

Indique se haverá segregação por camadas (ex: staging, trusted, analytics);

Liste as práticas de segurança aplicadas (ex: criptografia, auditoria, backups);

Apresente mecanismos de autenticação e controle de sessões.


6. Ciclo de Vida dos Dados


Descreva o ciclo completo dos dados no projeto, desde a ingestão até o descarte.


Instruções:



Modele (em texto ou diagrama) o ciclo de vida dos dados;

Indique prazos de retenção e descarte para cada tipo de dado;

Descreva como é feita a auditoria, versionamento e arquivamento;

Especifique regras de reuso e rastreabilidade entre as fontes e o DW.


7. Avaliação de Maturidade em Governança


Avalie o nível atual de maturidade da governança de dados no parceiro e proponha planos de melhoria.


Instruções:



Escolha um modelo de referência (ex: DAMA-DMBOK, DCAM, CMMI-DM);

Faça um diagnóstico baseado em critérios técnicos, organizacionais e culturais;

Aponte lacunas, riscos e oportunidades;

Elabore um plano de ação para evoluir a maturidade da governança.
 


CRITÉRIOS DE AVALIAÇÃO



Estrutura organizacional - Clareza na atribuição de papéis e responsabilidades;

Qualidade de dados - Definição de atributos, metas, indicadores e ações corretivas;

Metadados e catálogo - Organização, rastreabilidade e documentação adequada dos dados;

Classificação e privacidade - Aderência à LGPD e definição clara de categorias e controles;

Segurança e acesso - Definição de perfis, mecanismos técnicos e políticas de controle;

Ciclo de vida - Modelagem e documentação do ciclo de vida completo dos dados;

Avaliação de maturidade - Aplicação de framework, diagnóstico coerente e plano de evolução proposto.

---

Este documento registra a evolução do projeto ao longo da sprint 3, com base em práticas ágeis, políticas de gestão de configuração e critérios definidos pelo Escritório de Projetos. Seu objetivo é garantir visibilidade, rastreabilidade e alinhamento contínuo entre escopo, progresso e entregas do grupo.


Estrutura Esperada do Documento


O conteúdo deverá ser escrito no arquivo Gestão-Evolutiva-do-Projeto-Sprint-3.md e armazenado na pasta docs do repositório do grupo.


1. Backlog Revisado


O grupo deve revisar e atualizar o backlog do projeto, contemplando:



Features (Épicos): lista completa e atualizada das funcionalidades de alto nível do sistema;

User Stories: histórias de usuário alinhadas às features, refinadas e priorizadas;

Tasks: tarefas técnicas e de negócio associadas a cada user story, detalhadas para execução.


Formato sugerido: utilize tabelas ou listas organizadas em subseções por feature, com status e responsáveis atribuídos.
 
2. Métricas da Sprint 3


Apresente as medições realizadas na sprint, considerando:



Throughput: número de user stories ou tasks concluídas durante a sprint;

Cycle Time: tempo médio entre o início e a conclusão de cada user story;

Burndown Chart: gráfico de evolução da sprint em termos de tarefas realizadas por dia.


Instruções:



Apresente gráficos ou tabelas com os dados coletados;

Interprete os resultados: quais fatores influenciaram os tempos? Alguma meta foi descumprida? Por quê?


3. Planejamento da Sprint 4


Atualize o planejamento da sprint 4, considerando aprendizados da sprint 3:



Objetivos da sprint 4;

User stories selecionadas;

Tasks planejadas por story;

Critérios de pronto (Definition of Done);

Distribuição da carga de trabalho entre os membros.


Inclua: quadro Kanban ou link para ferramenta de gestão usada (ex: Jira, Trello, GitHub Projects).
 
4. Conformidade com os Critérios do Escritório de Projetos


Descreva como o grupo está atendendo aos critérios definidos pelo Escritório de Projetos.


Formato sugerido: checklist ou breve narrativa explicando a aderência aos critérios e planos de correção, se necessário.
 
5. Políticas de Gestão de Configuração


Liste e comprove a aplicação das políticas mínimas de gestão de configuração definidas para o módulo:



Controle de versões dos documentos (ex: uso de Git, pull requests revisadas);

Registro de mudanças com histórico e justificativa;

Padronização de nomenclaturas, pastas e convenções do repositório;

Uso de tags ou releases para marcos importantes.


Inclua: evidências como links para commits, tags, pull requests ou print de histórico no repositório.


 


CRITÉRIOS DE AVALIAÇÃO



Backlog Revisado: o backlog está atualizado com todas as features relevantes, refletindo as mudanças e adaptações necessárias; as user stories estão claramente definidas e atualizadas, alinhadas com as metas do projeto e o feedback da sprint anterior; as features e user stories estão organizadas e priorizadas de acordo com o planejamento estratégico do projeto;

Métricas da Sprint 3: O throughput e o cycle time são contabilizados corretamente; o burndown é calculado, mostrando a redução do trabalho restante ao longo da sprint 3, desde o início até a conclusão, oferecendo insights sobre o ritmo de entrega da equipe;

Planejamento da Sprint 4: A lista completa de tasks para a próxima sprint é apresentada, com descrições claras e detalhadas; as tasks são priorizadas e sequenciadas de forma lógica e estratégica, considerando a capacidade do time e os objetivos da Sprint;

Conformidade com os Critérios do Escritório de Projetos: aqueles possíveis para esta etapa do projeto;
Políticas de Gestão de Configuração: uso correto destas políticas.

