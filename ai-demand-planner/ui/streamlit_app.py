import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.pipeline import run_pipeline

st.set_page_config(page_title="AI Demand Planner")

st.title("📊 AI Demand Planner MVP")

if st.button("Rodar previsão"):
    
    result = run_pipeline()

    st.line_chart(result["history"])

    st.subheader("📈 Previsão")
    st.line_chart(result["forecast"])

    st.subheader("⚠️ Insights de Negócio")

    for insight in result["insights"]:
        st.write(insight)
    
    st.subheader("🧠 Explicação da IA (LLM)")
    st.write(result["llm_explanation"])