# =========================================================
# IMPORTS
# =========================================================

from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma


# =========================================================
# EMBEDDINGS
# =========================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================================================
# VECTOR DATABASE
# =========================================================

db = Chroma(
    persist_directory="rag_db",
    embedding_function=embeddings
)


# =========================================================
# INGEST DOCUMENTS
# =========================================================

def ingest_documents():

    """
    Processa documentos corporativos.
    """

    # =====================================================
    # LOAD FILE
    # =====================================================

    loader = TextLoader(
        "knowledge_base/policies.txt"
    )

    documents = loader.load()

    # =====================================================
    # TEXT SPLITTING
    # =====================================================

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        documents
    )

    # =====================================================
    # SAVE VECTOR DB
    # =====================================================

    db.add_documents(chunks)

    db.persist()

    return len(chunks)


# =========================================================
# RETRIEVAL
# =========================================================

def retrieve_context(question):

    """
    Busca contexto relevante.
    """

    results = db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(

        [
            doc.page_content
            for doc in results
        ]
    )

    return context