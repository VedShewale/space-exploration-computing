import joblib 
import pandas as pd

model = joblib.load("models/exoplanet_classifier.pkl")

def predict_exoplanet(planet_radius, planet_mass, orbital_period):
    input_data = pd.DataFrame([[planet_radius,planet_mass, orbital_period]], columns=["Planet Radius (Earth radii)", "Planet Mass (Earth masses)", "Orbital Period (days)"])
    prediction = model.predict(input_data)
    return prediction[0]

# Mapping numerical labels to their planet categories
category_mapping = {
    0: "Earth-like",
    1: "Super-Earth",
    2: "Neptune-like",
    3: "Gas Giant"
}

example_prediction = predict_exoplanet(1.5, 5.2, 365)
predicted_category = category_mapping[example_prediction]
print(f"Predicted Exoplanet Category: {predicted_category}")