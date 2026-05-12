# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.pipeline import run_pipeline

from app.chat_agent import ask_agents


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Autonomous Inventory Agent",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("📦 Autonomous Inventory Agent")


# =========================================================
# EXECUTA PIPELINE
# =========================================================

result = run_pipeline()


# =========================================================
# INVENTORY GRAPH
# =========================================================

st.subheader("📊 Inventory Simulation")

st.line_chart(
    result["data"]["inventory"]
)


# =========================================================
# AGENT OUTPUT
# =========================================================

st.subheader("🤖 Multi-Agent Decisions")

# =========================================================
# WORKFLOW VISUAL
# =========================================================

st.subheader("🔄 AI Workflow")

st.markdown("""

Demand Agent
⬇️

Inventory Agent
⬇️

Cost Agent
⬇️

Logistics Agent
⬇️

LLM Business Explanation

""")

st.json(result["agents"])


# =========================================================
# LLM EXPLANATION
# =========================================================

st.subheader("🧠 AI Explanation")

st.write(result["explanation"])


# =========================================================
# CHAT SECTION
# =========================================================

st.subheader("💬 Chat With Agents")

question = st.text_input(
    "Pergunte sobre estoque, custo, risco ou logística:"
)


if question:

    answer = ask_agents(
        question,
        result["agents"]
    )

    st.write(answer)

# =========================================================
# HISTORICAL MEMORY
# =========================================================

st.subheader("🧠 Historical Decisions")

st.write(
    result["previous_decision"]
)

st.subheader("📚 Enterprise Knowledge Base")

st.info("""

Knowledge Sources:
- Supply chain policies
- Logistics rules
- Inventory policies
- Operational procedures

""")