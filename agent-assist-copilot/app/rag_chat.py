# =========================================================
# IMPORTS
# =========================================================

# Carrega variáveis do arquivo .env
from dotenv import load_dotenv

# Cliente LLM da Groq
from langchain_groq import ChatGroq

# Modelo de embeddings do HuggingFace
from langchain_community.embeddings import HuggingFaceEmbeddings

# Banco vetorial ChromaDB
from langchain_community.vectorstores import Chroma


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

# Carrega automaticamente o arquivo .env
# Exemplo:
# GROQ_API_KEY=xxxx
load_dotenv()


# =========================================================
# EMBEDDINGS MODEL
# =========================================================

# Modelo responsável por transformar texto em vetores
# Vetores são representações numéricas semânticas
#
# Isso permite:
# - busca semântica
# - similarity search
# - retrieval contextual
#
# Modelo escolhido:
# all-MiniLM-L6-v2
#
# Muito usado em projetos RAG:
# - leve
# - rápido
# - eficiente
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================================================
# LOAD VECTOR DATABASE
# =========================================================

# Carrega o banco vetorial persistido localmente
#
# O ChromaDB contém:
# - embeddings dos documentos
# - chunks da knowledge base
#
# persist_directory:
# pasta onde os vetores foram salvos
db = Chroma(
    persist_directory="chromadb",
    embedding_function=embeddings
)


# =========================================================
# LLM CONFIGURATION
# =========================================================

# Inicializa modelo da Groq
#
# llama3-8b-8192:
# - rápido
# - ótimo custo-benefício
# - excelente para copilots
#
# A Groq fornece inferência extremamente rápida
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)


# =========================================================
# USER QUESTION
# =========================================================

# Simula mensagem recebida do cliente
#
# Em produção:
# isso viria:
# - WhatsApp
# - Zendesk
# - API
# - Webchat
question = """
Meu pedido está atrasado há mais de 10 dias.
Quero cancelar e receber reembolso imediatamente.
"""


# =========================================================
# RETRIEVAL
# =========================================================

# Realiza busca semântica no banco vetorial
#
# similarity_search:
# procura documentos semanticamente parecidos
#
# k=3:
# retorna os 3 chunks mais relevantes
results = db.similarity_search(
    question,
    k=3
)


# =========================================================
# BUILD CONTEXT
# =========================================================

# Junta todos os chunks encontrados
#
# page_content:
# conteúdo textual do documento
#
# O contexto será enviado para o LLM
context = "\n\n".join(
    [doc.page_content for doc in results]
)


# =========================================================
# LOAD SYSTEM PROMPT
# =========================================================

# Carrega prompt externo
#
# Boa prática:
# separar:
# - prompts
# - lógica
# - orchestration
#
# Facilita:
# - manutenção
# - versionamento
# - prompt engineering
with open("prompts/support_prompt.txt", "r") as file:
    system_prompt = file.read()


# =========================================================
# FINAL PROMPT
# =========================================================

# Monta prompt completo enviado ao modelo
#
# Estrutura:
# - instruções
# - contexto
# - mensagem cliente
# - tarefa
#
# Isso reduz hallucinations
# e melhora qualidade da resposta
prompt = f"""
{system_prompt}

=====================
CONTEXTO
=====================

{context}

=====================
MENSAGEM DO CLIENTE
=====================

{question}

=====================
TAREFA
=====================

Gere uma sugestão de resposta para o agente de atendimento.

A resposta deve:
- ser empática
- ser objetiva
- seguir as políticas da empresa
- orientar claramente o cliente
- soar natural e humana

RESPOSTA SUGERIDA:
"""


# =========================================================
# GENERATE RESPONSE
# =========================================================

# Envia prompt para o modelo
response = llm.invoke(prompt)


# =========================================================
# OUTPUT
# =========================================================

# Exibe resposta final
print("\n============================")
print("RESPOSTA GERADA PELA IA")
print("============================\n")

print(response.content)