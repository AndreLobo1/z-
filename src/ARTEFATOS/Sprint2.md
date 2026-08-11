Este documento reúne os elementos de compreensão do contexto institucional e de governança do parceiro, os requisitos funcionais, não funcionais e critérios de aceitação necessários à condução do projeto.


Estrutura Esperada do Documento


O conteúdo deverá ser escrito no arquivo Contextualização-e-Especificação-de-Requisitos-do-Projeto.md na pasta docs do repositório do grupo.


1. Cenário Organizacional e de Governança


Esta seção tem como objetivo reunir informações fundamentais sobre o parceiro e o ambiente em que o projeto será conduzido. As informações aqui descritas devem permitir compreender o posicionamento do projeto dentro da organização, sua relevância para o negócio, e as condições institucionais que impactam diretamente sua execução, incluindo aspectos organizacionais, estratégicos e de governança de dados.


1.1. Visão Geral do Parceiro e do Projeto


Descreva o parceiro envolvido na iniciativa e o contexto em que o projeto está inserido. A apresentação deve permitir uma compreensão sobre o parceiro, qual o seu papel no mercado e qual problema ou oportunidade o projeto visa atender. Para isto:



Apresente o nome do parceiro, seu setor de atuação, localização geográfica e uma breve descrição institucional (histórico, porte, missão, produtos ou serviços);

Descreva o contexto do negócio e da indústria, incluindo tendências relevantes, concorrência, desafios setoriais e oportunidades que justifiquem o projeto;

Detalhe os objetivos do projeto com base nas demandas do parceiro; utilize verbos de ação claros (ex: reduzir tempo de resposta, melhorar a acurácia de previsões, automatizar etapas manuais etc.);

Delimite com precisão o escopo do projeto, informando o que será abordado e o que ficará de fora, justificando tecnicamente essas decisões.


1.2. Alinhamento Estratégico


Evidencie como o projeto está inserido na lógica organizacional do parceiro, demonstrando aderência ao seu fluxo de valor e ao seu direcionamento estratégico. É fundamental compreender como o projeto impacta a organização como um todo e quais são os atores envolvidos. Para isto:



Modele o fluxo de valor da organização, evidenciando onde o projeto se insere e quais entregas de valor ele pretende aprimorar ou viabilizar; utilize diagramas, se necessário;

Realize uma análise dos stakeholders, identificando os principais interessados no projeto, seus papéis, expectativas e possíveis resistências; recomenda-se o uso de uma matriz de poder/interesse;

Aponte os principais processos organizacionais impactados pelo projeto e os objetivos e metas estratégicas aos quais ele está alinhado (ex: aumento de produtividade, conformidade regulatória, inovação tecnológica etc.).


1.3. Governança de Dados do Parceiro


Descreva como o parceiro trata dados em seus processos internos, destacando aspectos técnicos, legais e organizacionais relacionados à governança. A análise deve indicar o nível de maturidade da organização quanto ao uso e gestão dos dados. Para isso:



Aponte a estrutura de governança de dados do parceiro, mencionando se há comitês, responsáveis formais, políticas ou ferramentas específicas adotadas;

Descreva como são tratados os acessos a dados, tanto internos quanto externos, incluindo níveis de permissão, auditoria e rastreabilidade;

Informe se o parceiro adota políticas de segurança da informação, incluindo práticas de controle de acesso, criptografia, backups e prevenção de vazamentos;

Especifique como é tratada a conformidade com a LGPD, incluindo coleta de consentimento, tratamento de dados sensíveis e direitos dos titulares;

Indique a existência de uma política de uso de dados, inclusive no contexto de uso para análise ou desenvolvimento de modelos;

Descreva quais são as métricas de qualidade dos dados utilizadas pela organização, como elas são definidas e medidas, e qual o processo de monitoramento e correção de inconsistências.


2. Requisitos Funcionais (RFs)


Cada RF deve ser descrito usando o formato de user story:


Como <persona>, eu quero <realizar uma ação> para <objetivo>.


Instruções:



Use personas reais do contexto do parceiro (ex: coordenador técnico, auditor, analista de dados);

Associe cada RF a pelo menos um teste de usuário;

Numere os requisitos como RF01, RF02, etc.


3. Requisitos Não Funcionais (RNFs)


Devem estar alinhados à norma ISO 25010, e também descritos como user stories.


Como <persona>, eu quero <ação relacionada à qualidade> para <benefício>.


