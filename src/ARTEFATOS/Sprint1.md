O conteúdo deverá ser produzido no arquivo contexto_organizacional_+_requisitos_da_solução_analítica.md, na pasta docs do repositório.


1. Cenário Organizacional e Contexto do Projeto

1.1 Visão Geral do Parceiro


Inclua:



nome da organização;

setor de atuação;

localização geográfica;

porte da empresa;

principais produtos ou serviços;

breve histórico;

missão ou propósito institucional.


1.2 Contexto do Negócio


Inclua:



características da indústria ou setor;

desafios enfrentados pela organização;

oportunidades identificadas;

tendências relevantes;

fatores que justificam a realização do projeto.


1.3 Objetivos do Projeto


Apresente os objetivos do projeto utilizando verbos de ação claros e mensuráveis.


Explique como cada objetivo gera valor para o parceiro.


1.4 Escopo do Projeto


Delimite o que será realizado e o que ficará fora do projeto.


Escopo Incluído



funcionalidades previstas;

análises que serão desenvolvidas;

dashboards que serão produzidos;

processos organizacionais contemplados.


Escopo Não Incluído


Explicite o que não será desenvolvido. Justifique as exclusões.


2. Alinhamento Estratégico


Demonstre como o projeto contribui para os objetivos do parceiro.


O foco não deve ser a tecnologia, mas sim o valor gerado para a organização.


2.1 Fluxo de Valor


Modele o fluxo de valor da organização.


Mostre:



principais atividades da organização;

entradas e saídas relevantes;

atores envolvidos;

ponto onde o projeto se insere.


Explique como o projeto contribui para melhorar esse fluxo.


2.2 Análise de Stakeholders


Para cada stakeholder, descreva:



papel na organização;

interesse no projeto;

benefícios esperados;

possíveis preocupações ou resistências.


2.3 Processos Impactados


Identifique os processos organizacionais afetados pelo projeto.


Para cada um, descreva:



situação atual;

limitações existentes;

melhorias esperadas após a implantação da solução.


2.4 Objetivos Estratégicos Atendidos


Relacione o projeto aos objetivos estratégicos da organização.


Explique claramente a contribuição do projeto para cada objetivo.


3. Governança de Dados


3.1 Estrutura de Governança


Descreva:



responsáveis pelos dados;

áreas envolvidas;

processos de aprovação;

políticas existentes;

ferramentas utilizadas para gestão de dados.


Caso não exista uma estrutura formal, descreva como as decisões relacionadas aos dados são tomadas.


3.2 Segurança da Informação


Descreva como o parceiro trata aspectos relacionados à segurança dos dados.


Considere:



controle de acesso;

níveis de permissão;

auditoria;

rastreabilidade;

backups;

criptografia;

prevenção de vazamento de informações


3.3 LGPD e Aspectos Regulatórios


Descreva como a organização trata:



dados pessoais;

dados sensíveis;

consentimento;

anonimização;

retenção de dados;

direitos dos titulares.


Indique possíveis impactos dessas restrições no projeto.


3.4 Qualidade dos Dados


Identifique os principais desafios relacionados à qualidade dos dados.


Descreva:



problemas conhecidos;

indicadores utilizados pela organização;

mecanismos de validação;

processos de correção de inconsistências.


4. Especificação dos Requisitos


4.1 Requisitos Funcionais


Cada requisito funcional deve ser descrito utilizando o formato de User Story:


Para cada requisito apresente:



Identificador: RF01, RF02, ...

User Story: descrição da necessidade;

Critérios de Aceitação: lista objetiva de condições que devem ser satisfeitas para que o requisito seja considerado atendido;

Teste de Usuário: descreva como um usuário validaria o requisito na prática.


Todos os requisitos devem ser rastreáveis para funcionalidades analíticas que serão apresentadas posteriormente.


4.2 Requisitos Não Funcionais


Os requisitos não funcionais devem estar alinhados às características de qualidade da ISO 25010.


Cada requisito deve ser descrito no formato:


Como <persona>, eu quero <característica de qualidade> para <benefício>.


Para cada requisito apresente:



Identificador: RNF01, RNF02, ...

Categoria ISO 25010: exemplos: desempenho; segurança; confiabilidade; ...

User Story: descrição da necessidade;

Critérios de Aceitação: condições objetivas para validação;

Teste de Usuário: forma de validação pelo usuário.


