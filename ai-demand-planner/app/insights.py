# =========================================================
# INSIGHTS ENGINE - AI DEMAND PLANNER
# =========================================================
# Gera insights acionáveis a partir de previsões
# =========================================================


def generate_insights(history, forecast):
    """
    Gera insights de negócio baseados em histórico e previsão.

    Args:
        history (list): série histórica de demanda
        forecast (list): série prevista pelo modelo

    Returns:
        list[str]: lista de insights acionáveis
    """

    insights = []

    # =====================================================
    # VALIDAÇÃO BÁSICA
    # =====================================================
    if not history or not forecast:
        return ["⚠️ Dados insuficientes para gerar insights."]

    # =====================================================
    # 1. TENDÊNCIA GERAL
    # =====================================================
    if forecast[-1] > forecast[0]:
        insights.append("📈 Tendência de crescimento na demanda prevista.")
    else:
        insights.append("📉 Tendência de queda na demanda prevista.")

    # =====================================================
    # 2. VARIABILIDADE
    # =====================================================
    avg_forecast = sum(forecast) / len(forecast)

    if max(forecast) > avg_forecast * 1.2:
        insights.append("⚠️ Pico relevante de demanda identificado.")

    if min(forecast) < avg_forecast * 0.8:
        insights.append("🚨 Possível risco de excesso de estoque ou baixa demanda.")

    # =====================================================
    # 3. COMPARAÇÃO HISTÓRICO VS FUTURO
    # =====================================================
    avg_history = sum(history) / len(history)

    if avg_forecast > avg_history:
        insights.append("📊 A demanda futura está acima da média histórica.")
    else:
        insights.append("📊 A demanda futura está abaixo da média histórica.")

    # =====================================================
    # 4. RECOMENDAÇÃO DE NEGÓCIO
    # =====================================================
    if forecast[-1] > forecast[0]:
        insights.append("🎯 Recomendação: reforçar estoque para evitar ruptura.")
    else:
        insights.append("🎯 Recomendação: reduzir compras e exposição de estoque.")

    return insights