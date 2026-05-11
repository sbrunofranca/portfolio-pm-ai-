# =========================================================
# IMPORTS BASE
# =========================================================

import streamlit as st
import sys
import os

# =========================================================
# GARANTE QUE A RAIZ DO PROJETO ESTÁ NO PYTHONPATH
# Isso resolve: ModuleNotFoundError: No module named 'app'
# =========================================================

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Importa seu backend RAG
from app.rag_pipeline import generate_response


# =========================================================
# CONFIGURAÇÃO DA PÁGINA (DEVE SER A PRIMEIRA CHAMADA ST)
# =========================================================

st.set_page_config(
    page_title="AI Copilot de Atendimento",
    layout="wide"
)


# =========================================================
# UI PRINCIPAL
# =========================================================

st.title("🤖 AI Copilot de Atendimento")
st.caption("RAG + Groq + Base de conhecimento interna")


# =========================================================
# ESTADO DA SESSÃO (MEMÓRIA DO CHAT)
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# RENDERIZA HISTÓRICO DO CHAT
# =========================================================

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# =========================================================
# INPUT DO USUÁRIO
# =========================================================

user_input = st.chat_input("Digite sua pergunta...")


if user_input:

    # -----------------------------------------
    # 1. salva mensagem do usuário
    # -----------------------------------------
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)


    # -----------------------------------------
    # 2. chama seu RAG pipeline
    # -----------------------------------------
    response = generate_response(user_input)


    # -----------------------------------------
    # 3. salva resposta do assistente
    # -----------------------------------------
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)