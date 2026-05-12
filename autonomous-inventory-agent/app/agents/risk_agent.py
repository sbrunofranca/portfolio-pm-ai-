# =========================================================
# RISK AGENT
# =========================================================

def risk_agent(state):

    """
    Analisa risco operacional.
    """

    simulation = state["simulation"]

    stockouts = simulation["stockouts"]

    final_stock = simulation["final_stock"]

    # =====================================================
    # RISK ANALYSIS
    # =====================================================

    if stockouts > 3:

        risk = "HIGH RISK"

    elif stockouts > 0:

        risk = "MEDIUM RISK"

    else:

        risk = "LOW RISK"

    return {

        "risk_level": risk,

        "stockouts": stockouts,

        "final_stock": final_stock
    }