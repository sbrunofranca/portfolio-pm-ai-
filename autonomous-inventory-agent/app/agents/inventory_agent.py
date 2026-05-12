# =========================================================
# IMPORTA MOTOR DE OTIMIZAÇÃO
# =========================================================

from app.optimization import optimize_inventory


# =========================================================
# INVENTORY AGENT
# =========================================================

def inventory_decision(df):

    """
    Agente responsável pela decisão de estoque.
    """

    # =====================================================
    # OBTÉM ESTOQUE MAIS RECENTE
    # =====================================================

    latest_stock = df["inventory"].iloc[-1]

    # =====================================================
    # ESTIMA DEMANDA FUTURA
    # =====================================================

    # pega média dos últimos 7 dias
    # multiplica por 2 para projetar horizonte futuro

    predicted_demand = int(
        df["demand"].tail(7).mean() * 2
    )

    # =====================================================
    # EXECUTA OTIMIZAÇÃO
    # =====================================================

    optimization = optimize_inventory(
        latest_stock,
        predicted_demand
    )

    # =====================================================
    # DEFINE PRIORIDADE OPERACIONAL
    # =====================================================

    priority = "normal"

    # estoque crítico

    if latest_stock < 150:

        priority = "high"

    # =====================================================
    # RETORNO FINAL DO AGENTE
    # =====================================================

    return {

        # verifica se precisa comprar

        "restock": optimization[
            "optimized_quantity"
        ] > 0,

        # quantidade ótima

        "quantity": optimization[
            "optimized_quantity"
        ],

        # prioridade operacional

        "priority": priority,

        # status da otimização

        "optimization_status": optimization[
            "status"
        ],

        # custo estimado

        "estimated_cost": optimization[
            "total_cost"
        ],

        # demanda prevista

        "predicted_demand": predicted_demand
    }