# =========================================================
# IMPORTS
# =========================================================

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma


# =========================================================
# LOAD ENV
# =========================================================

load_dotenv()


# =========================================================
# EMBEDDINGS MODEL
# =========================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================================================
# VECTOR DATABASE
# =========================================================

db = Chroma(
    persist_directory="chromadb",
    embedding_function=embeddings
)


# =========================================================
# LLM CONFIG
# =========================================================

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)


# =========================================================
# LOAD SYSTEM PROMPT
# =========================================================

with open("prompts/support_prompt.txt", "r") as file:
    system_prompt = file.read()


# =========================================================
# MAIN RAG FUNCTION
# =========================================================

def generate_response(question: str):

    """
    Pipeline principal RAG.
    """

    # =====================================================
    # RETRIEVAL
    # =====================================================

    results = db.similarity_search(
        question,
        k=3
    )

    # =====================================================
    # BUILD CONTEXT
    # =====================================================

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    # =====================================================
    # FINAL PROMPT
    # =====================================================

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

    Gere uma sugestão de resposta para o agente.

    RESPOSTA:
    """

    # =====================================================
    # GENERATE RESPONSE
    # =====================================================

    response = llm.invoke(prompt)

    return response.content