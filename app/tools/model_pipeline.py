import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# 🔹 Load Dataset
def load_data(path):
    df = pd.read_csv(path)
    print("✅ Dataset Loaded:", df.shape)
    return df


# 🔹 Preprocess Data
def preprocess_data(df, target_column):
    
    df = df.copy()

    # Drop unnecessary columns if exist
    drop_cols = ['Pipe_ID', 'Inspection_Date']
    for col in drop_cols:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    # Handle missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Encode categorical columns
    label_encoders = {}
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le
    
    # REMOVE THESE from features
    leakage_cols = ['Failure_Risk', 'Recommended_Action']

    X = df.drop(columns=leakage_cols)
    y = df['Recommended_Action']

    return X, y, label_encoders


# 🔹 Train Model
def train_model(X, y):
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=8,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print("\n🎯 Accuracy:", acc)
    print("\n📊 Classification Report:\n", classification_report(y_test, preds))

    return model, acc


# 🔹 Save Model
def save_model(model, path="outputs/model.pkl"):
    joblib.dump(model, path)
    print("💾 Model saved at:", path)


# 🔹 Full Pipeline
def run_pipeline(data_path, target_column):

    df = load_data(data_path)

    X, y, encoders = preprocess_data(df, target_column)

    model, acc = train_model(X, y)

    save_model(model)

    return model, acc