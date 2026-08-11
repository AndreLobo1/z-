# Contexto Organizacional + Requisitos da Solução Analítica

Este documento consolida o contexto organizacional do projeto, os requisitos da solução analítica e a especificação inicial dos dashboards previstos para a Sprint 1. A base principal desta versão é formada pelo [TAPI do projeto](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Tapi.md), pelo [Workshop Sindusfarma](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Workshop%20Sindusfarma.md), pela [Apresentação institucional Inteli](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Apresentac%CC%A7a%CC%83o%20institucional%20Inteli.md) e pelo relatório [Modelagem Quantitativa dos Dados do Parceiro](/Users/andrelobo/Downloads/Sidusfarma/docs/modelagem_quantitativa_de_dados_do_parceiro.md). Informações públicas externas podem complementar a narrativa, mas não substituem esses materiais, que são a principal fonte de diferenciação e aderência ao que o parceiro efetivamente apresentou ao grupo.

## 1. Cenário Organizacional e Contexto do Projeto

### 1.1 Visão Geral do Parceiro

O parceiro do projeto é o **Sindusfarma, Sindicato da Indústria de Produtos Farmacêuticos no Estado de São Paulo**, organização de representação setorial voltada ao apoio técnico, regulatório e estratégico às empresas da indústria farmacêutica. Conforme o [TAPI](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Tapi.md), a principal frente de negócio relacionada a este projeto é a **Inteligência de Mercado e Pesquisas**, operacionalizada pela Central de Pesquisas. Essa área conduz levantamentos setoriais e pesquisas aplicadas que subsidiam decisões das empresas participantes.

O contexto institucional apresentado ao grupo mostra um parceiro inserido em um mercado farmacêutico de grande porte e alta relevância econômica, com presença de capital nacional e estrangeiro e com forte peso regulatório, comercial e operacional, como sintetizado na [Apresentação institucional Inteli](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Apresentac%CC%A7a%CC%83o%20institucional%20Inteli.md). O TAPI informa volume aproximado de **120 pesquisas por ano** e cerca de **60 empresas envolvidas por pesquisa**, o que posiciona a Central de Pesquisas como um ativo estratégico de informação para o setor.

Os principais serviços e entregas ligados a esse contexto são a condução de pesquisas setoriais, a consolidação de resultados, a publicação de relatórios e a manutenção de um acervo consultável por participantes e solicitantes. Em termos de propósito institucional no escopo deste projeto, o Sindusfarma busca transformar dados dispersos ao longo do ciclo de pesquisa em informação rastreável, confiável e útil para a tomada de decisão.

### 1.2 Contexto do Negócio

O negócio está inserido em um setor com forte exigência regulatória, necessidade permanente de inteligência de mercado e grande sensibilidade a tempo de resposta, qualidade de informação e comparabilidade histórica. O [Workshop Sindusfarma](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Workshop%20Sindusfarma.md) reforça que o motivador principal do projeto é **garantir governança suficiente para ganhar escala**, ampliando volume e frequência das pesquisas sem multiplicar o esforço manual da equipe.

Os principais desafios hoje são a fragmentação das fontes, a atualização manual dos painéis, a ausência de rastreabilidade ponta a ponta entre solicitação, execução e resultado, a necessidade de verificar dados em múltiplos sistemas e a baixa capacidade de afirmar gargalos operacionais com precisão. O TAPI registra que a Central opera com ferramentas consolidadas por etapa, como Excel, SurveyMonkey, Trello, repositório interno do site e um fluxo em n8n, mas sem integração estruturada entre elas.

As oportunidades identificadas são claras: construir uma fonte única da verdade, acelerar a produção e leitura de indicadores, reduzir retrabalho, melhorar a publicação no site, sustentar um acervo confiável de pesquisas e ampliar a capacidade de análise temporal e comparativa. Entre as tendências relevantes para o projeto estão a centralização analítica em banco de dados em nuvem, a governança de dados como base de escala operacional, o consumo de dashboards por múltiplos perfis de usuário e o uso de dados anonimizados para exploração segura de resultados.

