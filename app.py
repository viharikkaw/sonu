from Analytics import load_energy_data,visualize_daily_usage,usage_by_appliance,hourly_pattern
import datetime as dt
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.markdown("<h1 style='text-align:center;'>" " 🏠AI Smart Home Energy Console</h1>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Detect • Forecast • Optimizer ⚙</h3>", unsafe_allow_html=True)

df = load_energy_data()

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='metric-box><h4>Total Energy Used</h4><h2>{round(df['total_usage'].sum(), 2)} KWh</h2></div>", unsafe_allow_html=True)
with col2:
    avg_day = round(df.groupby(df['timestamp'].dt.date)['total_usage'].sum().mean(),2)
    st.markdown(f"<div class='metric-box'><h4>Average Daily Usage</h4><h2>{avg_day}KWh</h2></div>",unsafe_allow_html=True)
with col3:
    ac_pct = round((df['ac_usage'].sum() /df['total_usage'].sum()) * 100, 1)
    st.markdown(f"<div class='metric-box'><h4>AC Usage Contribution</h4><h2>{ac_pct}%</h2></div>",unsafe_allow_html=True)


st.markdown("## 📊 Daily Usage Trend")
st.pyplot(visualize_daily_usage(df))

st.markdown("## 💡 Appliance-wise Energy Usage")
st.pyplot(usage_by_appliance(df))

st.markdown("## ⏰ Hourly Usage Patteren")
st.pyplot(hourly_pattern(df))