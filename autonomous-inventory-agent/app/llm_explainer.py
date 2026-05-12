# =========================================================
# IMPORTS
# =========================================================

import os

from dotenv import load_dotenv

from groq import Groq


# =========================================================
# LOAD ENV
# =========================================================

load_dotenv()


# =========================================================
# CLIENT
# =========================================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# =========================================================
# MAIN FUNCTION
# =========================================================

def explain_decision(decision, latest_stock):

    """
    Gera explicação da decisão do sistema.
    """

    # =====================================================
    # PROMPT
    # =====================================================

    prompt = f"""
    Você é um analista especialista em supply chain.

    Analise a seguinte decisão:

    Estoque atual:
    {latest_stock}

    Decisão:
    {decision}

    Explique:

    1. O risco operacional
    2. O motivo da reposição
    3. Impacto no negócio
    4. Recomendação

    Responda de forma objetiva.
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
    # RETURN
    # =====================================================

    return response.choices[0].message.content