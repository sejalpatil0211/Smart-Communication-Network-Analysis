
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model/network_model.pkl")

st.set_page_config(
    page_title="Smart Communication Network Analysis",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Smart Communication Network Analysis")
st.write("Enter network parameters to predict the network condition.")

st.subheader("Network Parameters")

with st.form("network_form"):
    col1, col2 = st.columns(2)

    with col1:
        device_type = st.selectbox(
            "Device Type",
            ["router", "access_point", "client", "switch", "unknown"]
        )

        rssi_dbm = st.number_input(
            "Signal Strength (dBm)",
            min_value=-120.0,
            max_value=0.0,
            value=-55.0
        )

        channel_utilization_pct = st.slider(
            "Channel Utilization (%)", 0, 100, 30
        )

        latency_ms = st.number_input(
            "Latency (ms)", min_value=0.0, value=20.0
        )

    with col2:
        packet_loss_pct = st.slider(
            "Packet Loss (%)", 0.0, 100.0, 1.0
        )

        dhcp_failures = st.number_input(
            "DHCP Failures", min_value=0, value=0, step=1
        )

        dns_risk_score = st.slider(
            "DNS Risk Score", 0.0, 100.0, 10.0
        )

    submitted = st.form_submit_button("Predict Network Condition")

if submitted:
    input_data = pd.DataFrame([{
        "rssi_dbm": rssi_dbm,
        "channel_utilization_pct": channel_utilization_pct,
        "latency_ms": latency_ms,
        "packet_loss_pct": packet_loss_pct,
        "dhcp_failures": dhcp_failures,
        "dns_risk_score": dns_risk_score,
        "device_type": device_type
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")
    st.success(f"Predicted Network Condition: {prediction}")

    descriptions = {
        "healthy": "The model classifies this input as a healthy network.",
        "weak_signal": "The model detects a weak-signal incident.",
        "high_latency": "The model detects a high-latency incident.",
        "wifi_congestion": "The model detects Wi-Fi congestion.",
        "dns_security_risk": "The model detects a possible DNS security risk.",
        "dhcp_failure": "The model detects a DHCP failure."
    }

    st.write(descriptions.get(prediction, "Predicted incident category."))

    probabilities = model.predict_proba(input_data)[0]
    probability_df = pd.DataFrame({
        "Incident Category": model.classes_,
        "Model Probability (%)": probabilities * 100
    }).sort_values("Model Probability (%)", ascending=False)

    st.subheader("Prediction Probabilities")
    st.bar_chart(
        probability_df.set_index("Incident Category")
    )