Esses fatores justificam o projeto porque o valor do parceiro não está apenas em coletar respostas, mas em transformar o conjunto de pesquisas em inteligência operacional e estratégica reutilizável. Sem essa estrutura, o conhecimento produzido continua preso a silos e a processos artesanais.

### 1.3 Objetivos do Projeto

Os objetivos abaixo foram formulados com base no [TAPI](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Tapi.md) e no [Workshop Sindusfarma](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Workshop%20Sindusfarma.md):

1. **Centralizar** os dados do ciclo de vida das pesquisas em uma base relacional única na nuvem.
2. **Integrar** as fontes hoje dispersas sem substituir os sistemas operacionais já adotados pelo parceiro.
3. **Automatizar** a produção de indicadores operacionais e estratégicos que hoje dependem de atualização manual.
4. **Rastrear** o fluxo de cada pesquisa da solicitação à publicação no site, com melhor visibilidade de status, prazo e acervo.
5. **Servir** dashboards analíticos que apoiem decisões internas e leitura comparativa de resultados ao longo do tempo.
6. **Fortalecer** a governança e a conformidade no tratamento de dados, com atenção explícita à LGPD e ao controle de acesso por perfil.

Cada objetivo gera valor ao parceiro porque reduz trabalho manual, melhora a confiança nos números divulgados, acelera a leitura gerencial do portfólio de pesquisas e prepara a Central para operar com mais escala e consistência.

### 1.4 Escopo do Projeto

#### Escopo Incluído

O escopo incluído nesta etapa contempla a modelagem e implementação de uma base central para o ciclo de vida das pesquisas, a construção de pipeline de integração e tratamento de dados, a definição dos principais indicadores e a especificação de dashboards analíticos alinhados ao que o parceiro apresentou no TAPI e no workshop. Também estão incluídos os mecanismos de controle de acesso, governança básica de dados e publicação estruturada de informação para consumo interno e externo.

No nível analítico, esta primeira versão concentra a solução em dois dashboards priorizados pelo grupo: **Report 02 - Prazos & SLA** e **Report 11 - Comparativo Anual & Tendências**, ambos já detalhados nos mockups textuais fornecidos pelo parceiro em [relatorio_02.md](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/esboc%CC%A7o%20de%20relato%CC%81rios/relatorio_02.md) e [relatorio_11.md](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/esboc%CC%A7o%20de%20relato%CC%81rios/relatorio_11.md).

#### Escopo Não Incluído

Não faz parte do projeto substituir SurveyMonkey, Trello, repositório público, Excel ou outros sistemas operacionais utilizados hoje pelo Sindusfarma. Também não faz parte desta etapa alterar os métodos de coleta, o desenho das pesquisas ou a lógica de captura junto aos participantes. A coleta permanece como está e só deve mudar futuramente se o próprio Sindusfarma entender que essa revisão faz sentido. O trabalho do grupo é **capturar, tratar, integrar, governar e servir os dados**, não redefinir as fontes de coleta.

Também ficam fora do escopo desta sprint o tratamento de dados pessoais reais sem anonimização adequada, a formalização jurídica completa de políticas internas do parceiro e a implementação integral de todos os relatórios previstos no conjunto de mockups.

## 2. Alinhamento Estratégico

### 2.1 Fluxo de Valor

O fluxo de valor central da área pode ser resumido em seis etapas: solicitação da pesquisa, planejamento do instrumento, coleta das respostas, consolidação dos dados, produção de indicadores e publicação dos resultados no site/acervo. As entradas principais são solicitações de associados, demandas recorrentes da área e respostas coletadas nas pesquisas. As saídas principais são relatórios consolidados, indicadores operacionais, dashboards gerenciais e acervo consultável.

