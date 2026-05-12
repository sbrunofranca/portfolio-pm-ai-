# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import pandas as pd
import sys
import os

# =========================================================
# PATH CONFIG
# =========================================================

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# =========================================================
# IMPORT PIPELINE
# =========================================================

from app.pipeline import run_pipeline
from app.chat_agent import ask_agents

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="Autonomous Inventory Agent",

    page_icon="📦",

    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""

<style>

.main {
    background-color: #0E1117;
}

div[data-testid="metric-container"] {

    background-color: #1E1E1E;

    padding: 15px;

    border-radius: 10px;

    border: 1px solid #333333;
}

</style>

""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🏭 Supply Chain AI")

    st.markdown("---")

    st.markdown("""
    
    ### System Modules
    
    - Demand Forecasting
    - Inventory Simulation
    - Risk Analysis
    - Autonomous Procurement
    - Logistics Intelligence
    - Enterprise RAG
    - AI Agents
    
    """)

    st.markdown("---")

    st.info("""

    AI-powered autonomous
    inventory management system.

    """)

# =========================================================
# TITLE
# =========================================================

st.title("📦 Autonomous Inventory Agent")

st.caption(
    "AI-powered supply chain decision platform"
)

# =========================================================
# RUN PIPELINE
# =========================================================

result = run_pipeline()

# =========================================================
# LOAD DATA
# =========================================================

agents = result["agents"]

simulation = agents["simulation"]

risk = agents["risk_analysis"]

decision = agents["replenishment_decision"]

# =========================================================
# TOP KPIs
# =========================================================

st.markdown("## 📊 Operational KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(

        "Final Stock",

        simulation["final_stock"]
    )

with col2:

    st.metric(

        "Stockouts",

        simulation["stockouts"]
    )

with col3:

    st.metric(

        "Orders Created",

        len(simulation["orders"])
    )

with col4:

    st.metric(

        "Risk Level",

        risk["risk_level"]
    )

# =========================================================
# FORECAST + SIMULATION
# =========================================================

col1, col2 = st.columns(2)

# =========================================================
# FORECAST
# =========================================================

with col1:

    st.markdown("## 📈 Demand Forecast")

    st.info(

        f"Predicted Demand: "
        f"{agents['forecast']['predicted_demand']} units"
    )

# =========================================================
# SIMULATION
# =========================================================

with col2:

    st.markdown("## 🏭 Supply Chain Simulation")

    history_df = pd.DataFrame(

        simulation["stock_history"]
    )

    st.line_chart(

        history_df.set_index("day")["stock"]
    )

# =========================================================
# RISK + AUTONOMOUS DECISION
# =========================================================

col1, col2 = st.columns(2)

# =========================================================
# RISK ANALYSIS
# =========================================================

with col1:

    st.markdown("## ⚠️ Operational Risk")

    st.error(

        f"Risk Level: "
        f"{risk['risk_level']}"
    )

    st.write(risk)

# =========================================================
# AUTONOMOUS PROCUREMENT
# =========================================================

with col2:

    st.markdown("## 🤖 Autonomous Procurement")

    st.success(

        f"Decision: "
        f"{decision['decision']}"
    )

    st.write(decision)

# =========================================================
# MULTI AGENT WORKFLOW
# =========================================================

st.markdown("## 🔄 Multi-Agent Workflow")

workflow_col1, workflow_col2, workflow_col3 = st.columns(3)

with workflow_col1:

    st.info("📊 Demand Agent")

    st.info("📦 Inventory Agent")

with workflow_col2:

    st.info("💰 Cost Agent")

    st.info("🚚 Logistics Agent")

with workflow_col3:

    st.info("⚠️ Risk Agent")

    st.info("🤖 Procurement Agent")

# =========================================================
# AI EXPLANATION
# =========================================================

st.markdown("## 🧠 AI Business Explanation")

st.write(result["explanation"])

# =========================================================
# CHAT SECTION
# =========================================================

st.markdown("## 💬 Chat With AI Agents")

question = st.text_input(

    "Ask about inventory, risk, logistics or procurement:"
)

if question:

    answer = ask_agents(

        question,

        agents
    )

    st.success(answer)

# =========================================================
# EXPANDERS
# =========================================================

with st.expander("📚 Enterprise Knowledge Base"):

    st.markdown("""

    ### Knowledge Sources

    - Supply chain policies
    - Inventory procedures
    - Logistics rules
    - Procurement guidelines
    - Operational workflows

    """)

with st.expander("🧠 Historical Decisions"):

    st.write(
        result["previous_decision"]
    )

with st.expander("🔍 Full Agent State"):

    st.json(agents)