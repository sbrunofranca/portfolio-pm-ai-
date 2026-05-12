# =========================================================
# IMPORTS
# =========================================================

from app.agents.demand_agent import analyze_demand

from app.agents.inventory_agent import inventory_decision

from app.agents.cost_agent import analyze_cost

from app.agents.logistics_agent import logistics_decision

from app.agents.risk_agent import risk_agent

from app.agents.autonomous_replenishment_agent import (
    autonomous_replenishment_agent
)

from app.forecast_engine import predict_next_demand

from app.supply_chain_simulator import run_simulation


# =========================================================
# WORKFLOW ENGINE
# =========================================================

def run_workflow(df):

    """
    Executa workflow multi-agent.
    """

    # =====================================================
    # FORECAST
    # =====================================================

    forecast = predict_next_demand()

    # =====================================================
    # SIMULATION
    # =====================================================

    simulation = run_simulation()

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
    # PARTIAL STATE
    # =====================================================

    state = {

        "forecast": forecast,

        "simulation": simulation,

        "demand": demand_output,

        "inventory": inventory_output,

        "cost": cost_output,

        "logistics": logistics_output
    }

    # =====================================================
    # STEP 5 — RISK AGENT
    # =====================================================

    risk_analysis = risk_agent(state)

    # =====================================================
    # ADD RISK TO STATE
    # =====================================================

    state["risk_analysis"] = risk_analysis

    # =====================================================
    # STEP 6 — AUTONOMOUS REPLENISHMENT
    # =====================================================

    replenishment_decision = (
        autonomous_replenishment_agent(state)
    )

    # =====================================================
    # ADD DECISION TO STATE
    # =====================================================

    state["replenishment_decision"] = (
        replenishment_decision
    )

    # =====================================================
    # RETURN
    # =====================================================

    return state