Os atores envolvidos nesse fluxo são a equipe interna da Central de Pesquisas, as áreas técnicas do Sindusfarma, os solicitantes das pesquisas, as empresas participantes e os consumidores dos relatórios publicados. O projeto se insere no ponto em que o fluxo hoje perde eficiência: a transição entre as etapas operacionais e a consolidação analítica. Seu papel é transformar esse trecho fragmentado em um fluxo governado, rastreável e reaproveitável.

O projeto melhora esse fluxo ao reduzir conferência manual, dar continuidade informacional entre as etapas, fortalecer a publicação no site e permitir análise de KPIs e tendências sem necessidade de reconstituir a história da pesquisa a cada consulta.

### 2.2 Análise de Stakeholders

| Stakeholder | Papel na organização | Interesse no projeto | Benefícios esperados | Possíveis preocupações ou resistências |
| :--- | :--- | :--- | :--- | :--- |
| Equipe interna da Central de Pesquisas | Opera o fluxo, acompanha status e entrega resultados | reduzir esforço manual e ganhar rastreabilidade | visão operacional integrada, atualização mais rápida e menor retrabalho | receio de transição de rotina, dependência de dados incompletos |
| Áreas técnicas do Sindusfarma | validam questionários, acompanham adesão e qualidade da informação | melhorar consistência e comparabilidade das análises | acesso mais simples a indicadores, melhor alinhamento regulatório e analítico | preocupação com qualidade dos dados e semântica dos indicadores |
| Liderança de negócio da Central | patrocina e valida a utilidade da solução | aumentar escala, governança e visibilidade gerencial | apoio à tomada de decisão, visão consolidada e melhor gestão do portfólio | preocupação com aderência do dashboard ao negócio real |
| Solicitantes das pesquisas | demandam levantamentos e consomem resultados | obter respostas mais rápidas e resultados mais confiáveis | acervo mais acessível, melhor tempo de resposta e visão comparativa | preocupação com atraso, clareza e completude dos relatórios |
| Empresas participantes | fornecem respostas e consultam publicações permitidas | ter confiança na preservação e no uso correto dos dados | anonimização, maior utilidade analítica dos resultados e visão setorial mais clara | preocupação com LGPD, confidencialidade e exposição indevida |

### 2.3 Processos Impactados

| Processo | Situação atual | Limitações existentes | Melhorias esperadas |
| :--- | :--- | :--- | :--- |
| Planejamento e acompanhamento das pesquisas | acompanhamento distribuído entre múltiplas ferramentas | status e histórico não ficam consolidados automaticamente | visão operacional unificada do ciclo das pesquisas |
| Análise de KPIs | leitura gerencial depende de atualização manual e reconciliação entre fontes | atraso, retrabalho e baixa rastreabilidade | indicadores automáticos, replicáveis e comparáveis |
| Publicação no site e manutenção do acervo | repositório público é alimentado sem integração plena com a base operacional | risco de inconsistência entre interno e publicado | publicação mais consistente e acervo alinhado à base central |
| Gestão de qualidade dos dados | correções dependem de tratamento manual e heterogêneo | inconsistências de domínio, órfãos e baixa completude em campos críticos | regras de padronização, deduplicação e saneamento explícitas |

### 2.4 Objetivos Estratégicos Atendidos

O projeto atende diretamente ao objetivo de tornar o Sindusfarma uma referência em dados do setor, objetivo explicitado no [Workshop Sindusfarma](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Workshop%20Sindusfarma.md). Também contribui para o ganho de escala da Central de Pesquisas, para a redução da dependência de atualização manual e para o fortalecimento da governança da informação. Em vez de apenas informatizar relatórios, a solução proposta cria uma base analítica contínua para decisões operacionais, priorização de pesquisas, acompanhamento de adesão, leitura de prazos e publicação estruturada de conhecimento setorial.

## 3. Governança de Dados

