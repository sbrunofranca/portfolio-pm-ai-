# =========================================================
# LLM INSIGHTS ENGINE - GROQ
# =========================================================
# Transforma forecast em explicação de negócio
# =========================================================

import os
from dotenv import load_dotenv
from groq import Groq

# Carrega variáveis de ambiente
load_dotenv()

# Inicializa cliente Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_llm_insights(history, forecast):
    """
    Gera explicação inteligente usando LLM (Groq)
    """

    # =====================================================
    # PREPARA CONTEXTO
    # =====================================================
    context = f"""
    Você é um analista sênior de supply chain.

    Histórico de demanda:
    {history}

    Previsão futura:
    {forecast}

    Tarefa:
    Explique de forma simples:
    1. O que está acontecendo com a demanda
    2. Possíveis causas
    3. O que o time de negócios deve fazer

    Responda em português, de forma objetiva.
    """

    # =====================================================
    # CHAMADA AO MODELO
    # =====================================================
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Você é um especialista em supply chain e analytics."},
            {"role": "user", "content": context}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content