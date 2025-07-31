import streamlit as st
import time
import random
import pandas as pd

# Set page title
st.set_page_config(page_title="Rocket Telemetry Simulator", layout="wide")
st.title(" Rocket Telemetry Simulator Dashboard")

# Data simulation
def generate_data():
    return {
        "Altitude (m)": random.uniform(100 + i * 20, 120 + i * 20),
        "Velocity (m/s)": random.uniform(300, 500),
        "Temperature (°C)": random.uniform(15, 35)
    }

# Set up empty lists for plotting
altitudes, velocities, temperatures, timestamps = [], [], [], []

# Display charts
chart_placeholder = st.empty()
log_placeholder = st.empty()

# Simulate data stream
for i in range(60):  # run for 60 iterations (~1 min)
    data = generate_data()
    timestamp = time.strftime("%H:%M:%S")
    
    altitudes.append(data["Altitude (m)"])
    velocities.append(data["Velocity (m/s)"])
    temperatures.append(data["Temperature (°C)"])
    timestamps.append(timestamp)

    # Create dataframe
    df = pd.DataFrame({
        "Timestamp": timestamps,
        "Altitude (m)": altitudes,
        "Velocity (m/s)": velocities,
        "Temperature (°C)": temperatures
    })

    # Show plots
    with chart_placeholder.container():
        st.subheader(" Live Telemetry Data")
        st.line_chart(df.set_index("Timestamp"))

    # Show latest log
    with log_placeholder.container():
        st.subheader("📋 Latest Reading")
        st.write(f"⏱️ Time: {timestamp}")
        st.write(f"🛰️ Altitude: {data['Altitude (m)']:.2f} m")
        st.write(f"💨 Velocity: {data['Velocity (m/s)']:.2f} m/s")
        st.write(f"🌡️ Temperature: {data['Temperature (°C)']:.2f} °C")

    time.sleep(1)

st.success("Simulation Complete ✅")
