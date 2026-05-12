# 🚀 Autonomous Inventory Agent

AI-powered autonomous inventory management system with:
- Multi-Agent AI workflows
- Demand intelligence
- Inventory optimization
- Enterprise RAG
- Conversational supply chain assistant
- Historical memory and decision tracking

---

# 📌 Problema Real Sendo Resolvido

Empresas frequentemente enfrentam problemas como:

- ruptura de estoque
- excesso de inventário
- decisões manuais lentas
- dificuldade de interpretar demanda
- falta de visibilidade operacional
- dependência de dashboards complexos

Além disso, planners e analistas precisam:
- consultar múltiplos sistemas
- interpretar indicadores manualmente
- tomar decisões sob pressão operacional

O objetivo deste projeto é criar um sistema inteligente capaz de:

✅ monitorar estoque
✅ analisar demanda
✅ recomendar reposição
✅ justificar decisões
✅ responder perguntas em linguagem natural
✅ consultar políticas corporativas

---

# 🏢 Contexto de Negócio

## Usuários

- Supply Chain Analysts
- Inventory Planners
- Procurement Teams
- Logistics Managers
- Operations Teams

## Cenário Operacional

Em ambientes de supply chain:

- decisões precisam acontecer rapidamente
- estoque parado gera custo
- ruptura gera perda de receita
- demanda muda constantemente
- regras operacionais são complexas

O sistema atua como um:
AI Copilot para operações de estoque.

---

# 🧠 Hipótese

Se criarmos um sistema com:

- agentes especializados
- memória operacional
- RAG corporativo
- explicabilidade
- interface conversacional

Então usuários não técnicos poderão:
- tomar decisões mais rápidas
- reduzir risco operacional
- acessar conhecimento corporativo
- operar supply chain com apoio de IA

---

# 💡 Solução

O projeto implementa um:
Autonomous Inventory AI System

capaz de:

✅ analisar demanda
✅ simular decisões de estoque
✅ calcular custos
✅ definir logística
✅ consultar políticas corporativas
✅ responder perguntas em linguagem natural

---

# 🎯 Caso de Uso

Exemplos de perguntas:

- Qual a política de estoque mínimo?
- Quando devemos usar priority shipping?
- Existe risco operacional?
- O custo da operação aumentou?
- Qual fornecedor possui maior lead time?

---

# 🏗️ Arquitetura da Solução

User
↓
Streamlit UI
↓
Multi-Agent Workflow
↓
Demand Agent
Inventory Agent
Cost Agent
Logistics Agent
↓
Memory Layer
↓
RAG Knowledge Base
↓
LLM Response (Groq + Llama)

---

# 🤖 Agentes Implementados

## 📊 Demand Agent

Responsável por:
- analisar tendência de demanda
- detectar crescimento/redução
- avaliar risco operacional

## 📦 Inventory Agent

Responsável por:
- decidir reposição
- calcular necessidade de estoque
- evitar ruptura

## 💰 Cost Agent

Responsável por:
- estimar custo operacional
- avaliar impacto financeiro
- otimizar compras

## 🚚 Logistics Agent

Responsável por:
- selecionar estratégia logística
- avaliar lead time
- definir shipping priority

---

# 🧠 Memory Layer

O sistema mantém:
- histórico de decisões
- contexto operacional
- evolução temporal

Isso permite:
- reasoning histórico
- comparação entre execuções
- observabilidade operacional

---

# 📚 RAG — Enterprise Knowledge Base

O sistema consulta documentos corporativos usando:
- embeddings
- vector search
- retrieval augmentation

Exemplos:
- políticas de estoque
- regras logísticas
- processos operacionais
- lead times
- regras de reposição

---

# ⚙️ Funcionalidades

## ✅ Multi-Agent Workflow

Agentes colaboram em sequência:
- compartilhando contexto
- executando decisões
- consolidando estado operacional

## ✅ Conversational AI

Usuários podem:
- fazer perguntas em linguagem natural
- receber explicações executivas
- consultar políticas corporativas

## ✅ Historical Memory

O sistema:
- salva decisões passadas
- rastreia histórico operacional
- fornece contexto temporal

## ✅ RAG Grounding

As respostas:
- utilizam documentos internos
- reduzem hallucination
- melhoram precisão operacional

---

# 🛠️ Tecnologias Utilizadas

## AI / LLM

- Groq
- Llama 3
- Prompt Engineering

## RAG

- LangChain
- ChromaDB
- Sentence Transformers

## Data / Supply Chain

- pandas
- numpy

## Frontend

- Streamlit

## Backend

- Python

---

# 📊 Métricas de Sucesso

O sistema busca reduzir:

- ruptura de estoque
- excesso de inventário
- tempo de tomada de decisão
- dependência operacional manual

---

# 📈 Impacto Esperado

## Operacional

✅ decisões mais rápidas
✅ redução de risco
✅ maior visibilidade

## Negócio

✅ menor custo operacional
✅ maior eficiência logística
✅ aumento de disponibilidade de produtos

## Usuário

✅ acesso simplificado a informações
✅ linguagem natural
✅ menos dependência de dashboards

---

# ▶️ Como Executar

1. Clonar projeto

git clone <repo_url>

2. Criar ambiente virtual

python -m venv venv

3. Ativar ambiente

Mac/Linux:
source venv/bin/activate

4. Instalar dependências

pip install -r requirements.txt

5. Configurar variáveis

Criar `.env`

GROQ_API_KEY=your_api_key

6. Processar documentos RAG

python ingest.py

7. Executar aplicação

streamlit run ui/streamlit_app.py

---

# ⚖️ Trade-offs

## OR-Tools removido temporariamente

Inicialmente o projeto utilizava:
- Google OR-Tools

Porém:
- conflitos protobuf no macOS Apple Silicon
- problemas binários no ambiente local

Foi adotada uma:
optimization engine simplificada

Vantagens:
- maior estabilidade
- explicabilidade
- simplicidade do MVP

## Knowledge Base simplificada

Atualmente:
- documentos em `.txt`

Futuramente:
- PDFs
- ERPs
- bancos corporativos
- SharePoint
- SAP

## Forecasting ainda simulado

A demanda ainda é:
- parcialmente simulada

Próxima evolução:
- modelos reais de ML
- forecasting temporal

---

# 🚀 Próximos Passos

## ETAPA 21 — MLOps

Adicionar:
- MLflow
- monitoramento
- tracking de decisões
- observabilidade

## ETAPA 22 — Deploy Cloud

Deploy com:
- Docker
- FastAPI
- AWS/GCP

---

# 🧠 Resultado Final Esperado

Um sistema estilo:

"AI Supply Chain Copilot que opera estoque, consulta conhecimento corporativo e explica decisões usando agentes inteligentes."

---

# 👨‍💻 Autor

Bruno — AI Product & Operations Portfolio