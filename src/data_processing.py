import pandas as pd

def load_data(filepath="data/exoplanets.csv"):
    """Loads and cleans the exoplanet dataset."""
    df = pd.read_csv(filepath)

    if df is None:
        raise ValueError("Error: DataFrame is empty or file is not loaded properly.")

    # Clean missing values
    df = df.fillna({"pl_rade": df["pl_rade"].median()})
    df.dropna(subset=["pl_orbper", "pl_bmasse"], inplace=True)

    # Rename columns for better readability
    df = df.rename(columns={
        "pl_name": "Planet",
        "hostname": "Host Star",
        "pl_orbper": "Orbital Period (days)",
        "pl_rade": "Planet Radius (Earth radii)",
        "pl_bmasse": "Planet Mass (Earth masses)"
    })

    return df

def classify_planet(row):
    """Classifies planets into Earth-like, Super-Earth, Neptune-like, or Gas Giant."""
    if row["Planet Radius (Earth radii)"] < 2 and row["Planet Mass (Earth masses)"] < 10:
        return "Earth-like"
    elif 2 <= row["Planet Radius (Earth radii)"] < 10 and 10 <= row["Planet Mass (Earth masses)"] < 50:
        return "Super-Earth"
    elif 10 <= row["Planet Radius (Earth radii)"] < 20 and 50 <= row["Planet Mass (Earth masses)"] < 500:
        return "Neptune-like"
    else:
        return "Gas Giant"

def add_planet_category(df):
    """Adds a 'Category' column based on planet mass and radius."""
    df["Category"] = df.apply(classify_planet, axis=1)
    return df
