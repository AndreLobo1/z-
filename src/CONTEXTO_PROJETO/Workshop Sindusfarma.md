# **Documento de Consolidação de Requisitos do Projeto**

## **1\. Visão Geral e Objetivos do Projeto**

* **Motivador Principal:** Garantir a governança necessária para ganhar escala, aumentando o volume e a frequência das pesquisas realizadas.  
* **Objetivo Estratégico:** Posicionar a entidade (**Sindusfarma**) como a principal referência em dados do setor, atingindo **mais de 50% de participação frequente** das empresas da indústria nas pesquisas.  
* **Exemplos de objetos das pesquisas:** Levantamentos sobre assuntos regulatórios, legislação e gestão de RH (ex.: pesquisas sobre *Home Office*, *Short Friday*), permitindo a geração de **produtos de dados e relatórios personalizados** para a indústria.

## **2\. Perfis de Usuário, Acessos e Governança (RBAC)**

### **Perfis de Usuários (Roles)**

| Perfil | Quantidade Estimada | Descrição & Responsabilidades |
| :---- | :---- | :---- |
| **Administrador** | 3 a 4 pessoas | Gestão total da plataforma, configuração de pesquisas e aprovações do fluxo. |
| **Equipe Interna** | Até 45 pessoas | Usuários operacionais que gerenciam o ciclo de vida das pesquisas e análises. |
| **Usuários Externos / Participantes** | N/A | Respondentes anônimos das pesquisas da indústria. |

### **Governança e Segurança**

* **Autenticação:** Obrigatória para qualquer tipo de acesso ao sistema de pesquisas.  
* **Controle de Acesso Baseado em Papéis (RBAC):** As *roles* atribuídas aos usuários gerenciarão automaticamente as permissões de acesso aos dados diretamente na camada do banco de dados/DW.  
* **Integração com BI:** Login e nível de visualização no **Power BI** atrelados e herdados diretamente da *role* do usuário.  
* **Anonimização de Dados:**  
  * As empresas participantes das pesquisas são rigorosamente **anônimas**.  
  * Todos os dados coletados passam por um processo de anonimização na entrada.  
  * **Estratégia Dev/Prod:** Durante o desenvolvimento/testes, o dashboard rodará com dados fictícios/anonimizados. Ao ser implantado em produção, fará a conversão para os dados reais do ambiente produtivo.

## **3\. Arquitetura de Dados, Integrações e Fluxo (ETL/ELT)**

### **Componentes do Pipeline**

> 1. **Fontes de Dados Iniciais:**  
   * 4 arquivos CSV de carga inicial / integração.  
   * **Fonte Única da Verdade (SSOT):** O **Excel** é definido como o *Single Source of Truth* em situações onde houver divergência de informações.  
> 2. **Persistência / Armazenamento:**  
   * **Data Warehouse (Analítico):** **ClickHouse** será a tecnologia adotada para suportar a volumetria, agregação e performance analítica.  
   * **Ingestão Contínua:** O DW receberá novas inserções em tempo real/streaming enquanto as pesquisas estiverem abertas e recebendo respostas.  
> 3. **Interface de Relatórios & BI:**  
   * Relatórios e dashboards operacionais/executivos consumirão os dados consolidados no ClickHouse.

### **Regras de Tratamento e Qualidade dos Dados**

* **Limpeza e Transformação:** Implementação de regras automatizadas para sanitização dos dados antes da carga no DW.  
* **Tratamento de Duplicidades:** Algoritmos para identificar e tratar **respostas duplicadas vindas do mesmo correspondente**.  
* **Unificação de Fontes:** Eliminar o processo manual de verificação cruzada de múltiplas fontes para melhorar a **acurácia dos resumos gerados por IA** e o alinhamento com áreas regulatórias.

## **4\. Métricas de Sucesso, KPIs e SLAs Operacionais**

### **Targets de Eficiência Operacional (SLAs)**

| Indicador de Desempenho | Situação Atual (As-Is) | Meta Projetada (To-Be) | Ganho de Eficiência Esperado |
| :---- | :---- | :---- | :---- |
| **Tempo Total do Ciclo da Pesquisa** | Média de **21 dias úteis** | **15 a 17 dias úteis** | Redução de \~20% a 28% no tempo total |
| **Geração do Relatório Pós-Pesquisa** | Média de **5 dias úteis** | **1 a 2 dias úteis** | Redução de \~60% a 80% no tempo de emissão |

### **Dashboards e Visualização (2 Views)**

> 1. **View 1: Gestão Interna (Sindusfarma)**  
   * Acompanhamento operacional do ciclo de vida das pesquisas.  
   * Métrica de pesquisas ativas vs. finalizadas por ano.  
   * SLA de tempo de resposta e tempo gasto pela equipe interna.  
> 2. **View 2: Visualização de Resultados**  
   * Dashboard interativo para exploração dos dados consolidados e anonimizados do setor.  
   * Geração de relatórios analíticos de mercado e benchmarking setorial.

## **5\. Dores Atuais a Serem Resolvidas pelo Projeto**

> 1. **Gargalo em Verificação Manual:** A necessidade atual de conferir manualmente dados dispersos em várias fontes consome muito tempo da equipe.  
> 2. **Desalinhamento Regulatório:** A falta de centralização e padronização gera atrito e reprocessamento com áreas regulatórias.  
> 3. **Imprecisão na IA:** A ausência de um repositório centralizado de dados limpos afeta negativamente a qualidade dos resumos e *insights* gerados por ferramentas de Inteligência Artificial.  
> 4. **Inconsistência de Respostas:** Presença de dados duplicados vindo do mesmo respondente em uma mesma pesquisa.

> 

## **6\. Próximos Passos Sugeridos para Engenharia & Desenvolvimento**

> 1. **Modelagem do BD Relacional (MVP):**  
   * Criar o modelo relacional para rastrear o ciclo de vida da pesquisa.  
> 2. **Configuração do ClickHouse (DW):**  
   * Definir os *schemas* das tabelas analíticas otimizadas para leitura rápida e agregação.  
> 3. **Desenvolvimento do Pipeline de Dados (ETL/ELT):**  
   * Mapear a estrutura dos 4 CSVs fornecidos.  
   * Criar regras de deduplicação e validação contra o Excel (fonte da verdade).  
> 4. **Configuração de Segurança e RBAC:**  
   * Configurar perfis e políticas de acesso a dados no banco/DW e sincronizar com o Power BI.  
> 5. **Construção dos Dashboards Protótipo:**  
   * Desenvolver os protótipos das duas visões (Sindusfarma e Resultados da Pesquisa) utilizando massa de dados anonimizada.