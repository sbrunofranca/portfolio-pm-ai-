# =========================================================
# DEMAND AGENT
# =========================================================

def analyze_demand(df):

    """
    Analisa tendência de demanda.
    """

    # =====================================================
    # MÉDIA RECENTE
    # =====================================================

    recent_avg = round(
        df["demand"].tail(7).mean(),
        2
    )

    # =====================================================
    # MÉDIA HISTÓRICA
    # =====================================================

    historical_avg = round(
        df["demand"].mean(),
        2
    )

    # =====================================================
    # TENDÊNCIA
    # =====================================================

    trend = "stable"

    if recent_avg > historical_avg:

        trend = "up"

    elif recent_avg < historical_avg:

        trend = "down"

    # =====================================================
    # RISCO
    # =====================================================

    risk_level = "low"

    if trend == "up":

        risk_level = "medium"

    # =====================================================
    # RETURN
    # =====================================================

    return {

        "recent_average": recent_avg,

        "historical_average": historical_avg,

        "trend": trend,

        "risk_level": risk_level
    }