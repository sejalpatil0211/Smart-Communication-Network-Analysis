
import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# 1. Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Smart Communication Network Analysis",
    page_icon="📡",
    layout="wide"
)

# --------------------------------------------------
# 2. Load Trained ML Model
# --------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("network_model.pkl")


try:
    model = load_model()
except Exception as e:
    st.error(f"Unable to load the ML model: {e}")
    st.stop()

# --------------------------------------------------
# 3. Application Title
# --------------------------------------------------

st.title("📡 Smart Communication Network Analysis")

st.write(
    "Enter network parameters to predict the network condition "
    "using Machine Learning."
)

st.divider()

# --------------------------------------------------
# 4. Network Parameters Input
# --------------------------------------------------

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
            "Channel Utilization (%)",
            0, 100, 30
        )

        latency_ms = st.number_input(
            "Latency (ms)",
            min_value=0.0,
            value=20.0
        )

    with col2:

        packet_loss_pct = st.slider(
            "Packet Loss (%)",
            0.0, 100.0, 1.0
        )

        dhcp_failures = st.number_input(
            "DHCP Failures",
            min_value=0,
            value=0,
            step=1
        )

        dns_risk_score = st.slider(
            "DNS Risk Score",
            0.0, 100.0, 10.0
        )

    submitted = st.form_submit_button(
        "Predict Network Condition",
        use_container_width=True
    )

# --------------------------------------------------
# 5. Prediction
# --------------------------------------------------

if submitted:

    try:

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

        probabilities = model.predict_proba(input_data)[0]

        # ------------------------------------------
        # 6. Prediction Result
        # ------------------------------------------

        st.divider()
        st.subheader("Prediction Result")

        st.success(
            f"Predicted Network Condition: {prediction}"
        )

        descriptions = {
            "healthy": "The model classifies this input as a healthy network.",
            "weak_signal": "The model detects a weak-signal incident.",
            "high_latency": "The model detects a high-latency incident.",
            "wifi_congestion": "The model detects Wi-Fi congestion.",
            "dns_security_risk": "The model detects a possible DNS security risk.",
            "dhcp_failure": "The model detects a DHCP failure."
        }

        st.info(
            descriptions.get(
                prediction,
                "Predicted incident category."
            )
        )

        # ------------------------------------------
        # 7. Highest Model Probability
        # ------------------------------------------

        highest_probability = max(probabilities) * 100

        st.metric(
            "Highest Model Probability",
            f"{highest_probability:.2f}%"
        )

        # ------------------------------------------
        # 8. Prediction Probability Chart
        # ------------------------------------------

        probability_df = pd.DataFrame({
            "Incident Category": model.classes_,
            "Model Probability (%)": probabilities * 100
        }).sort_values(
            "Model Probability (%)",
            ascending=False
        )

        st.subheader("Prediction Probabilities")

        st.bar_chart(
            probability_df.set_index("Incident Category")
        )

        st.caption(
            "Probabilities represent the model's estimated "
            "class probabilities, not guaranteed prediction accuracy."
        )

    except Exception as e:

        st.error(f"Prediction failed: {e}")

# --------------------------------------------------
# 9. Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Smart Communication Network Analysis | "
    "Machine Learning Project"
)