### 3.1 Estrutura de Governança

O material disponível não comprova a existência de uma estrutura formal completa de governança com comitê documentado, políticas corporativas detalhadas e matriz formal de stewardship. O que o [TAPI](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Tapi.md) e o [Workshop Sindusfarma](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Workshop%20Sindusfarma.md) mostram com segurança é uma governança **operacionalmente ativa**, com responsáveis identificáveis e com forte preocupação prática com qualidade, acesso e rastreabilidade.

No material do projeto aparecem como papéis centrais Felipe Fernandes Rojas na liderança técnica, Reinaldo Nobrega na liderança de negócio e Fabio Moreira como liderança executiva da Central de Pesquisas. As áreas envolvidas incluem a equipe interna da Central, as áreas técnicas do Sindusfarma e os usuários externos que consultam ou alimentam partes do fluxo.

Quanto a processos de aprovação, há evidência de validação operacional de questionários e acompanhamento por áreas técnicas, mas não há descrição formal completa do rito de aprovação de dados. Quanto a ferramentas, o ecossistema atual envolve Excel, SurveyMonkey, Trello, repositório interno do site, fluxo em n8n e a proposta de um banco central e camada analítica em nuvem.

Como proposta fundamentada da equipe para registrar no artefato, faz sentido assumir para o projeto os seguintes papéis-alvo: **Data Owner de negócio** na Central de Pesquisas, **Data Custodian técnico** na equipe de dados/engenharia, e **responsáveis explícitos por qualidade, acesso e publicação** na camada analítica.

### 3.2 Segurança da Informação

O [Workshop Sindusfarma](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/Workshop%20Sindusfarma.md) fornece base suficiente para afirmar que o parceiro espera autenticação obrigatória, controle de acesso baseado em papéis, anonimização de dados e separação entre contextos de desenvolvimento/teste e produção. Também foi explicitada a intenção de herdar permissões até a camada de BI.

Por outro lado, os materiais consultados não detalham política implantada de backups, criptografia, auditoria de acesso ou prevenção de vazamento em nível operacional. Por isso, esta primeira versão registra como fato o que está evidenciado nos materiais e, como proposta da equipe, recomenda que a solução final inclua logs de acesso, trilha de auditoria para publicação no site, backups automatizados e segregação clara entre dados sensíveis, analíticos e públicos.

### 3.3 LGPD e Aspectos Regulatórios

Há forte evidência, tanto no TAPI quanto no workshop, de que a conformidade com a LGPD é requisito central do projeto. O parceiro destacou que dados reais de empresas participantes, respostas individuais identificáveis e contatos não devem ir para contexto público, e que ambientes públicos ou acadêmicos devem operar com dados anonimizados ou fictícios.

Também ficou claro que o tratamento de dados sensíveis e identificáveis deve respeitar anonimização desde a entrada analítica, especialmente para consumo externo. O material disponível não descreve em detalhe política de retenção, fluxo de direitos dos titulares ou base legal formalizada para cada tratamento. Portanto, nesta versão esses elementos devem ser descritos como pontos a aprofundar com o parceiro, sem impedir a especificação da solução.

Os impactos dessas restrições no projeto são diretos: a camada analítica precisa separar consumo interno e externo, proteger respostas individuais, controlar acesso por perfil e evitar qualquer publicação que permita reidentificação indevida.

### 3.4 Qualidade dos Dados

O diagnóstico de qualidade já foi consolidado no relatório [Modelagem Quantitativa dos Dados do Parceiro](/Users/andrelobo/Downloads/Sidusfarma/docs/modelagem_quantitativa_de_dados_do_parceiro.md). Os principais problemas conhecidos são heterogeneidade em domínios, baixa completude em variáveis operacionais críticas, colunas sem valor analítico, registros órfãos em relações com `pesquisas.csv` e fragilidade de campos importantes para SLA detalhado, como `complexidade`, `data_aprov`, `hora_inicio` e `hora_termino`.

