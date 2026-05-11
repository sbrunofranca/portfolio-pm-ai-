from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/sample.db")

with engine.connect() as conn:

    # =========================================================
    # CRIA TABELA SALES
    # =========================================================
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        revenue REAL
    )
    """))

    # =========================================================
    # INSERE DADOS MOCK
    # =========================================================
    conn.execute(text("""
    INSERT INTO sales (date, revenue) VALUES
    ('2024-01-01', 1000),
    ('2024-01-02', 1500),
    ('2024-01-03', 2000)
    """))

    conn.commit()

print("Banco inicializado com sucesso!")