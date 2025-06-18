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
  
#  Clone the repository
git clone https://github.com/rajkachhadiya123/flask-time-series-forecast.git
cd flask-time-series-forecast


# Install dependencies
pip install -r requirements.txt || pip install flask pandas numpy scikit-learn statsmodels

# Run the Flask application
python app.py

# Once running, open your browser and visit:


# http://127.0.0.1:5000/