Os indicadores de qualidade já disponíveis para o projeto incluem completude geral, completude de variáveis críticas, presença de órfãos referenciais, colunas 100% nulas e inconsistências de domínio. Como mecanismos de validação, a equipe já possui auditoria de completude, verificação de integridade referencial e tratamento quantitativo de lacunas. Como processo corretivo proposto, recomenda-se quarentena de registros órfãos, normalização de domínio, derivação de flags operacionais e sinalização explícita de cobertura parcial nos KPIs.

## 4. Especificação dos Requisitos

### 4.1 Requisitos Funcionais

| ID | User Story | Critérios de Aceitação | Teste de Usuário |
| :--- | :--- | :--- | :--- |
| RF01 | Como equipe interna da Central de Pesquisas, eu quero consolidar os dados das pesquisas em uma base central para reduzir a dependência de cruzamentos manuais. | a solução integra pelo menos as bases principais do projeto; os dados ficam acessíveis em estrutura única; a origem dos registros permanece rastreável | um usuário interno consulta informações de pesquisa, participação e publicação sem recorrer a planilhas paralelas |
| RF02 | Como gestor da Central, eu quero acompanhar indicadores de prazo e ciclo das pesquisas para identificar atrasos e priorizar ação operacional. | o dashboard apresenta ciclo total, dias úteis aberta, dias para tabulação e prorrogações; é possível filtrar por período e tipo; casos fora do padrão ficam visíveis | o gestor acessa o dashboard 02, aplica filtros e identifica pesquisas fora do comportamento esperado |
| RF03 | Como área técnica, eu quero comparar períodos e tendências das pesquisas para entender mudanças no portfólio e no engajamento ao longo do tempo. | o dashboard apresenta evolução temporal, comparações entre períodos e indicadores por ano/onda; o usuário consegue segmentar a leitura | a área técnica acessa o dashboard 11 e compara evolução entre períodos consecutivos |
| RF04 | Como usuário analítico autorizado, eu quero filtros por tempo, status e tipo para refinar a leitura dos dados conforme minha necessidade. | os dashboards possuem filtros compatíveis com as perguntas de negócio; os recortes alteram os indicadores exibidos de forma coerente | o usuário altera filtros e verifica mudança consistente dos números e visuais |
| RF05 | Como organização, eu quero publicar informações analíticas de forma consistente com o acervo do site para reduzir divergência entre o que é gerido internamente e o que é divulgado externamente. | a solução prevê integração lógica entre base central e publicação; o acervo passa a depender da base governada; não há necessidade de duplicar manutenção manual | um responsável valida que a informação publicada deriva da mesma base analítica usada nos painéis |
| RF06 | Como administrador, eu quero controlar o acesso por perfil para proteger dados internos e restringir o consumo conforme o papel do usuário. | há diferenciação entre perfis interno, técnico e externo; dados sensíveis não aparecem em contexto público; o consumo externo opera sobre informação anonimizada | um usuário externo não consegue acessar visões internas e um usuário interno acessa visões gerenciais completas |

### 4.2 Requisitos Não Funcionais