Instruções:



Relacione cada RNF a atributos de qualidade (desempenho, segurança, usabilidade, confiabilidade, manutenibilidade etc.);

Use identificadores no formato RNF01, RNF02, etc.;

Associe os RNFs a testes de usuário.


4. Testes de Usuário e Critérios de Aceitação


Cada RF e RNF deve conter ao menos um teste de usuário vinculado.


Formato dos Testes:



Pré-condição: O estado inicial necessário;

Procedimento de teste: Ação executada para validar o requisito;

Resultado esperado: O que se espera ver após o teste;

Pós-condição: Estado final após a execução.


5. Tabela de Correlação RF ↔ RNF


Monte uma tabela cruzada mostrando quais RNFs estão diretamente relacionados a quais RFs.


Exemplo de estrutura:


   +-----------------------+--------------------------+------------------------+-----------------------+
    |  Requisito Funcional  |  RNF01 (Desempenho)  |  RNF02 (Usabilidade)  |  RNF03 (Segurança)  |
   +-----------------------+--------------------------+------------------------+-----------------------+
    |  RF01                         |                   X                   |                                    |                 X                |
    |  RF02                         |                                        |                 X                 |                                   |
   +-----------------------+--------------------------+------------------------+-----------------------+


CRITÉRIOS DE AVALIAÇÃO



Cenário Organizacional e de Governança - clareza na caracterização do parceiro, contextualização setorial, definição objetiva de objetivos e escopo, alinhamento estratégico bem estruturado e descrição adequada da governança de dados;

Requisitos Funcionais - requisitos completos, relevantes, bem redigidos em formato de user story, corretamente codificados e vinculados a testes de usuário;

Requisitos Não Funcionais - aderência à ISO 25010, clareza no formato de user story, codificação correta, associação a testes e coerência com os RFs;

Testes de Usuário e Critérios de Aceitação - estrutura completa, clareza e mensurabilidade, com foco na validação eficaz de RFs e RNFs;

Coerência RF ↔ RNF - tabela de correlação clara e lógica, com aderência aos objetivos do projeto e à arquitetura proposta.

---

Este documento complementa a especificação de requisitos do projeto, descrevendo a modelagem dimensional do Data Warehouse a ser desenvolvido. O objetivo é garantir que as análises, relatórios e dashboards apoiem as decisões estratégicas do parceiro, com dados organizados, limpos e historicamente consistentes.


Estrutura Esperada do Documento


O conteúdo deverá ser escrito no arquivo Modelagem-Dimensional-do-Data-Warehouse.md na pasta docs do repositório do grupo.


1. Tabelas de Fato


Nesta seção, devem ser listadas as principais tabelas de fato do DW, contendo os eventos ou transações que representam os processos de negócio medidos pelo projeto.


Instruções:



Para cada tabela, defina um nome claro e conciso (ex: Fato_Produção, Fato_Auditoria);

Especifique a granularidade da tabela (ex: por aplicação, por coleta, por visita técnica);

Liste as medidas que serão armazenadas na tabela (ex: produtividade colhida, tempo de aplicação, custo, volume, índice de falhas).


2. Tabelas de Dimensão


Apresente as dimensões que fornecerão o contexto descritivo para as análises.


Instruções:



Nomeie cada tabela de dimensão (ex: Dim_Produtor, Dim_Localidade, Dim_Safra, Dim_Auditor);

Liste os atributos relevantes (ex: nome do produtor, tipo de cultura, município, estado, cargo do auditor, grau de risco);

Identifique as hierarquias existentes (ex: Município → Estado; Safra → Ano; Cargo → Departamento).


3. Data Mapping


Documente o mapeamento entre os campos das bases de dados operacionais ou históricas e os atributos das dimensões e medidas das tabelas de fato.


Instruções:


Crie uma tabela ou descrição que indique:



Nome do campo na base de origem;

Nome do campo no DW;

Tabela destino (dimensão ou fato);

Tipo de transformação ou agregação, se aplicável.


Exemplo:


    +--------------------+--------------------+-----------------------+------------------+----------------------------------+
     |   Campo Fonte      |    Tabela Origem    |        Campo DW        |      Tabela DW     |           Transformação                 |
    +--------------------+--------------------+-----------------------+------------------+----------------------------------+
     |    colheita_kg        |  produção.csv        |  produtividade_kg     |  Fato_Produção   |  Nenhuma                                 |
     |   produtor_nome  |  cadastro.xlsx         |  nome_produtor        |  Dim_Produtor    |  Limpeza de espaços e casing  |
     | data_aplicacao     |  operacoes.db        |  data_aplicacao          |  Fato_Aplicacao  |  Conversão para datetime        |
    +--------------------+--------------------+-----------------------+------------------+----------------------------------+


