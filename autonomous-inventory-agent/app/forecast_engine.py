# =========================================================
# IMPORTS
# =========================================================

import pandas as pd

from xgboost import XGBRegressor


# =========================================================
# LOAD DATA
# =========================================================

def load_data():

    """
    Carrega histórico de demanda.
    """

    df = pd.read_csv(
        "data/demand_history.csv"
    )

    return df


# =========================================================
# FEATURE ENGINEERING
# =========================================================

def create_features(df):

    """
    Cria features temporais.
    """

    # =====================================================
    # LAGS
    # =====================================================

    df["lag_1"] = df["demand"].shift(1)

    df["lag_2"] = df["demand"].shift(2)

    df["rolling_mean"] = (
        df["demand"]
        .rolling(3)
        .mean()
    )

    # =====================================================
    # REMOVE NULLS
    # =====================================================

    df = df.dropna()

    return df


# =========================================================
# TRAIN MODEL
# =========================================================

def train_forecast_model(df):

    """
    Treina modelo de previsão.
    """

    # =====================================================
    # FEATURES
    # =====================================================

    features = [
        "day",
        "lag_1",
        "lag_2",
        "rolling_mean"
    ]

    X = df[features]

    y = df["demand"]

    # =====================================================
    # MODEL
    # =====================================================

    model = XGBRegressor(

        n_estimators=100,

        max_depth=3,

        learning_rate=0.1
    )

    model.fit(X, y)

    return model


# =========================================================
# FORECAST
# =========================================================

def predict_next_demand():

    """
    Prevê próxima demanda.
    """

    # =====================================================
    # LOAD DATA
    # =====================================================

    df = load_data()

    # =====================================================
    # FEATURES
    # =====================================================

    df = create_features(df)

    # =====================================================
    # TRAIN MODEL
    # =====================================================

    model = train_forecast_model(df)

    # =====================================================
    # LAST VALUES
    # =====================================================

    last_row = df.iloc[-1]

    next_day = last_row["day"] + 1

    lag_1 = last_row["demand"]

    lag_2 = df.iloc[-2]["demand"]

    rolling_mean = (
        df["demand"]
        .tail(3)
        .mean()
    )

    # =====================================================
    # PREDICTION DATA
    # =====================================================

    future = pd.DataFrame({

        "day": [next_day],

        "lag_1": [lag_1],

        "lag_2": [lag_2],

        "rolling_mean": [rolling_mean]
    })

    # =====================================================
    # PREDICTION
    # =====================================================

    prediction = model.predict(
        future
    )[0]

    return {

        "next_day": int(next_day),

        "predicted_demand": round(
            float(prediction),
            2
        )
    }