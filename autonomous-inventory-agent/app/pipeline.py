# =========================================================
# IMPORTS
# =========================================================

from app.simulation import generate_inventory_data

from app.workflow import run_workflow

from app.llm_explainer import explain_decision

from app.memory import save_decision

from app.memory import get_last_decision


# =========================================================
# MAIN PIPELINE
# =========================================================

def run_pipeline():

    """
    Executa pipeline completo.
    """

    # =====================================================
    # GERA DADOS
    # =====================================================

    df = generate_inventory_data()

    # =====================================================
    # ÚLTIMA DECISÃO
    # =====================================================

    previous_decision = get_last_decision()

    # =====================================================
    # EXECUTA WORKFLOW
    # =====================================================

    agents_state = run_workflow(df)

    # =====================================================
    # SALVA MEMÓRIA
    # =====================================================

    save_decision(agents_state)

    # =====================================================
    # EXPLICAÇÃO IA
    # =====================================================

    explanation = explain_decision(
        agents_state,
        df["inventory"].iloc[-1]
    )

    # =====================================================
    # RETURN
    # =====================================================

    return {

        "data": df,

        "agents": agents_state,

        "previous_decision": previous_decision,

        "explanation": explanation
    }