import joblib
from ai_model import predict_habitability

# Load the trained habitability model
model = joblib.load("models/habitability_classifier.pkl")

def get_user_input():
    """Get user input for planet radius and mass."""
    try:
        radius = float(input("Enter the Planet Radius (in Earth radii): "))
        mass = float(input("Enter the Planet Mass (in Earth masses): "))
        return radius, mass
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return get_user_input()

def main():
    """Main function to predict habitability."""
    print("Welcome to the Habitability Prediction System!")
    
    # Get user input for radius and mass
    radius, mass = get_user_input()

    # Make habitability prediction
    habitability = predict_habitability(model, radius, mass)

    # Output the result
    if habitability == 1:
        print(f"The planet with radius {radius} and mass {mass} is HABITABLE!")
    else:
        print(f"The planet with radius {radius} and mass {mass} is NOT HABITABLE!")

if __name__ == "__main__":
    main()
