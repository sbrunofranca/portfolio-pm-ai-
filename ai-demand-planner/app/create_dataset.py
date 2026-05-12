import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range("2024-01-01", periods=180)

data = pd.DataFrame({
    "date": dates,
    "sku": "SKU_1",
    "sales": np.random.randint(20, 100, size=len(dates))
})

data.to_csv("data/sales.csv", index=False)