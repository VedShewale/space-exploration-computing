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

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def load_data(filepath="data/exoplanets_with_habitability.csv"):
    """Load and clean exoplanet data."""
    df = pd.read_csv(filepath)
    
    # Ensure relevant columns are present
    if "Planet Radius (Earth radii)" not in df.columns or "Planet Mass (Earth masses)" not in df.columns:
        raise ValueError("Necessary columns are missing!")
    
    # Clean missing values (you may adjust based on your needs)
    df = df.fillna({"Planet Radius (Earth radii)": df["Planet Radius (Earth radii)"].median(),
                    "Planet Mass (Earth masses)": df["Planet Mass (Earth masses)"].median()})
    
    # The habitability column should be defined before training (1: habitable, 0: not habitable)
    return df

def train_habitability_model(df):
    """Train a machine learning model to predict habitability."""
    # Select features and target
    features = ["Planet Radius (Earth radii)", "Planet Mass (Earth masses)"]
    target = "Habitability"  # Ensure habitability column exists
    
    X = df[features]
    y = df[target]
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the model (Random Forest for this example)
    habitability_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    
    # Train the model
    habitability_model.fit(X_train, y_train)
    
    # Predict and evaluate
    y_pred = habitability_model.predict(X_test)
    print("Model Accuracy: ", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    return habitability_model

if __name__ == "__main__":
    df = load_data("data/exoplanets_with_habitability.csv")
    train_habitability_model(df)
    habitability_model = train_habitability_model(df)
    joblib.dump(habitability_model, "models/habitability_classifier.pkl")
    print("Model saved to 'models/habitability_classifier.pkl'")

def predict_habitability(habitability_model, radius, mass):
    """Predict habitability of a new planet."""
    prediction = habitability_model.predict([[radius, mass]])  # Predict using the trained model
    return prediction[0]  # Return 0 (not habitable) or 1 (habitable)
