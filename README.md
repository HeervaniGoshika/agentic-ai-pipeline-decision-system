# 🚀 Agentic AI Pipeline Maintenance System

An intelligent **Agentic AI system** for predictive maintenance in oil & gas pipelines.  
This project goes beyond traditional ML by combining **multi-agent reasoning, memory, self-correction, and real-time visualization**.

---

## ✨ Key Features

- 📉 **Failure Risk Prediction** using Machine Learning (Regression)
- 🤖 **Multi-Agent Debate System** (Safety vs Cost vs Moderator)
- 🧠 **Explainable AI** with structured reasoning
- 🔁 **Self-Correction Mechanism** based on confidence
- 💾 **Memory Module** to store historical decisions
- 📊 **Interactive Streamlit Dashboard**
- ⚡ **Real-time Simulation** using user inputs

---

## 🏗️ System Architecture

```
Input Data (Sensors)
        ↓
ML Model → Predict Failure Risk
        ↓
Confidence Estimation
        ↓
Self-Correction Agent
        ↓
Multi-Agent Debate
    ├── Safety Agent
    ├── Cost Agent
    └── Moderator Agent
        ↓
Final Decision
        ↓
Memory Storage + UI Visualization
```

---

## 🛠️ Tech Stack

- **Backend:** Python
- **ML:** Scikit-learn, Pandas, NumPy
- **UI:** Streamlit
- **Agents:** Custom Multi-Agent System
- **Memory:** JSON-based persistence
- **Visualization:** Streamlit charts
- **Optional LLM:** OpenAI (with fallback)

---

## 🚀 Setup and Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/agentic-ai-pipeline-maintenance.git
cd agentic-ai-pipeline-maintenance
```

---

### 2. Create Virtual Environment

```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Training Pipeline

```bash
python main.py
```

---

### 5. Run Streamlit Dashboard

```bash
streamlit run app/ui/dashboard.py
```

---

## 🖥️ How to Use

1. Adjust input parameters using sliders:
   - Temperature  
   - Pressure  
   - Flow Rate  
   - Corrosion Rate  
   - Thickness Loss  

2. Click **Run Prediction**

3. View:
   - 📉 Risk Score  
   - 🎯 Confidence  
   - 🛠 Recommended Action  
   - 🧠 Agent Debate Explanation  
   - 📊 Risk Trend Graph  

4. Check **Memory Table** for past decisions

---