4. Transformações ETL


Descreva as principais transformações a serem aplicadas no processo de ETL (Extract, Transform, Load).


Instruções:



Liste e explique as limpezas de dados (ex: remoção de registros nulos, tratamento de outliers, padronização de formatos de datas e unidades);

Descreva os joins necessários entre fontes distintas (ex: cruzamento entre arquivos CSV e banco relacional);

Indique processos de deduplicação de registros redundantes e as regras de chave natural/surrogate;

Liste padronizações de nomenclatura, unidades de medida ou codificações categóricas (ex: sim/não → booleano, kg/t → unidade padrão).
 


CRITÉRIOS DE AVALIAÇÃO



Tabelas de Fato: nome adequado, granularidade bem definida, medidas coerentes com os objetivos do projeto;

Tabelas de Dimensão: atributos relevantes, hierarquias representadas corretamente, nomes consistentes;

Data Mapping: clareza, precisão e rastreabilidade entre fontes e destino no DW;

Transformações ETL: abrangência e justificativa das operações propostas; alinhamento com as necessidades de qualidade dos dados para análise.

---

Este documento define as diretrizes que devem ser seguidas no desenvolvimento de dashboards interativos no Power BI.


Os dashboards devem:



Apoiar decisões estratégicas e técnicas do Parceiro;

Estar alinhados com os dados dos cubos dimensionais previamente modelados;

Atender às user stories e critérios de aceitação documentados no projeto;

Considerar privacidade e segurança conforme a LGPD;

Ser responsivos, navegáveis e segmentáveis por filtros relevantes. 


Entregáveis Esperados:



Um arquivo .pbix contendo os dashboards prontos;

Um documento Especificação-dos-Dashboards-em-Power BI.md na pasta docs contendo:Visão geral dos dashboards criados;

Justificativa para cada visual escolhido;

Tabela de rastreabilidade entre dashboards e requisitos funcionais (RFs);

Lista dos filtros utilizados em cada relatório;

Descrição de medidas DAX criadas e seus propósitos. 


Estrutura Esperada do Documento


1. Visão Geral


Breve descrição do propósito geral dos dashboards criados. Relacione-os a perguntas-chave como:



Quais práticas de manejo estão associadas às maiores produtividades?

Qual a variação da produtividade média por região ou consultor?

Como tem evoluído a adoção de determinadas tecnologias nas lavouras?


2. Descrição dos Dashboards Criados


Para cada dashboard, forneça:



Nome do dashboard;

Objetivo;

Medidas e filtros utilizados;

Visuais utilizados e justificativas (ex: gráfico de barras para comparação entre regiões);

Print da tela (ou link para o Power BI Service, se aplicável).


3. Tabela de Rastreabilidade RF ↔ Dashboards


Monte uma tabela indicando quais dashboards atendem a quais Requisitos Funcionais definidos no arquivo Contextualização-e-Especificação-de-Requisitos-do Projeto.md.


Exemplo:


    +-------+-----------------------------------------------+--------------------------------+------------------------------+
     |    RF    |                  Nome do Relatório                     |       Tipo Visual Principal         | Medidas Utilizadas              |
    +-------+-----------------------------------------------+--------------------------------+------------------------------+
     |  RF01  |  Inconsistência de Unidades de Medida      |  Tabela + Indicador                |  Qtd de registros com erro  |
    +-------+-----------------------------------------------+--------------------------------+------------------------------+
     | RF03   |  Ranking de Produtividade por Consultor   |  Gráfico de barras ordenado  |  Produtividade média por   |
     |            |                                                                      |                                                |  consultor                            |
    +-------+-----------------------------------------------+--------------------------------+------------------------------+


4. Medidas DAX Criadas


Liste todas as medidas criadas em DAX com:



Nome da Medida;

Fórmula em DAX;

Objetivo e uso no(s) dashboard(s).


Exemplo:



Produtividade Média por Região;

ProdMediaRegiao = AVERAGE(FatoProdutividade[Produtividade]);

Utilizada para comparar desempenho médio entre regiões.


5. Filtros e Segmentações


