import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def load_data(path):
    df = pd.read_csv(path)
    return df


def preprocess(df):
    df = df.copy()

    # ❌ REMOVE leakage
    drop_cols = ['Recommended_Action']
    for col in drop_cols:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    # Handle missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Encode categorical
    df = pd.get_dummies(df, drop_first=True)

    X = df.drop(columns=['Failure_Risk'])
    y = df['Failure_Risk']

    return X, y


def train_model(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)

    print("📉 MAE:", mae)

    return model


def save_model(model):
    joblib.dump(model, "outputs/risk_model.pkl")


def run_pipeline(path):
    df = load_data(path)
    X, y = preprocess(df)
    model = train_model(X, y)
    save_model(model)

    return model