# =========================================================
# COST AGENT
# =========================================================

def analyze_cost(quantity):

    """
    Calcula custos operacionais.
    """

    # =====================================================
    # CUSTO UNITÁRIO
    # =====================================================

    unit_cost = 12

    # =====================================================
    # CUSTO LOGÍSTICO
    # =====================================================

    # custo de transporte/distribuição

    logistics_cost = quantity * 2

    # =====================================================
    # CUSTO DE ARMAZENAGEM
    # =====================================================

    # custo de manter produto em estoque

    storage_cost = quantity * 1.5

    # =====================================================
    # CUSTO TOTAL
    # =====================================================

    total_cost = (
        quantity * unit_cost
        + logistics_cost
        + storage_cost
    )

    # =====================================================
    # RETORNO FINAL
    # =====================================================

    return {

        "unit_cost": unit_cost,

        "logistics_cost": logistics_cost,

        "storage_cost": storage_cost,

        "total_cost": total_cost
    }