Descreva os principais filtros aplicados e os campos de segmentação disponíveis ao usuário. Por exemplo:



Ano da Safra;

Região;

Tipo de Solo;

Consultor Técnico;

Produto Aplicado.


Explique como esses filtros afetam as visualizações e auxiliam na exploração dos dados.


Considerações Técnicas



Os dashboards devem ser baseados exclusivamente nas tabelas de fato e dimensões projetadas;

Dados pessoais devem ser anonimizados ou omitidos (exigência da LGPD);

Medidas de performance como tempo de carregamento e responsividade serão avaliadas;

Visualizações redundantes ou pouco informativas devem ser evitadas.
 


CRITÉRIOS DE AVALIAÇÃO



Alinhamento com o modelo dimensional: uso correto dos dados do DW, sem consultas diretas à base bruta;

Clareza e utilidade dos relatórios: propósito claro, insights úteis e baseados em requisitos reais;

Qualidade técnica: desempenho, uso de DAX apropriado, filtros e segmentações eficazes;

Documentação dos relatórios: estruturação do Relatorios.md, clareza na descrição dos visuais e medidas;

Rastreabilidade e justificativa: tabela RF ↔ relatório bem elaborada, uso de prints e explicações.

---

Este documento define a abordagem de governança de dados adotada no contexto do projeto, com o objetivo de assegurar a qualidade, integridade, segurança, rastreabilidade e uso ético dos dados. A proposta visa alinhar-se às práticas reconhecidas de mercado e aos princípios apresentados em frameworks como, por exemplo, DAMA-DMBOK 2.0 e DCAM, promovendo uma gestão eficaz dos dados como ativos estratégicos.


Estrutura Esperada do Documento


O conteúdo deverá ser escrito no arquivo Governança-de Dados-do-Projeto.md na pasta docs do repositório do grupo.


1. Estrutura Organizacional da Governança de Dados


Nesta seção, o grupo deverá mapear e atribuir os papéis fundamentais no ciclo de governança de dados.


Instruções:



Defina os responsáveis pelas funções de:

Data Owner: responsável final pelo domínio dos dados (ex: área do negócio);

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

Este documento registra a evolução do projeto ao longo da sprint 2, com base em práticas ágeis, políticas de gestão de configuração e critérios definidos pelo Escritório de Projetos. Seu objetivo é garantir visibilidade, rastreabilidade e alinhamento contínuo entre escopo, progresso e entregas do grupo.


Estrutura Esperada do Documento


O conteúdo deverá ser escrito no arquivo Gestão-Evolutiva-do-Projeto-Sprint-2.md e armazenado na pasta docs do repositório do grupo.


1. Backlog Revisado


O grupo deve revisar e atualizar o backlog do projeto, contemplando:



Features (Épicos): lista completa e atualizada das funcionalidades de alto nível do sistema;

User Stories: histórias de usuário alinhadas às features, refinadas e priorizadas;

Tasks: tarefas técnicas e de negócio associadas a cada user story, detalhadas para execução.


Formato sugerido: utilize tabelas ou listas organizadas em subseções por feature, com status e responsáveis atribuídos.
 
2. Métricas da Sprint 2


Apresente as medições realizadas na sprint, considerando:



Throughput: número de user stories ou tasks concluídas durante a sprint;

Cycle Time: tempo médio entre o início e a conclusão de cada user story;

Burndown Chart: gráfico de evolução da sprint em termos de tarefas realizadas por dia.


Instruções:



Apresente gráficos ou tabelas com os dados coletados;

Interprete os resultados: quais fatores influenciaram os tempos? Alguma meta foi descumprida? Por quê?


3. Planejamento da Sprint 3


Atualize o planejamento da sprint 3, considerando aprendizados da sprint 2:



Objetivos da sprint 3;

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

Métricas da Sprint 2: O throughput e o cycle time são contabilizados corretamente; o burndown é calculado, mostrando a redução do trabalho restante ao longo da sprint 2, desde o início até a conclusão, oferecendo insights sobre o ritmo de entrega da equipe;

Planejamento da Sprint 3: A lista completa de tasks para a próxima sprint é apresentada, com descrições claras e detalhadas; as tasks são priorizadas e sequenciadas de forma lógica e estratégica, considerando a capacidade do time e os objetivos da Sprint;

Conformidade com os Critérios do Escritório de Projetos: aqueles possíveis para esta etapa do projeto;
Políticas de Gestão de Configuração: uso correto destas políticas.