5. Especificação da Solução Analítica


Esta seção traduz os requisitos do projeto em dashboards, indicadores e mecanismos de análise. O objetivo não é descrever a implementação técnica, mas sim a solução analítica que será entregue ao parceiro.


5.1 Perguntas de Negócio


Liste as perguntas que a solução deverá responder. Cada pergunta deve estar associada a pelo menos um requisito funcional.


5.2 Indicadores e Métricas de Negócio


Liste os principais indicadores que serão apresentados nos dashboards.


Para cada indicador descreva:



nome;

objetivo;

significado para o negócio;

granularidade de análise;

possíveis dimensões de segmentação.


Não é necessário apresentar fórmulas DAX nesta etapa.


5.3 Dashboards Propostos


Para cada dashboard, apresente:



Nome: nome do dashboard;

Objetivo: problema ou necessidade que o dashboard pretende atender;

Perguntas de Negócio Respondidas: lista das perguntas atendidas;

Indicadores Apresentados: indicadores exibidos no dashboard;

Visualizações Previstas: descreva os visuais pretendidos. Exemplos: gráfico de barras; gráfico de linhas; etc; Justifique a escolha de cada visual;

Filtros e Segmentações: descreva os filtros disponíveis ao usuário;

Protótipo: inclua um esboço, wireframe ou representação preliminar do dashboard.


Não é necessário que o dashboard esteja implementado nesta etapa.


6. Matriz de Rastreabilidade


Monte uma tabela relacionando:



Requisito Funcional;

Pergunta de Negócio;

Dashboard.


Todo requisito funcional deve estar associado a pelo menos um dashboard.


Todo dashboard deve atender a pelo menos um requisito funcional.


 
CRITÉRIOS DE AVALIAÇÃO



Contextualização Organizacional: parceiro, contexto, objetivos e escopo;

Alinhamento Estratégico: fluxo de valor, stakeholders e alinhamento ao negócio;

Governança de Dados: governança, segurança, LGPD e qualidade dos dados;

Requisitos: User Stories, critérios de aceitação e testes;

Especificação Analítica: perguntas de negócio, indicadores, dashboards e protótipos;

Rastreabilidade: relação entre requisitos e dashboards.

---

Este artefato tem como objetivo consolidar as decisões de modelagem dimensional do projeto, estabelecendo a ligação entre o contexto de negócio, os requisitos levantados e a estrutura dos cubos analíticos que comporão o Data Warehouse.


Para seu preenchimento, utilize como principal fonte de informação o documento contexto_organizacional_+_requisitos_da_solução_analítica.md, elaborado na etapa anterior. As informações registradas no canvas devem ser coerentes com o contexto do parceiro, os requisitos definidos e a solução analítica especificada.


O Data Model Canvas deverá ser produzido utilizando a ferramenta disponível em:


https://afonsolelis.github.io/aulas/pages/module-11-eng-software/data-model-canvas.html


Ao finalizar o preenchimento, exporte o arquivo JSON gerado pela ferramenta e salve-o com o nome dmc.json na pasta docs do repositório do grupo.


Preenchimento do Data Model Canvas


Nesta etapa, não é necessário preencher todas as seções do Data Model Canvas. Preencha apenas as seções descritas a seguir.


1. Negócio


Inclua:



objetivos de negócio que motivam o Data Warehouse;

principais perguntas analíticas que a solução deverá responder;

processos de negócio que serão representados pelos cubos analíticos.


As informações registradas devem refletir diretamente os objetivos e requisitos definidos junto ao parceiro.


2. Consumo Analítico


Preencha:



indicadores e métricas de negócio;

usuários e formas de consumo das informações analíticas;

decisões ou riscos ainda existentes relacionados ao consumo dos dados.


As informações desta seção devem representar como os dados serão utilizados para apoiar a tomada de decisão.


3. Governança Corporativa


Preencha:



papéis e responsáveis pelos dados;

políticas de segurança e conformidade;

metadados e maturidade da governança.


Caso alguma informação não esteja disponível junto ao parceiro, registre uma proposta fundamentada para o projeto, indicando claramente que se trata de uma sugestão da equipe.


4. Cubos Analíticos


Crie um card no data model canvas para cada cubo analítico identificado durante a especificação da solução.


Nesta entrega, preencha apenas a subseção "Modelo Dimensional" de cada cubo.


Para cada cubo, complete:



