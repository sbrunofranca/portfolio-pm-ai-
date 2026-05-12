def check_restock(df):

    latest_stock = df["inventory"].iloc[-1]

    if latest_stock < 150:

        return {
            "restock": True,
            "quantity": 500,
            "reason": "Estoque abaixo do mínimo."
        }

    return {
        "restock": False,
        "quantity": 0,
        "reason": "Estoque saudável."
    }