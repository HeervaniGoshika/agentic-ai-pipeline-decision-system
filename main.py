from app.tools.risk_model import run_pipeline
from app.inference import predict_and_decide

if __name__ == "__main__":

    # 🔹 Train model
    run_pipeline("data/pipeline_dataset.csv")

    # 🔹 Example input (simulate new pipeline data)
    sample_input = {
        "Temperature": 80,
        "Pressure": 120,
        "Flow_Rate": 300,
        "Corrosion_Rate": 0.8,
        "Thickness_Loss": 0.6
    }

    result = predict_and_decide(sample_input)

    print("\n🚀 FINAL OUTPUT:")
    print(result)