| ID | Categoria ISO 25010 | User Story | Critérios de Aceitação | Teste de Usuário |
| :--- | :--- | :--- | :--- | :--- |
| RNF01 | Segurança | Como organização, eu quero controle de acesso por perfil para proteger dados internos e sensíveis. | autenticação obrigatória; separação entre perfis; visões públicas sem dados identificáveis | validar acessos com usuários de perfis diferentes |
| RNF02 | Confiabilidade | Como gestor, eu quero números consistentes entre base, indicadores e publicação para confiar nas análises. | indicadores reproduzíveis; mesma lógica entre dashboards e base; tratamento explícito de lacunas | confrontar amostras do dashboard com a base central e os cálculos documentados |
| RNF03 | Desempenho | Como usuário analítico, eu quero painéis com resposta adequada para explorar filtros sem travamento. | consultas principais respondem em tempo aceitável para uso gerencial; filtros não inviabilizam a navegação | aplicar filtros centrais e medir resposta percebida pelo usuário |
| RNF04 | Usabilidade | Como usuário de negócio, eu quero dashboards claros para interpretar tendências e gargalos sem depender da equipe técnica. | títulos, filtros e visuais usam linguagem de negócio; leitura executiva é possível sem treinamento avançado | pedir que um usuário de negócio responda perguntas do dashboard sem apoio técnico |
| RNF05 | Manutenibilidade | Como equipe do projeto, eu quero pipeline e regras documentadas para evoluir os dashboards sem retrabalho excessivo. | regras de tratamento e fontes ficam documentadas; indicadores têm definição rastreável | um novo membro da equipe entende origem e cálculo dos indicadores a partir da documentação |
| RNF06 | Compatibilidade | Como organização, eu quero que a solução conviva com as ferramentas atuais sem forçar substituição imediata das fontes de coleta. | integração com fontes atuais; escopo não exige troca de SurveyMonkey, Trello ou métodos de coleta | validar que o fluxo proposto usa as fontes existentes como entrada |

## 5. Especificação da Solução Analítica

### 5.1 Perguntas de Negócio

| ID | Pergunta de Negócio | Requisito Funcional associado |
| :--- | :--- | :--- |
| PN01 | Qual é o ciclo total médio e mediano entre solicitação e divulgação das pesquisas? | RF02 |
| PN02 | Quanto tempo as pesquisas permanecem abertas e quanto tempo a tabulação consome? | RF02 |
| PN03 | Quais pesquisas estão mais sujeitas a atraso ou prorrogação? | RF02 |
| PN04 | Como o volume de pesquisas evolui ao longo do tempo? | RF03 |
| PN05 | O portfólio está mudando em composição, status ou tipo ao longo dos períodos? | RF03 |
| PN06 | Como a adesão e outros indicadores variam entre anos ou ondas? | RF03 |
| PN07 | Quais recortes temporais e operacionais precisam de atenção prioritária da equipe? | RF02, RF03, RF04 |

### 5.2 Indicadores e Métricas de Negócio

| Indicador | Objetivo | Significado para o negócio | Granularidade de análise | Possíveis dimensões de segmentação |
| :--- | :--- | :--- | :--- | :--- |
| Ciclo médio da pesquisa | medir tempo médio entre solicitação e divulgação | mostra velocidade operacional agregada | pesquisa, período | tempo, tipo, área |
| Ciclo mediano da pesquisa | medir valor central mais robusto do ciclo | reduz distorção causada por extremos | pesquisa, período | tempo, tipo, área |
| Média de dias úteis aberta | medir janela de coleta | indica quanto tempo a pesquisa permanece disponível | pesquisa, período | tempo, tipo |
| Média de dias para tabulação | medir esforço pós-coleta | mostra custo operacional da etapa de consolidação | pesquisa, período | tempo, tipo |
| Taxa de pesquisas prorrogadas | medir peso de prorrogações | sinaliza fragilidade de prazo ou necessidade de ajuste operacional | pesquisa, período | tempo, tipo, área |
| Volume de pesquisas por período | medir produção ao longo do tempo | mostra ritmo do portfólio | período | ano, trimestre, tipo, status |
| Volume de pesquisas finalizadas por período | medir entregas concluídas | mostra capacidade de fechamento do fluxo | período | ano, trimestre, tipo |
| Crescimento do volume vs. período anterior | medir tendência de expansão ou retração | apoia leitura executiva do portfólio | período | ano, trimestre |
| Volume de pesquisas em andamento | medir carga operacional corrente | mostra pressão atual sobre a equipe | período | status, tipo |
| Variação de adesão entre períodos | medir mudança de engajamento ao longo do tempo | ajuda a interpretar mudança de comportamento da base | período | ano, onda, tipo |

