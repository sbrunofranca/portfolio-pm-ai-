from app.forecast import train_model, predict_future
from app.explainability import explain_forecast
from app.insights import generate_insights
from app.llm_insights import generate_llm_insights


def run_pipeline():

    model, df = train_model()

    last_day = df["day_index"].max()

    predictions = predict_future(model, last_day)

    history = df["demand"].tolist() if "demand" in df else []
    forecast = predictions.tolist() if hasattr(predictions, "tolist") else predictions

    # =====================================================
    # RULE-BASED INSIGHTS
    # =====================================================
    insights = generate_insights(history, forecast)

    # =====================================================
    # LLM INSIGHTS (NOVO)
    # =====================================================
    llm_explanation = generate_llm_insights(history, forecast)

    return {
        "history": history,
        "forecast": forecast,
        "insights": insights,
        "llm_explanation": llm_explanation
    }