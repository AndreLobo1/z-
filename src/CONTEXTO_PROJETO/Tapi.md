PROJETO PARCEIRO

ESMD11 - Arquitetura e governança de dados
alinhada à estratégia corporativa

PROJETO: Governança e Integração de Dados da Central de Pesquisas

EMPRESA: Sindusfarma — Sindicato da Indústria de Produtos Farmacêuticos no Estado de São Paulo

BREVE DESCRIÇÃO EMPRESA / MINI BIO: O Sindusfarma é uma das principais entidades de
representação da indústria farmacêutica no Brasil, atuando no apoio técnico, regulatório e estratégico às empresas
do setor. Entre suas frentes de serviço ao associado está a Central de Pesquisas, responsável por conduzir estudos
de mercado e levantamentos setoriais que subsidiam as decisões das empresas participantes — com volume
aproximado de 120 pesquisas por ano e cerca de 60 empresas envolvidas por pesquisa.

PROFESSOR ORIENTADOR: Hermano Peixoto

OVERVIEW

●  PRINCIPAL ÁREA DE NEGÓCIO: Inteligência de Mercado e Pesquisas
●  LÍDER DO PROJETO: Felipe Fernandes Rojas – Analista de Dados Sr.
●  PONTO FOCAL BACKUP: Reinaldo Nobrega – Coordenador de Dados

                 Lucas Andrade – Analista de Dados Jr.
LÍDER TÉCNICO: Felipe Fernandes Rojas – Analista de Dados Sr
LÍDER DE NEGÓCIO: Reinaldo Nobrega – Coordenador de Dados
LÍDER EXECUTIVO [Onboarding Executivo]: Fabio Moreira – Gestor da Central de Pesquisas

●
●
●

ESBOÇO DO PROJETO

●  PROBLEMA: A Central de Pesquisas opera um volume expressivo de pesquisas ao ano com

ferramentas consolidadas em cada etapa (Excel, SurveyMonkey, Trello e o repositório interno do site),
porém sem integração estruturada entre elas. Hoje o único ponto de conexão é um workﬂow em n8n que
apenas replica novas solicitações, sem consolidar nem governar o dado ao longo do ciclo de vida da
pesquisa. Como consequência, o dashboard é atualizado manualmente, o repositório publicado é um silo
isolado, não há rastreabilidade automatizada entre solicitação, execução e resultado, e as decisões
estratégicas dependem de cruzamentos manuais em planilhas. A área possui dados valiosos, mas não
uma arquitetura que os torne completamente acessíveis e conﬁáveis.

●  OBJETIVO: Construir a espinha dorsal de dados da Central de Pesquisas — integrando as fontes

existentes, estruturando um banco de dados centralizado na nuvem, garantindo governança e qualidade
do dado em cada etapa do ﬂuxo e entregando um data app com dashboards operacionais e estratégicos
que eliminem a dependência de atualizações manuais.

●  BENEFÍCIOS ESPERADOS PARA O PARCEIRO: Fonte única da verdade para o ciclo de vida
das pesquisas; rastreabilidade e auditabilidade ponta a ponta (da solicitação à publicação); visibilidade
consolidada de indicadores estratégicos em tempo real; redução do esforço manual de atualização e
tabulação; maior conﬁabilidade e consistência entre o sistema interno e o acervo publicado; e
conformidade com a LGPD no tratamento de dados de empresas parceiras e respostas individuais.

●  MATERIAIS DE ESTUDOS ANEXADOS: <Detalhar>

DESCRIÇÃO CURTA DO PROJETO
Arquitetura de dados que centraliza, governa e visualiza dados de pesquisas setoriais.

ESCOPO MACRO
Espera-se a entrega de um data app funcional que atue como central de governança e inteligência operacional da
área, contemplando:

●

●