### 5.3 Dashboards Propostos

#### Dashboard 1: Report 02 - Prazos & SLA

**Objetivo:** apoiar o acompanhamento interno dos tempos operacionais do ciclo de pesquisa, destacando atrasos, prorrogações e comportamento agregado de prazo.

**Perguntas de Negócio Respondidas:** PN01, PN02, PN03, PN07.

**Indicadores Apresentados:** ciclo médio, ciclo mediano, média de dias úteis aberta, média de dias para tabulação, taxa de pesquisas prorrogadas.

**Visualizações Previstas:** linha temporal do ciclo ao longo do tempo para leitura de tendência; cartões para métricas centrais de prazo; tabela de pesquisas fora do padrão para ação operacional; barras por recorte de tipo ou área quando a segmentação for consistente. A linha é apropriada para evolução temporal, cartões para leitura executiva rápida e tabela para priorização operacional.

**Filtros e Segmentações:** período, tipo de pesquisa, área, status. O uso de `complexidade` deve aparecer apenas como filtro experimental ou secundário, nunca como eixo confiável principal nesta versão, porque o próprio relatório quantitativo mostrou baixa cobertura desse campo.

**Protótipo:** referência nos mockups fornecidos pelo parceiro em [relatorio_02.md](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/esboc%CC%A7o%20de%20relato%CC%81rios/relatorio_02.md) e [relatorio_02.png](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/esboc%CC%A7o%20de%20relato%CC%81rios/relatorio_02.png).

#### Dashboard 2: Report 11 - Comparativo Anual & Tendências

**Objetivo:** apoiar a leitura de evolução do portfólio e de mudança de comportamento dos indicadores entre anos ou ondas comparáveis.

**Perguntas de Negócio Respondidas:** PN04, PN05, PN06, PN07.

**Indicadores Apresentados:** volume de pesquisas por período, volume finalizado por período, crescimento vs. período anterior, variação de adesão entre períodos, tendência-chave.

**Visualizações Previstas:** linha de evolução temporal dos principais indicadores; composição por ano ou onda em barras empilhadas ou agrupadas; tabela do que mais mudou entre períodos. A linha é a melhor escolha para tendência, a composição por período ajuda a comparar estrutura, e a tabela evidencia mudanças que exigem interpretação qualitativa adicional.

**Filtros e Segmentações:** período, tipo, status, área e, quando houver critério padronizado, onda. O termo “onda” deve entrar no dashboard apenas depois de regra explícita de definição.

**Protótipo:** referência nos mockups fornecidos pelo parceiro em [relatorio_11.md](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/esboc%CC%A7o%20de%20relato%CC%81rios/relatorio_11.md) e [relatorio_11.png](/Users/andrelobo/Downloads/Sidusfarma/CONTEXTO_PROJETO/esboc%CC%A7o%20de%20relato%CC%81rios/relatorio_11.png).

## 6. Matriz de Rastreabilidade

| Requisito Funcional | Pergunta de Negócio | Dashboard |
| :--- | :--- | :--- |
| RF01 | PN01, PN02, PN04, PN05 | Report 02, Report 11 |
| RF02 | PN01, PN02, PN03, PN07 | Report 02 |
| RF03 | PN04, PN05, PN06, PN07 | Report 11 |
| RF04 | PN01, PN02, PN04, PN05, PN06, PN07 | Report 02, Report 11 |
| RF05 | PN05, PN07 | Report 11 |
| RF06 | PN03, PN07 | Report 02, Report 11 |

Essa matriz foi construída para garantir que todo requisito funcional esteja associado a pelo menos um dashboard e que todo dashboard atenda a pelo menos um requisito funcional. O Report 02 concentra leitura operacional de prazo e o Report 11 concentra leitura temporal e comparativa, formando juntos a base analítica inicial priorizada pelo grupo.
