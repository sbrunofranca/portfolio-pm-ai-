# 🤖 AI Copilot de Suporte ao Cliente (RAG + Groq + Streamlit)

---

## 📌 Nome do Projeto
AI Copilot de Suporte ao Cliente

---

## 🚨 Problema Real Sendo Resolvido

Equipes de suporte ao cliente enfrentam:

- Alto volume de perguntas repetitivas
- Custo elevado de atendimento humano
- Tempo de resposta lento
- Inconsistência nas respostas entre atendentes
- Escalabilidade limitada do time de suporte

---

## 👤 Contexto (Usuário e Negócio)

### Usuário final:
Clientes que precisam de suporte rápido e consistente.

### Usuário interno:
Agentes de suporte que lidam com grande volume de tickets.

### Contexto de negócio:
Empresas SaaS e operações de atendimento que precisam reduzir custo operacional e escalar suporte sem aumentar proporcionalmente o time humano.

---

## 🧪 Hipótese

Se utilizarmos um sistema baseado em **RAG (Retrieval-Augmented Generation)** conectado a uma base de conhecimento interna, podemos:

- Reduzir significativamente o volume de tickets humanos
- Aumentar a velocidade de resposta
- Melhorar consistência das respostas
- Automatizar parte do atendimento de primeiro nível

---

## 💡 Solução (Produto + Técnica)

Um **AI Copilot de Suporte ao Cliente** que responde dúvidas automaticamente com base em documentos internos da empresa.

### Técnica:
- RAG para recuperação de contexto relevante
- Embeddings semânticos
- LLM para geração de respostas
- Pipeline modular em Python

---

## 🎯 Caso de Uso

### Suporte ao cliente antes de escalar para atendimento humano

O sistema atua como primeira camada de atendimento:

- Responde perguntas frequentes automaticamente
- Consulta base de conhecimento interna (RAG)
- Escala apenas casos complexos para humano
- Reduz carga do time de suporte

---

## 🧱 Arquitetura da Solução

### 🔹 Pipeline de IA
1. Usuário envia pergunta
2. Sistema realiza embedding da query
3. Busca semântica na base (ChromaDB)
4. Recupera top-k documentos relevantes
5. Monta contexto + prompt
6. LLM gera resposta (Groq)

### 🔹 Componentes
- `ingest.py` → ingestão da base de conhecimento
- `rag_pipeline.py` → lógica principal de recuperação + geração
- `streamlit_app.py` → interface do usuário

---

## ⚙️ Funcionalidades

- Chat inteligente estilo assistente
- Respostas baseadas em base de conhecimento
- Memória de sessão no Streamlit
- Recuperação semântica (RAG)
- Interface simples e funcional

---

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- LangChain
- ChromaDB (vector database)
- HuggingFace Embeddings
- Groq API (LLaMA 3.1)

---

## 📊 Métricas de Sucesso

- Taxa de resolução automática de tickets
- Redução de tickets enviados para humanos
- Tempo médio de resposta (latência)
- Precisão das respostas baseadas na base de conhecimento
- Satisfação do usuário (CSAT simulado)

---

## 📈 Impacto Esperado

- Redução de custo operacional de suporte
- Escalabilidade sem aumento proporcional de equipe
- Melhoria na experiência do cliente
- Padronização das respostas
- Maior eficiência do time humano (foco em casos complexos)

---

## ⚠️ Trade-offs (ESSENCIAL)

- Dependência da qualidade da base de conhecimento
- Possibilidade de respostas incorretas sem contexto suficiente
- Latência maior devido ao uso de LLM + retrieval
- Custo de inferência com API de LLM
- Necessidade de manutenção contínua da base de dados

---

## 🚀 Próximos Passos

- Exposição de fontes do RAG na interface (explicabilidade)
- Sistema de escalonamento para atendimento humano
- Implementação de multi-agentes (triagem + resposta + validação)
- Observabilidade (logs, métricas e qualidade das respostas)
- Integração com canais reais (WhatsApp, Webchat, APIs)

---

## ▶️ Como Executar

### 1. Instalar dependências
-pip install -r requirements.txt

### 2. Inserir base de conhecimento
-python app/ingest.py

### 3. Rodar aplicação
-streamlit run ui/streamlit_app.py
