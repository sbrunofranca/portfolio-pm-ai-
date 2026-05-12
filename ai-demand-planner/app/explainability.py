# =========================================================
# EXPLAINABILITY MODULE
# =========================================================
# Responsável por gerar explicações simples
# baseadas em padrões estatísticos das previsões
# =========================================================

import pandas as pd


def explain_forecast(predictions):
    """
    Gera explicações simples baseadas nas previsões do modelo.

    Args:
        predictions (list or pd.DataFrame):
            Lista ou dataframe com valores previstos de demanda.

    Returns:
        str: explicação em linguagem natural
    """

    # =====================================================
    # CONVERTE PARA LISTA SE NECESSÁRIO
    # =====================================================
    if isinstance(predictions, pd.DataFrame):
        values = predictions.iloc[:, 0].tolist()
    else:
        values = list(predictions)

    # =====================================================
    # CÁLCULOS BÁSICOS
    # =====================================================
    avg_demand = sum(values) / len(values)
    max_demand = max(values)
    min_demand = min(values)

    trend = "estável"

    # Detecta tendência simples
    if values[-1] > values[0]:
        trend = "crescimento"
    elif values[-1] < values[0]:
        trend = "queda"

    # =====================================================
    # GERA EXPLICAÇÃO
    # =====================================================
    explanation = f"""
📊 ANÁLISE DE DEMANDA

- Demanda média prevista: {avg_demand:.2f}
- Pico de demanda: {max_demand:.2f}
- Menor demanda: {min_demand:.2f}

📈 Tendência identificada: {trend}

🧠 INTERPRETAÇÃO:
A previsão indica um cenário de {trend} na demanda.

💡 POSSÍVEIS CAUSAS:
- Variação natural de consumo
- Sazonalidade (se aplicável)
- Oscilações de mercado

⚠️ OBS:
Esta é uma explicação baseada em padrões estatísticos simples.
Para explicações mais avançadas, utilize o módulo LLM.
"""

    return explanation