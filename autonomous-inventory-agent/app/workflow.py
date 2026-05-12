# =========================================================
# IMPORTS
# =========================================================

from app.agents.demand_agent import analyze_demand

from app.agents.inventory_agent import inventory_decision

from app.agents.cost_agent import analyze_cost

from app.agents.logistics_agent import logistics_decision


# =========================================================
# WORKFLOW ENGINE
# =========================================================

def run_workflow(df):

    """
    Executa workflow multi-agent.
    """

    # =====================================================
    # STEP 1 — DEMAND AGENT
    # =====================================================

    demand_output = analyze_demand(df)

    # =====================================================
    # STEP 2 — INVENTORY AGENT
    # =====================================================

    inventory_output = inventory_decision(df)

    # =====================================================
    # STEP 3 — COST AGENT
    # =====================================================

    cost_output = analyze_cost(
        inventory_output["quantity"]
    )

    # =====================================================
    # STEP 4 — LOGISTICS AGENT
    # =====================================================

    logistics_output = logistics_decision(
        inventory_output["quantity"]
    )

    # =====================================================
    # STEP 5 — CONSOLIDATED STATE
    # =====================================================

    state = {

        "demand": demand_output,

        "inventory": inventory_output,

        "cost": cost_output,

        "logistics": logistics_output
    }

    # =====================================================
    # RETURN
    # =====================================================

    return state