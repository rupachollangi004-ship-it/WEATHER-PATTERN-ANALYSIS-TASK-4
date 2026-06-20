import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="Weather Pattern Analysis Dashboard",
                   layout="wide")

# Dashboard Title
st.title("Weather Pattern Analysis Dashboard")

# Sample Weather Data (No Dataset Required)
weather_data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Temperature": [30, 32, 29, 31, 33, 34, 30],
    "Humidity": [65, 70, 68, 72, 75, 73, 67],
    "Rainfall": [5, 0, 10, 2, 0, 8, 3]
}

df = pd.DataFrame(weather_data)

# KPI Section
st.subheader("Weather Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Temperature", f"{df['Temperature'].mean():.1f} °C")

with col2:
    st.metric("Average Humidity", f"{df['Humidity'].mean():.1f}%")

with col3:
    st.metric("Total Rainfall", f"{df['Rainfall'].sum()} mm")

# Temperature Trend
st.subheader("Temperature Trend")

temp_chart = px.line(
    df,
    x="Day",
    y="Temperature",
    markers=True,
    title="Weekly Temperature Analysis"
)

st.plotly_chart(temp_chart, use_container_width=True)

# Humidity Analysis
st.subheader("Humidity Analysis")

humidity_chart = px.bar(
    df,
    x="Day",
    y="Humidity",
    title="Daily Humidity Levels"
)

st.plotly_chart(humidity_chart, use_container_width=True)

# Rainfall Distribution
st.subheader("Rainfall Distribution")

rain_chart = px.pie(
    df,
    names="Day",
    values="Rainfall",
    title="Rainfall Contribution"
)

st.plotly_chart(rain_chart, use_container_width=True)

# Data Table
st.subheader("Weather Data")

st.dataframe(df)

# Footer
st.success("Weather Pattern Analysis Dashboard Generated Successfully!")