import joblib 
import pandas as pd
import numpy as np

model = joblib.load("models/exoplanet_classifier.pkl")

category_mapping = {
    0: "Earth-like",
    1: "Super-Earth",
    2: "Neptune-like",
    3: "Gas Giant"
}

def predict_exoplanet():
    try: 
        mass = float(input("Enter planet mass (Earth masses): "))
        radius = float(input("Enter planet radius (Earth radii): "))
        orbital_period = float(input("Enter orbital period (days): "))
        input_data = pd.DataFrame([[radius, mass, orbital_period]], columns=["Planet Radius (Earth radii)", "Planet Mass (Earth masses)", "Orbital Period (days)"])
        predicted_category = model.predict(input_data)[0]
        print(f"\nPredcited Exoplanet Category: {category_mapping[predicted_category]}")
    except ValueError:
        print("Invalid Input! Please enter numerical values.")

if __name__ == "__main__":
    predict_exoplanet()