Arquitetura de dados integrada: modelagem e implementação de um banco de dados relacional na
nuvem (Amazon RDS, Google Cloud SQL ou equivalente) que consolide informações hoje dispersas entre
Excel, SurveyMonkey, Trello e o repositório do site, cobrindo o ciclo completo de uma pesquisa — da
solicitação à publicação — com rastreabilidade em cada etapa.
Pipeline de integração de dados: conectores e rotinas de ingestão que alimentem o banco central a
partir das fontes existentes, com tratamento de inconsistências, deduplicação e padronização. O n8n
atual poderá ser aproveitado como camada de orquestração, mas a arquitetura deve ir além do registro
pontual de novas solicitações e cobrir todo o ﬂuxo.

●  Data app com dashboards operacionais e estratégicos: interface intuitiva com KPIs como volume de

pesquisas por período, taxa de adesão por empresa e departamento, tempo médio de entrega, status em
tempo real de cada pesquisa em andamento e acervo consultável de pesquisas publicadas.

●  Governança e qualidade de dados: protocolos de validação, controle de acesso por perﬁl de usuário

●

(equipe interna, áreas técnicas e solicitantes externos) e conformidade com a LGPD.
Integração com o repositório público do site: o acervo disponível a participantes e solicitantes passa a
ser alimentado automaticamente pelo banco central, eliminando a atualização manual e garantindo
consistência entre o sistema interno e o publicado externamente.

Público-alvo / quem utilizará: usuário principal = equipe interna da Central de Pesquisas (opera o ﬂuxo e
acompanha indicadores); usuário secundário = áreas técnicas do Sindusfarma (validam questionários e
acompanham adesão); usuário terciário = solicitantes e participantes (consultam o acervo público e baixam
resultados). Quem validará: equipe da Central de Pesquisas. Ambiente de uso: ambiente web/nuvem, acessado
pela equipe interna e pelas áreas técnicas, com camada pública para o acervo.

MVP
Versão mínima funcional contendo: (1) banco de dados relacional na nuvem modelando o ciclo de vida de uma
pesquisa (solicitação → planejamento → execução → resultado); (2) pelo menos um pipeline de ingestão funcional
consolidando dados de pelo menos uma das fontes atuais (ex.: respostas do SurveyMonkey e/ou base em Excel) no
banco central, com tratamento básico de inconsistências e deduplicação; (3) dashboard com um conjunto inicial de
KPIs operacionais e estratégicos atualizados a partir do banco central (sem atualização manual); e (4) controle de
acesso por perﬁl de usuário, com tratamento de dados sensíveis em conformidade com a LGPD.

DADOS DISPONIBILIZADOS
Este projeto conta com um Agente de IA em .json responsável por integrar a chegada de uma nova solicitação no
nosso sistema interno, otimizar o questionário com um LLM, criar lista de tarefas no Trello, criar questionário no
SurveyMonkey, alimentar nossa planilha e organizar e-mails e pastas no Outlook.

Também conta com as seguintes bases de dados:

o

o

o

o

pesquisas.csv: ~400 registros x 27 colunas

clientes.csv: ~6.000 registros x 5 colunas

respondentes.csv: ~20.000 registros x 6 colunas

empresas.csv: ~800 registros x 9 colunas

Todas essas bases contêm dados estruturados e representam somente 3MB de dados

DEMAIS ENTREGÁVEIS
Modelo de dados documentado (diagrama entidade-relacionamento); documentação da arquitetura e do pipeline
de integração; documentação dos protocolos de governança, qualidade e conformidade com a LGPD; e
manual/orientação de uso do data app para a equipe da Central de Pesquisas.

RESTRIÇÕES / O PROJETO NÃO CONTEMPLA

Substituição das ferramentas operacionais atuais (SurveyMonkey, Trello, Repositório público etc.) — o projeto
integra e governa, não as substitui;

Tratamento de dados pessoais reais sem anonimização/mascaramento quando aplicável;

CONTEÚDO RESTRITO
Como o projeto é publicado no GitHub/site do Inteli, devem ser restritos ao compartilhamento aberto: bases com
dados reais de empresas participantes, respostas individuais identiﬁcáveis e dados de contato. Sugere-se que o
repositório público utilize dados anonimizados ou ﬁctícios.

