import pandas as pd
import numpy as np


def generate_inventory_data():

    days = list(range(30))

    demand = np.random.randint(20, 50, size=30)

    inventory = []

    stock = 500

    for d in demand:

        stock -= d

        inventory.append(stock)

    df = pd.DataFrame({
        "day": days,
        "demand": demand,
        "inventory": inventory
    })

    return df