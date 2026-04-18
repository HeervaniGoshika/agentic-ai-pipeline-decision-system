import streamlit as st
import pandas as pd

from app.inference import predict_and_decide
from app.memory.memory_store import load_memory


st.set_page_config(page_title="Agentic AI Pipeline System", layout="wide")

st.title("🚀 Agentic AI for Pipeline Maintenance")
st.markdown("Predict failure risk and get intelligent maintenance decisions")

# 🔹 Sidebar Inputs
st.sidebar.header("🔧 Input Parameters")

temperature = st.sidebar.slider("Temperature", 0, 150, 80)
pressure = st.sidebar.slider("Pressure", 0, 200, 120)
flow_rate = st.sidebar.slider("Flow Rate", 0, 500, 300)
corrosion_rate = st.sidebar.slider("Corrosion Rate", 0.0, 1.0, 0.5)
thickness_loss = st.sidebar.slider("Thickness Loss", 0.0, 1.0, 0.4)

repair_cost = st.sidebar.number_input("Repair Cost", value=10000)
downtime = st.sidebar.number_input("Downtime (days)", value=5)

# 🔹 Load memory ONCE
memory = load_memory()

# 🔹 Prediction Button
if st.sidebar.button("🚀 Run Prediction"):

    input_data = {
        "Temperature": temperature,
        "Pressure": pressure,
        "Flow_Rate": flow_rate,
        "Corrosion_Rate": corrosion_rate,
        "Thickness_Loss": thickness_loss,
        "Repair_Cost": repair_cost,
        "Downtime": downtime
    }

    try:
        result = predict_and_decide(input_data)
        st.session_state["result"] = result

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")

# 🔹 Show Result (persistent)
if "result" in st.session_state:

    result = st.session_state["result"]

    col1, col2, col3 = st.columns(3)

    col1.metric("📉 Predicted Risk", round(result["Predicted_Risk"], 2))
    col2.metric("🎯 Confidence", round(result["Confidence"], 2))
    col3.metric("🛠 Recommended Action", result["Recommended_Action"])

    # 🔥 Risk Indicator
    risk = result["Predicted_Risk"]

    if risk > 0.7:
        st.error(f"🔴 High Risk: {risk:.2f}")
    elif risk > 0.4:
        st.warning(f"🟡 Moderate Risk: {risk:.2f}")
    else:
        st.success(f"🟢 Low Risk: {risk:.2f}")

    # 📊 Risk Trend
    if memory:
        df = pd.DataFrame(memory)

        if "risk" in df.columns:
            st.subheader("📈 Risk Trend")
            st.line_chart(df["risk"])

            avg_risk = df["risk"].mean()
            st.info(f"📊 Average Historical Risk: {avg_risk:.2f}")

    # 🧠 Debate Explanation
    st.subheader("🧠 Agent Debate")

    for line in result["Debate_Explanation"].split("\n"):
        if line.strip():
            st.write("•", line.strip())

# 🔹 Memory Table
st.subheader("📊 Past Decisions (Memory)")

if memory:
    st.dataframe(pd.DataFrame(memory).tail(10))
else:
    st.write("No memory data available yet.")