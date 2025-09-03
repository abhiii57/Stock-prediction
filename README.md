# 📈 Stock Market Prediction with LSTM + Streamlit

This project predicts stock prices using an **LSTM model** and displays results with **Streamlit**.  
It downloads stock data from **Yahoo Finance**, computes moving averages, and compares actual vs predicted prices.

---

## 🚀 Features
- Download historical stock data from Yahoo Finance
- Visualize:
  - MA50 (50-day moving average)
  - MA100 (100-day moving average)
  - MA200 (200-day moving average)
- Predict future stock prices using an LSTM model (`stockprediction.keras`)
- Interactive Streamlit web app

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhiii57/stock-market-prediction.git
   cd stock-market-prediction
2. Install Dependencies:
    pip install -r requirements.txt
3. Run the Streamlit app:
    streamlit run app.py