STAKEHOLDERS
Equipe interna da Central de Pesquisas (operação e gestão); áreas técnicas do Sindusfarma (validação de
questionários e acompanhamento de adesão); indústrias farmacêuticas participantes e solicitantes das pesquisas
(fornecem e consomem dados)

CHECKLIST  DE  IMPACTO  OPERACIONAL  E  ALINHAMENTO  DO  PROJETO  COM  OS

OBJETIVOS  DE  DESENVOLVIMENTO  SUSTENTÁVEL  (ODS)  DA  AGENDA  2030  DA

ONU

Esta seção avalia a proposta de valor do projeto em duas frentes complementares. A primeira

parte  foca  nos  impactos  operacionais,  buscando  entender  os  benefícios  práticos  para  a

organização.

A  segunda  analisa  o  alinhamento  do  Projeto  com  os  Objetivos  de  Desenvolvimento

Sustentável  (ODS),  a  agenda  global da ONU para um futuro melhor, estruturada nas suas 5

dimensões: Pessoas, Planeta, Prosperidade, Paz e Parcerias (para saber mais, acesse aqui).

Avalie  abaixo  como  seu  projeto  se  conecta  a  essas  duas  frentes,  marcando  as  opções

aplicáveis e descrevendo a iniciativa no campo de observações.

Impactos Operacionais do Projeto

●

 Prática ou Contribuições Gerenciais (Foco em problemas práticos)

●  O projeto contribui para a resolução ou minimização de um problema prático (dentro

da empresa)? Sim

●  O projeto promove competências para práticas de projetos de software? Sim

Observações (Gerais): O projeto resolve um gargalo operacional concreto (fragmentação de dados e
atualizações  manuais)  e  desenvolve  competências  em  arquitetura,  integração, governança de dados e

visualização.

Alinhamento do Projeto com ODS

●  Dimensão 1: Pessoas (Foco em dignidade, igualdade e bem-estar)
●

(ODS 1, 2, 3) O projeto contribui para a erradicação da pobreza, fome zero, ou para a
promoção da saúde e bem-estar?
(ODS  4,  5)  O  projeto promove educação de qualidade ou a igualdade de gênero e o
empoderamento de mulheres e meninas?

●

●  Não se aplica

Observações (Pessoas):

●  Dimensão 2: Planeta (Foco na proteção dos ecossistemas e combate às mudanças

climáticas)
(ODS 6, 12) O projeto promove a gestão sustentável da água e o consumo e produção

responsáveis (ex: economia circular)?

(ODS  13,  14,  15)  O  projeto  contribui  para  a  ação  climática  ou  para  a  proteção  e

●

●

recuperação da vida na água e na terra?

●  Não se aplica

Observações (Planeta):

●  Dimensão  3:  Prosperidade  (Foco  no  crescimento  econômico  inclusivo  e  em

harmonia com a natureza)
(ODS  8,  10)  O  projeto  promove  trabalho  decente  e  o  crescimento  econômico,

contribuindo para a redução das desigualdades?

(ODS  7,  11)  O  projeto  promove o acesso a energias limpas ou o desenvolvimento de

●

●

cidades e comunidades mais sustentáveis?

●  Não se aplica

Observações (Prosperidade):

●  Dimensão 4: Paz (Foco na promoção de sociedades pacíﬁcas, justas e inclusivas)
●

(ODS 16) O projeto fortalece instituições de forma ética e responsável, promovendo a

transparência, a justiça e a paz?

●  Não se aplica

Observações (Paz):

●  Dimensão 5: Parcerias (Foco na colaboração para alcançar os objetivos)
●

(ODS 9, 17) O projeto representa uma inovação para a indústria e infraestrutura e se

baseia em parcerias estratégicas para potencializar seu impacto?

●  Sim

Observações (Parcerias): o projeto é inovação aplicada em infraestrutura de dados e nasce de uma
parceria estratégica entre Sindusfarma e Inteli.