Grão: menor nível de detalhamento da tabela fato;

Estrutura: Star Schema, Snowflake Schema ou outra estrutura adotada;

Tipo de Fato: Transaction Fact, Periodic Snapshot ou Accumulating Snapshot;

Fatos/Eventos: eventos de negócio representados pela tabela fato;

Métricas: principais medidas associadas ao cubo;

Dimensões: perspectivas utilizadas para análise dos fatos;

Dimensões Especiais: quando aplicável, indique Bridge Tables, Junk Dimensions e dimensões conformadas.


As subseções "Dados" e "Governança" dos cubos não deverão ser preenchidas nesta etapa, pois dependem de decisões de implementação e integração que serão realizadas posteriormente.


Entregável


Ao final desta sprint, o grupo deverá entregar o arquivo dmc.json, exportado pela ferramenta e armazenado na pasta docs do repositório;




CRITÉRIOS DE AVALIAÇÃO



coerência entre o Data Model Canvas e o documento de contextualização e requisitos;

qualidade do preenchimento das seções Negócio, Consumo Analítico e Governança Corporativa;

consistência da modelagem dimensional proposta para cada cubo;

adequação da definição do grão, fatos, métricas e dimensões;

correspondência entre os cubos analíticos e os requisitos funcionais do projeto;

organização e completude do arquivo dmc.json entregue.

---

O grupo deverá realizar uma primeira análise matemática das bases de dados do projeto, aplicando os conceitos estudados: unidade de análise, tipos de variáveis, métricas, indicadores, estatística descritiva, granularidade e qualidade
dos dados.


O objetivo é demonstrar que o grupo compreendeu a estrutura quantitativa da base antes de propor dashboards, modelos de dados ou soluções computacionais.


Entrega esperada


O grupo deverá produzir um relatório em markdown, com o nome modelagem_quantitativa_de_dados_do_parceiro.md , na pasta docs do projeto, contendo os seguintes itens:


1. Contextualização quantitativa


Apresente brevemente que processo é representado nas bases de dados e quais decisões podem ser apoiadas por essas informações. Indique também qual é a principal unidade de análise do projeto, como pesquisa, empresa, cliente ou respondente.


2. Unidades de análise e variáveis


Identifique pelo menos três unidades de análise presentes nas bases e explique o que cada uma representa.
Em seguida, escolha pelo menos 10 variáveis relevantes e classifique-as matematicamente como: identificadora, categórica nominal, categórica ordinal, numérica discreta, numérica contínua ou temporal.


3. Qualidade dos dados


Faça uma verificação inicial das bases analisadas, apresentando:



número de registros e colunas;

dados ausentes;

percentual de completude de variáveis importantes;

registros duplicados;

possíveis inconsistências de preenchimento.


Comente como esses problemas podem afetar os indicadores e dashboards do
projeto.


4. Estatística descritiva


Analise as principais variáveis da base.
Para variáveis categóricas, apresente frequências, percentuais e moda.
Para variáveis numéricas, quando houver, apresente média, mediana, mínimo, máximo, amplitude, desvio padrão e coeficiente de variação.
Para variáveis temporais, apresente a distribuição dos registros ao longo do tempo, quando aplicável.


5. Indicadores iniciais


Proponha e calcule pelo menos cinco indicadores relevantes para o projeto. Para cada indicador, apresente nome, objetivo, fórmula, variáveis utilizadas e interpretação.

Exemplos possíveis: volume de pesquisas por período, percentual de pesquisas por status, taxa de adesão por empresa, tempo médio de entrega, taxa de participação de respondentes e percentual de dados ausentes em campos críticos.


6. Granularidade e síntese final


Escolha dois indicadores e explique como sua interpretação pode mudar dependendo da granularidade adotada, por exemplo, por pesquisa, empresa, período ou respondente.
Finalize indicando quais variáveis e indicadores parecem mais importantes para o projeto, quais problemas de qualidade dos dados precisam ser tratados e quais cuidados matemáticos devem ser considerados antes de automatizar os KPIs.


Formato da entrega


O relatório deve conter tabelas, cálculos, gráficos simples e interpretações textuais. O grupo pode incluir notebooks, planilhas e scripts utilizado nos cálculos na pasta docs do projeto, caso existam.


O essencial é que os indicadores sejam matematicamente bem definidos, interpretáveis e coerentes com o problema do projeto.

