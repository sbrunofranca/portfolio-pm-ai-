# =========================================================
# IMPORTS
# =========================================================

import os

from dotenv import load_dotenv

from groq import Groq

# =========================================================
# IMPORTS INTERNOS
# =========================================================

from app.memory import load_memory

from app.rag import retrieve_context


# =========================================================
# LOAD ENV VARIABLES
# =========================================================

# Carrega variáveis do .env

load_dotenv()


# =========================================================
# GROQ CLIENT
# =========================================================

# Inicializa cliente Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# =========================================================
# LOAD SYSTEM PROMPT
# =========================================================

# Carrega prompt principal do sistema

with open(
    "prompts/chat_prompt.txt",
    "r"
) as file:

    SYSTEM_PROMPT = file.read()


# =========================================================
# CHAT FUNCTION
# =========================================================

def ask_agents(
    question,
    agents_output
):

    """
    Responde perguntas utilizando:

    - outputs dos agentes
    - memória histórica
    - conhecimento corporativo (RAG)
    - contexto operacional
    """

    # =====================================================
    # MEMORY CONTEXT
    # =====================================================

    # Carrega histórico de decisões

    history = load_memory()

    # Mantém apenas últimas 5 decisões

    recent_history = history[-5:]

    # =====================================================
    # RAG RETRIEVAL
    # =====================================================

    # Busca contexto relevante
    # na base de conhecimento

    rag_context = retrieve_context(
        question
    )

    # =====================================================
    # AGENT CONTEXT
    # =====================================================

    # Consolida outputs dos agentes

    context = f"""

    DEMAND AGENT:
    {agents_output["demand"]}

    INVENTORY AGENT:
    {agents_output["inventory"]}

    COST AGENT:
    {agents_output["cost"]}

    LOGISTICS AGENT:
    {agents_output["logistics"]}

    """

    # =====================================================
    # FINAL PROMPT
    # =====================================================

    prompt = f"""

    {SYSTEM_PROMPT}

    ===================================
    CONTEXTO OPERACIONAL
    ===================================

    {context}

    ===================================
    HISTÓRICO RECENTE
    ===================================

    {recent_history}

    ===================================
    CONHECIMENTO CORPORATIVO
    ===================================

    {rag_context}

    ===================================
    PERGUNTA
    ===================================

    {question}

    ===================================
    RESPOSTA EXECUTIVA
    ===================================

    """

    # =====================================================
    # LLM CALL
    # =====================================================

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # =====================================================
    # FINAL RESPONSE
    # =====================================================

    return response.choices[0].message.content