import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from data_processing import load_data, add_planet_category
import joblib

def train_ai_model():
    """Train a Random Forest model to classify exoplanets"""
    #Load and preprocess data
    df = load_data()
    df = add_planet_category(df)

    #Select relevant features
    features = ["Planet Radius (Earth radii)", "Planet Mass (Earth masses)", "Orbital Period (days)"]
    X = df[features]
    y = df["Category"]

    #Encode categorical labels into numerical values
    y_encoded = y.astype("category").cat.codes

    #Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    #Train Random Forest model
    model = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    #Make predictions
    y_pred = model.predict(X_test)

    #Evaluate model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy {accuracy:.2f}")
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return model

if __name__ == "__main__":
    train_ai_model()

model = train_ai_model()

joblib.dump(model, "models/exoplanet_classifier.pkl")
print("Model Saved Successfully")