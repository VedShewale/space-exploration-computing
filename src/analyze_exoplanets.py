import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/exoplanets.csv")

if df is None:
    raise ValueError("Error: DataFrame is empty or file is not loaded properly.")

df.isnull().sum()
df = df.fillna({"pl_rade": df["pl_rade"].median()})
df = df.dropna(subset=["pl_orbper", "pl_bmasse"], inplace=True)

df = df.rename(columns={
    "pl_name": "Planet",
    "hostname": "Host Star",
    "pl_orbper": "Orbital Period (days)",
    "pl_rade": "Planet Radius (Earth radii)",
    "pl_bmasse": "Planet Mass (Earth masses)"
})

print(df.head())
print(df.describe())
print(df.nlargest(5, "pl_rade"))
print(df.nsmallest(5, "pl_rade"))
print(df.corr())

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Planet Radius (Earth radii)", y="Planet Mass (Earth masses)", data=df)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Planet Radius (Earth radii)")
plt.ylabel("Planet Mass (Earth masses)")
plt.title("Exoplanet Mass vs. Radius")
plt.show()