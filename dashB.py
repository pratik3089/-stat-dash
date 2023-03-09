import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express
st.title("IRIS DASH")
df = pd.read_csv('iris.csv')
st.dataframe(df)

fig,ax = plt.subplots()
ax.scatter(df.iloc[:,0],df.iloc[:,1])
st.pyplot(fig)

fig1,ax = plt.subplots()
ax.scatter(df.iloc[:,2] , df.iloc[:,3])
st.pyplot(fig1)

st.line_chart(df.iloc[:,2])

fig2,ax = plt.subplots()
ax.hist(df.iloc[:,1])
st.pyplot(fig2)


st.bar_chart(df.iloc[:,2])

st.area_chart(df.iloc[:,1])

t =df['species'].value_counts()
st.write(t)
st.bar_chart(t)
fig,ax = plt.subplots()
