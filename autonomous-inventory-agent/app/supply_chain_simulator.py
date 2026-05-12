# =========================================================
# IMPORTS
# =========================================================

import simpy

import random


# =========================================================
# INVENTORY SYSTEM
# =========================================================

class InventorySystem:

    """
    Simula operação de estoque.
    """

    def __init__(

        self,

        env,

        initial_stock=500,

        reorder_point=200,

        reorder_quantity=400,

        lead_time=3
    ):

        # =================================================
        # SIMULATION ENVIRONMENT
        # =================================================

        self.env = env

        # =================================================
        # INVENTORY VARIABLES
        # =================================================

        self.stock = initial_stock

        self.reorder_point = reorder_point

        self.reorder_quantity = reorder_quantity

        self.lead_time = lead_time

        # =================================================
        # METRICS
        # =================================================

        self.stock_history = []

        self.stockouts = 0

        self.orders = []

    # =====================================================
    # DAILY DEMAND
    # =====================================================

    def consume_inventory(self):

        """
        Consome estoque diariamente.
        """

        while True:

            # =============================================
            # RANDOM DEMAND
            # =============================================

            demand = random.randint(40, 80)

            # =============================================
            # CHECK STOCK
            # =============================================

            if self.stock >= demand:

                self.stock -= demand

            else:

                # =========================================
                # STOCKOUT
                # =========================================

                self.stockouts += 1

                self.stock = 0

            # =============================================
            # SAVE HISTORY
            # =============================================

            self.stock_history.append({

                "day": self.env.now,

                "stock": self.stock,

                "demand": demand
            })

            # =============================================
            # CHECK REPLENISHMENT
            # =============================================

            if self.stock <= self.reorder_point:

                self.env.process(
                    self.replenish_stock()
                )

            # =============================================
            # NEXT DAY
            # =============================================

            yield self.env.timeout(1)

    # =====================================================
    # REPLENISHMENT
    # =====================================================

    def replenish_stock(self):

        """
        Simula pedido de reposição.
        """

        # ================================================
        # SAVE ORDER
        # ================================================

        self.orders.append({

            "day_ordered": self.env.now,

            "quantity": self.reorder_quantity
        })

        # ================================================
        # LEAD TIME
        # ================================================

        yield self.env.timeout(
            self.lead_time
        )

        # ================================================
        # STOCK ARRIVES
        # ================================================

        self.stock += self.reorder_quantity


# =========================================================
# RUN SIMULATION
# =========================================================

def run_simulation(days=30):

    """
    Executa simulação.
    """

    # =====================================================
    # ENVIRONMENT
    # =====================================================

    env = simpy.Environment()

    # =====================================================
    # INVENTORY SYSTEM
    # =====================================================

    inventory = InventorySystem(env)

    # =====================================================
    # START PROCESS
    # =====================================================

    env.process(
        inventory.consume_inventory()
    )

    # =====================================================
    # RUN
    # =====================================================

    env.run(until=days)

    return {

        "stock_history": inventory.stock_history,

        "stockouts": inventory.stockouts,

        "orders": inventory.orders,

        "final_stock": inventory.stock
    }