# =========================================================
# DATABASE LAYER
# =========================================================

from sqlalchemy import create_engine
import pandas as pd

# Banco local SQLite (MVP simples)
engine = create_engine("sqlite:///data/sample.db")


def run_query(sql: str):
    """
    Executa SQL no banco e retorna resultado como DataFrame
    """
    return pd.read_sql(sql, engine)