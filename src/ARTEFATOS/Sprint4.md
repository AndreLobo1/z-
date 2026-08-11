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
Documentação Técnica – Conformidade com ISO/IEC 10746 e diagramas UML atualizados.

---

Este documento reúne os elementos necessários para a implementação final dos reports no Power BI, agora conectados diretamente aos cubos de dados derivados do repositório analítico estruturado pelo grupo. A construção visual da interface já foi definida com base no mockup anterior, e nesta etapa o foco está em detalhar como os gráficos, indicadores e painéis foram implementados com base nos cubos, assegurando integridade analítica e funcionalidade interativa.


O grupo deverá também realizar testes de usabilidade a partir de um plano de tarefas realistas e documentar os resultados, validando se a navegação, filtragem e exploração dos dados ocorrem corretamente.


Todo o conteúdo deverá ser registrado no arquivo solucao_dashboard.md, localizado na pasta docs/ do repositório do grupo.


1. Implementação de Reports com Base nos Cubos de Dados


O grupo deve especificar como os reports foram implementados a partir dos cubos de dados extraídos do repositório analítico alimentado pela ETL. Descreva:



Quais cubos foram utilizados (por tema, métrica ou área de negócio);

Quais medidas e dimensões foram aplicadas em cada visualização;

Como os relacionamentos entre fatos e dimensões foram manipulados;

Quais filtros, segmentações ou hierarquias foram construídos a partir desses cubos.


Explique também se houve a necessidade de criar medidas DAX personalizadas para compor os indicadores e como elas se conectam ao modelo multidimensional.


2. Plano de Tarefas para Testes de Usabilidade


Com base nos reports já construídos sobre os cubos de dados, o grupo deve elaborar um plano de tarefas simulando interações reais dos usuários com a interface analítica.


As tarefas devem explorar funcionalidades como:



Análise por filtros hierárquicos (ex: período, região, categoria);

Drill-down e drill-through com base em dimensões dos cubos;

Avaliação de métricas comparativas ao longo do tempo;

Segmentações simultâneas e cruzamentos entre painéis.


3. Execução e Validação das Tarefas


O grupo deve realizar todos os testes propostos, interagindo com os reports construídos sobre os cubos de dados e avaliando:



A precisão dos dados apresentados;

A resposta dos painéis aos filtros e segmentações;

A coerência dos indicadores ao navegar entre níveis de granularidade;
A ausência de erros, lentidão ou inconsistências técnicas.


Qualquer limitação identificada deve ser documentada com uma análise crítica e proposta de solução.


4. Avaliação da Qualidade Técnica e Funcional dos Reports


Os reports desenvolvidos com base nos cubos devem demonstrar:



Clareza e coerência visual;

Organização lógica das visualizações;

Consistência entre dados exibidos e métricas dos cubos;

Fluidez na navegação e na aplicação de filtros;

Aderência ao objetivo analítico da solução.


A qualidade técnica será avaliada com base no aproveitamento dos cubos, na construção das medidas e na integração correta das visualizações ao modelo de dados.


 
CRITÉRIOS DE AVALIAÇÃO



Implementação Técnica com Cubos de Dados: utilização consistente dos cubos, medidas e dimensões bem aplicadas, coerência com o modelo analítico e justificativas para adaptações;

Plano de Tarefas para Usabilidade: tarefas realistas, alinhadas ao uso prático da interface e representativas das necessidades dos usuários;

Validação Funcional dos Reports: execução bem-sucedida das tarefas, com fluidez e confiabilidade dos dados exibidos nos painéis;

Qualidade Visual e Interativa: clareza na apresentação dos dados, boa organização dos elementos e experiência intuitiva de uso;

Aderência à Arquitetura Analítica: os reports devem refletir adequadamente a estrutura dos cubos e a lógica do modelo analítico consolidado pelo grupo.

---

Este documento registra a evolução do projeto ao longo da sprint 4, com base em práticas ágeis, políticas de gestão de configuração e critérios definidos pelo Escritório de Projetos. Seu objetivo é garantir visibilidade, rastreabilidade e alinhamento contínuo entre escopo, progresso e entregas do grupo.


Estrutura Esperada do Documento


O conteúdo deverá ser escrito no arquivo Gestão-Evolutiva-do-Projeto-Sprint-4.md e armazenado na pasta docs do repositório do grupo.


1. Backlog Revisado


O grupo deve revisar e atualizar o backlog do projeto, contemplando:



Features (Épicos): lista completa e atualizada das funcionalidades de alto nível do sistema;

User Stories: histórias de usuário alinhadas às features, refinadas e priorizadas;

Tasks: tarefas técnicas e de negócio associadas a cada user story, detalhadas para execução.


Formato sugerido: utilize tabelas ou listas organizadas em subseções por feature, com status e responsáveis atribuídos.
 
2. Métricas da Sprint 4


Apresente as medições realizadas na sprint, considerando:



Throughput: número de user stories ou tasks concluídas durante a sprint;

Cycle Time: tempo médio entre o início e a conclusão de cada user story;

Burndown Chart: gráfico de evolução da sprint em termos de tarefas realizadas por dia.


Instruções:



Apresente gráficos ou tabelas com os dados coletados;

Interprete os resultados: quais fatores influenciaram os tempos? Alguma meta foi descumprida? Por quê?


3. Planejamento da Sprint 4


Atualize o planejamento da sprint 5, considerando aprendizados da sprint 4:



Objetivos da sprint 5;

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

Métricas da Sprint 4: O throughput e o cycle time são contabilizados corretamente; o burndown é calculado, mostrando a redução do trabalho restante ao longo da sprint 4, desde o início até a conclusão, oferecendo insights sobre o ritmo de entrega da equipe;

Planejamento da Sprint 5: A lista completa de tasks para a próxima sprint é apresentada, com descrições claras e detalhadas; as tasks são priorizadas e sequenciadas de forma lógica e estratégica, considerando a capacidade do time e os objetivos da Sprint;

Conformidade com os Critérios do Escritório de Projetos: aqueles possíveis para esta etapa do projeto;
Políticas de Gestão de Configuração: uso correto destas políticas.

