# =========================================================
# IMPORTS
# =========================================================

import pandas as pd


# =========================================================
# AUTONOMOUS REPLENISHMENT AGENT
# =========================================================

def autonomous_replenishment_agent(state):

    """
    Agente autônomo de reposição.
    """

    # =====================================================
    # LOAD SUPPLIERS
    # =====================================================

    suppliers = pd.read_csv(
        "data/suppliers.csv"
    )

    # =====================================================
    # LOAD CONTEXT
    # =====================================================

    forecast = state["forecast"]

    simulation = state["simulation"]

    risk = state["risk_analysis"]

    # =====================================================
    # BUSINESS CONTEXT
    # =====================================================

    predicted_demand = forecast[
        "predicted_demand"
    ]

    final_stock = simulation[
        "final_stock"
    ]

    risk_level = risk[
        "risk_level"
    ]

    # =====================================================
    # REORDER LOGIC
    # =====================================================

    reorder_needed = (

        final_stock <
        predicted_demand * 2
    )

    # =====================================================
    # NO REPLENISHMENT
    # =====================================================

    if not reorder_needed:

        return {

            "decision": "NO_REPLENISHMENT",

            "reason": (
                "Inventory level is healthy."
            )
        }

    # =====================================================
    # OPTIMIZATION SCORE
    # =====================================================

    suppliers["score"] = (

        suppliers["reliability"] * 100

        -

        suppliers["cost_per_unit"]

        -

        suppliers["lead_time"] * 2
    )

    # =====================================================
    # BEST SUPPLIER
    # =====================================================

    best_supplier = suppliers.sort_values(

        by="score",

        ascending=False

    ).iloc[0]

    # =====================================================
    # REORDER QUANTITY
    # =====================================================

    reorder_quantity = int(

        predicted_demand * 3
    )

    # =====================================================
    # ESTIMATED COST
    # =====================================================

    total_cost = (

        reorder_quantity *

        best_supplier["cost_per_unit"]
    )

    # =====================================================
    # PRIORITY
    # =====================================================

    if risk_level == "HIGH RISK":

        priority = "URGENT"

    elif risk_level == "MEDIUM RISK":

        priority = "HIGH"

    else:

        priority = "NORMAL"

    # =====================================================
    # FINAL DECISION
    # =====================================================

    return {

        "decision": "REPLENISH",

        "supplier": best_supplier[
            "supplier"
        ],

        "quantity": reorder_quantity,

        "estimated_cost": round(
            total_cost,
            2
        ),

        "lead_time": int(
            best_supplier["lead_time"]
        ),

        "priority": priority,

        "reason": (
            f"Predicted demand is "
            f"{predicted_demand} units "
            f"and current stock is "
            f"{final_stock}."
        )
    }