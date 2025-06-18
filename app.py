from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load models and scaler
with open("arima_model.pkl", "rb") as f:
    arima_model = pickle.load(f)

with open("sarima_model.pkl", "rb") as f:
    sarima_model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/forecast_web", methods=["POST"])
def forecast_web():
    days = int(request.form["days"])
    model_type = request.form["model"]

    # Choose model and forecast (normalized values)
    if model_type == "sarima":
        forecast_scaled = sarima_model.forecast(steps=days)
    else:
        forecast_scaled = arima_model.forecast(steps=days)

    # Reverse normalization (back to original scale)
    forecast_scaled_reshaped = np.array(forecast_scaled).reshape(-1, 1)
    forecast_real = scaler.inverse_transform(forecast_scaled_reshaped).flatten()

    return render_template("index.html", forecast=forecast_real.tolist(), model=model_type)

if __name__ == "__main__":
    app.run(debug=True)
