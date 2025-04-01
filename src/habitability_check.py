import pandas as pd
import numpy as np

def load_data(filepath="data/exoplanets.csv"):
    """Loads the exoplanet dataset."""
    df = pd.read_csv(filepath)
    df = df.rename(columns={
    'pl_rade': 'Planet Radius (Earth radii)',
    'pl_bmasse': 'Planet Mass (Earth masses)'
    })
    
    if df is None:
        raise ValueError("Error: DataFrame is empty or file is not loaded properly.")
    
    return df

def assign_habitability(df):
    """Assigns habitability (1 for habitable, 0 for non-habitable)."""
    habitability = []
    
    for _, row in df.iterrows():
        # Habitability condition: 0.5 < Radius ≤ 1.6 and 0.1 < Mass ≤ 3
        if 0.5 < row["Planet Radius (Earth radii)"] <= 1.6 and 0.1 < row["Planet Mass (Earth masses)"] <= 3:
            habitability.append(1)  # Potentially habitable
        else:
            habitability.append(0)  # Not habitable
    
    df["Habitability"] = habitability
    return df

def save_data(df, output_filepath="data/exoplanets_with_habitability.csv"):
    """Saves the DataFrame with habitability column."""
    df.to_csv(output_filepath, index=False)
    print(f"Data saved to {output_filepath}")

# Main script to execute
if __name__ == "__main__":
    df = load_data("data/exoplanets.csv")  # Adjust path if necessary
    df = assign_habitability(df)
    save_data(df)
