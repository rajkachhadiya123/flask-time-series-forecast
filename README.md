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


