# Flask Time Series Forecast App (ARIMA & SARIMA)

This project is a web-based time series forecasting app built with **Flask** that allows users to forecast future sales using either **ARIMA** or **SARIMA** models. It also includes a complete **Google Colab notebook** for model training, normalization, and serialization.


## Features

- Forecast daily sales for custom number of future days
- Choose between ARIMA or SARIMA models
- Models trained on normalized data using MinMaxScaler
- Reverse scaling applied in Flask before displaying results
- Web UI built using Flask + HTML/CSS
- Models and scaler saved and loaded using `pickle`
- Ready for deployment or local use


## Technologies Used

- Python
- Pandas, NumPy
- Statsmodels (ARIMA, SARIMA)
- scikit-learn (MinMaxScaler)
- Flask (Backend)
- HTML + CSS (Frontend)
- Google Colab (Model training)

### 🔹 1. Clone this repo
```bash
git clone https://github.com/rajkachhadiya123/flask-time-series-forecast-app.git
cd flask-forecast-app

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the flask App

python app.py

### 4. Open in Browser

http://127.0.0.1:5000/
