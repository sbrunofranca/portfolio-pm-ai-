import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def train_model():

    # =====================================================
    # CARREGA DADOS
    # =====================================================
    df = pd.read_csv("data/sales.csv")

    # transforma data em variável numérica
    df["date"] = pd.to_datetime(df["date"])
    df["day_index"] = (df["date"] - df["date"].min()).dt.days

    X = df[["day_index"]]
    y = df["sales"]

    # =====================================================
    # MODELO SIMPLES (MVP)
    # =====================================================
    model = LinearRegression()
    model.fit(X, y)

    return model, df


def predict_future(model, last_day, days=7):

    future = np.array([[last_day + i] for i in range(1, days + 1)])
    preds = model.predict(future)

    return preds