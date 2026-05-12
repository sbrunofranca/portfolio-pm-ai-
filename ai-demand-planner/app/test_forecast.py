from forecast import train_model, predict_future

model, df = train_model()

last_day = df["day_index"].max()

preds = predict_future(model, last_day)

print("Previsão próximos dias:")
print(preds)