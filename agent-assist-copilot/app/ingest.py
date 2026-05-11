# =========================================================
# IMPORTS
# =========================================================

# Carrega variáveis ambiente
from dotenv import load_dotenv

# Carrega documentos da KB
from langchain_community.document_loaders import DirectoryLoader

# Divide documentos em chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Modelo embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# Banco vetorial
from langchain_community.vectorstores import Chroma


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()


# =========================================================
# LOAD DOCUMENTS
# =========================================================

# Carrega todos os arquivos markdown
loader = DirectoryLoader(
    "data/knowledge_base",
    glob="**/*.md"
)

documents = loader.load()

print("\n========================")
print("DOCUMENTOS CARREGADOS")
print("========================")
print(f"Quantidade: {len(documents)}")


# =========================================================
# SPLIT DOCUMENTS
# =========================================================

# Divide documentos em chunks menores
#
# Isso melhora:
# - retrieval
# - precisão semântica
# - contexto
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

texts = text_splitter.split_documents(documents)

print("\n========================")
print("CHUNKS CRIADOS")
print("========================")
print(f"Quantidade: {len(texts)}")


# =========================================================
# EMBEDDINGS MODEL
# =========================================================

# Modelo embeddings HuggingFace
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("\nModelo embeddings carregado.")


# =========================================================
# CREATE VECTOR DATABASE
# =========================================================

# Cria ChromaDB
#
# persist_directory:
# salva vetores localmente
db = Chroma.from_documents(
    texts,
    embeddings,
    persist_directory="chromadb"
)

print("\n========================")
print("VECTOR DATABASE CRIADO")
print("========================")
print("Embeddings armazenados com sucesso!")