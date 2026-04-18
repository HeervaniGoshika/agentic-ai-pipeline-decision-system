import joblib
import pandas as pd

from app.agents.debate_agents import SafetyAgent, CostAgent, ModeratorAgent
from app.memory.memory_store import save_memory
from app.agents.self_correction_agent import SelfCorrectionAgent


def predict_and_decide(input_data):

    # 🔹 Load model
    model = joblib.load("outputs/risk_model.pkl")

    df = pd.DataFrame([input_data])
    df = pd.get_dummies(df)

    # 🔹 Align features
    model_features = model.feature_names_in_

    for col in model_features:
        if col not in df.columns:
            df[col] = 0

    df = df[model_features]

    # 🔹 Predict
    risk = model.predict(df)[0]

    # 🔥 Confidence
    confidence = 1 - abs(risk - 0.5)

    # 🔁 Self-correction
    correction_agent = SelfCorrectionAgent()

    if correction_agent.evaluate(risk, confidence):
        print("⚠ Low confidence → applying self-correction")
        risk = correction_agent.correct(risk)

    # 🤖 Multi-Agent Debate
    safety_agent = SafetyAgent()
    cost_agent = CostAgent()
    moderator = ModeratorAgent()

    safety_opinion = safety_agent.argue(risk)

    cost_opinion = cost_agent.argue(
        risk,
        repair_cost=input_data.get("Repair_Cost"),
        downtime=input_data.get("Downtime")
    )

    final_action, debate_explanation = moderator.decide(
        risk,
        safety_opinion,
        cost_opinion
    )

    # 📦 Final Result
    result = {
        "Predicted_Risk": float(risk),
        "Confidence": float(confidence),
        "Recommended_Action": final_action,  # ✅ FIXED
        "Debate_Explanation": debate_explanation
    }

    # 🔥 Logging
    with open("outputs/log.txt", "a") as f:
        f.write(str(result) + "\n")

    # 🧠 Memory (MUST be before return)
    memory_entry = {
        "input": input_data,
        "risk": float(risk),
        "confidence": float(confidence),
        "decision": final_action
    }

    save_memory(memory_entry)

    return result