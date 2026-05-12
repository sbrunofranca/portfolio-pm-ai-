# =========================================================
# OPTIMIZATION ENGINE
# =========================================================

def optimize_inventory(
    current_stock,
    predicted_demand
):

    """
    Simula uma otimização de estoque.

    Objetivo:
    minimizar custo
    evitar ruptura
    evitar excesso de inventário
    """

    # =====================================================
    # BUFFER DE SEGURANÇA
    # =====================================================

    safety_stock = 100

    # =====================================================
    # DEMANDA TOTAL NECESSÁRIA
    # =====================================================

    required_stock = (
        predicted_demand + safety_stock
    )

    # =====================================================
    # QUANTIDADE NECESSÁRIA
    # =====================================================

    quantity = max(
        0,
        required_stock - current_stock
    )

    # =====================================================
    # LIMITA COMPRA EXCESSIVA
    # =====================================================

    max_purchase = 1000

    quantity = min(
        quantity,
        max_purchase
    )

    # =====================================================
    # CUSTOS
    # =====================================================

    unit_cost = 12

    logistics_cost = quantity * 2

    storage_cost = quantity * 1.5

    total_cost = (
        quantity * unit_cost
        + logistics_cost
        + storage_cost
    )

    # =====================================================
    # RETURN
    # =====================================================

    return {

        "optimized_quantity": int(quantity),

        "total_cost": round(total_cost, 2),

        "status": "optimized"
    }