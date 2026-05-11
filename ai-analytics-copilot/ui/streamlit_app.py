import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.sql_generator import generate_sql
from app.database import run_query


st.set_page_config(
    page_title="AI Analytics Copilot",
    layout="wide"
)

st.title("📊 AI Analytics Copilot")
st.caption("Pergunte seus dados em linguagem natural")

question = st.chat_input("Pergunte algo sobre os dados...")

if question:

    st.chat_message("user").write(question)

    # schema fake MVP
    schema = """
    table: sales (date, revenue)
    table: support (date, tickets_resolved)
    """

    sql = generate_sql(question, schema)

    st.chat_message("assistant").write("📌 SQL gerado:")
    st.code(sql)

    try:
        result = run_query(sql)
        st.chat_message("assistant").write("📊 Resultado:")
        st.dataframe(result)
    except Exception as e:
        st.error(str(e))