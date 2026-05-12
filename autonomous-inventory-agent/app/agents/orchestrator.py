# =========================================================
# IMPORTS
# =========================================================

from app.agents.demand_agent import analyze_demand

from app.agents.inventory_agent import inventory_decision

from app.agents.logistics_agent import analyze_logistics

from app.agents.cost_agent import analyze_cost


# =========================================================
# MAIN ORCHESTRATOR
# =========================================================

def run_agents(df):

    """
    Coordena execução dos agentes.
    """

    # =====================================================
    # DEMAND AGENT
    # =====================================================

    demand_analysis = analyze_demand(df)

    # =====================================================
    # INVENTORY AGENT
    # =====================================================

    inventory_analysis = inventory_decision(df)

    # =====================================================
    # LOGISTICS AGENT
    # =====================================================

    logistics_analysis = analyze_logistics()

    # =====================================================
    # COST AGENT
    # =====================================================

    cost_analysis = analyze_cost(
        inventory_analysis["quantity"]
    )

    # =====================================================
    # RETURN
    # =====================================================

    return {
        "demand": demand_analysis,
        "inventory": inventory_analysis,
        "logistics": logistics_analysis,
        "cost": cost_analysis
    }