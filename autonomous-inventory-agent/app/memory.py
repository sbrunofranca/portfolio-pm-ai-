# =========================================================
# IMPORTS
# =========================================================

import json

from datetime import datetime


# =========================================================
# MEMORY FILE
# =========================================================

MEMORY_FILE = "memory/decision_history.json"


# =========================================================
# LOAD MEMORY
# =========================================================

def load_memory():

    """
    Carrega histórico de decisões.
    """

    try:

        with open(
            MEMORY_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return []


# =========================================================
# SAVE MEMORY
# =========================================================

def save_decision(state):

    """
    Salva decisão atual.
    """

    # =====================================================
    # CARREGA HISTÓRICO
    # =====================================================

    history = load_memory()

    # =====================================================
    # NOVA ENTRADA
    # =====================================================

    entry = {

        "timestamp": str(
            datetime.now()
        ),

        "demand": state["demand"],

        "inventory": state["inventory"],

        "cost": state["cost"],

        "logistics": state["logistics"]
    }

    # =====================================================
    # ADICIONA NO HISTÓRICO
    # =====================================================

    history.append(entry)

    # =====================================================
    # LIMITA TAMANHO
    # =====================================================

    history = history[-20:]

    # =====================================================
    # SALVA JSON
    # =====================================================

    with open(
        MEMORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )


# =========================================================
# GET LAST DECISION
# =========================================================

def get_last_decision():

    """
    Retorna última decisão.
    """

    history = load_memory()

    if len(history) == 0:

        return None

    return history[-1]