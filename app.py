import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import matplotlib.pyplot as plt

model=load_model('C:\github projects\Stock prediction\stockprediction.keras')

st.header("Stock Market Predictor")

stock=st.text_input("Enter Stock Symbol","GOOG")

start='2012-01-01'
end='2022-12-31'

data=yf.download(stock,start,end)

st.subheader('Stock Data')
st.write(data)

data_train = pd.DataFrame(data.Close[0 : int(len(data) * 0.85)])
data_test  = pd.DataFrame(data.Close[int(len(data) * 0.85) : len(data)])

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))

pas_100_days=data_train.tail(100)
data_test=pd.concat([pas_100_days,data_test],ignore_index=True)
data_test_scale=scaler.fit_transform(data_test)

st.subheader("Price VS MA50")
ma_50_days=data.Close.rolling(50).mean()
fig1=plt.figure(figsize=(8,6))
plt.plot(ma_50_days,'r',label="MA50")
plt.plot(data.Close,'g',label='Price')
plt.legend()
plt.show()
st.pyplot(fig1)

st.subheader("Price VS MA50 VS MA100")
ma_100_days=data.Close.rolling(100).mean()
fig2=plt.figure(figsize=(8,6))
plt.plot(ma_50_days,'b',label='MA50')
plt.plot(ma_100_days,'r',label='MA100')
plt.plot(data.Close,'g',label='Price')
plt.legend()
plt.show()
st.pyplot(fig2)

st.subheader("Price VS MA100 VS MA200")
ma_200_days=data.Close.rolling(200).mean()
fig3=plt.figure(figsize=(8,6))
plt.plot(ma_100_days,'b',label='Ma100')
plt.plot(ma_200_days,'r',label='MA200')
plt.plot(data.Close,'g',label='Price')
plt.legend()
plt.show()
st.pyplot(fig3)
x=[]
y=[]

for i in range(110,data_test_scale.shape[0]):
    x.append(data_test_scale[i-110:i])
    y.append(data_test_scale[i,0])

x,y=np.array(x),np.array(y)

predict=model.predict(x)
scale=1/scaler.scale_

predict=predict*scale
y=y*scale

st.subheader('Orignal Price VS Predicted Price')
fig4=plt.figure(figsize=(8,6))
plt.plot(predict,'r',label='Orignal Price')
plt.plot(y,'g',label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()
st.pyplot(fig4)
