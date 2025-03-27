import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data\exoplanets.csv")

if df is None:
    raise ValueError("Error: DataFrame is empty or file is not loaded properly.")

df.isnull().sum()
df = df.fillna({"pl_rade": df["pl_rade"].median()})
df.dropna(subset=["pl_orbper", "pl_bmasse"], inplace=True)

df = df.rename(columns={
    "pl_name": "Planet",
    "hostname": "Host Star",
    "pl_orbper": "Orbital Period (days)",
    "pl_rade": "Planet Radius (Earth radii)",
    "pl_bmasse": "Planet Mass (Earth masses)"
})

print(df.head())
print(df.describe())
print(df.nlargest(5, "Planet Radius (Earth radii)"))
print(df.nsmallest(5, "Planet Radius (Earth radii)"))
print(df.select_dtypes(include=['number']).corr())

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Planet Radius (Earth radii)", y="Planet Mass (Earth masses)", data=df)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Planet Radius (Earth radii)")
plt.ylabel("Planet Mass (Earth masses)")
plt.title("Exoplanet Mass vs. Radius")
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df["Planet Radius (Earth radii)"], bins=30, edgecolor="black")
plt.xlabel("Planet Radius (Earth radii)")
plt.ylabel("Number of Planets")
plt.title("Distribution of Planet Radii")
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df["Orbital Period (days)"], bins=30, edgecolor="black", log=True)
plt.xlabel("Orbital Period (days) - Log Scale")
plt.ylabel("Number of Planets")
plt.title("Distribution of Orbital Periods")
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Orbital Period (days)", y="Planet Mass (Earth masses)", data=df)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Orbital Period (days) - Log Scale")
plt.ylabel("Planet Mass (Earth masses)")
plt.title("Orbital Period vs. Planet Mass")
plt.show()

correlation_matrix = df.select_dtypes(include=['number']).corr()
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Exoplanet Features")
plt.show()

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.histplot(df["Planet Mass (Earth masses)"], bins=30, kde=True, log_scale=True)
plt.xlabel("Planet Mass (Earth masses)")
plt.title("Distribution of Planet Mass")

plt.subplot(1, 2, 2)
sns.histplot(df["Planet Radius (Earth radii)"], bins=30, kde=True, log_scale=True)
plt.xlabel("Planet Radius (Earth radii)")
plt.title("Distribution of Planet Radius")

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Planet Radius (Earth radii)", y="Planet Mass (Earth masses)", data=df)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Planet Radius (Earth radii)")
plt.ylabel("Planet Mass (Earth masses)")
plt.title("Exoplanet Mass vs. Radius")
plt.show()

print("Top 5 Largest Planets by Radius:")
print(df.nlargest(5, "Planet Radius (Earth radii)"))

print("\nTop 5 Smallest Planets by Radius:")
print(df.nsmallest(5, "Planet Radius (Earth radii)"))

print("\nTop 5 Most Massive Planets:")
print(df.nlargest(5, "Planet Mass (Earth masses)"))

print("\nTop 5 Least Massive Planets:")
print(df.nsmallest(5, "Planet Mass (Earth masses)"))

def classify_planet(row):
    if row["Planet Radius (Earth radii)"] < 2 and row["Planet Mass (Earth masses)"] < 10:
        return "Earth-like"
    elif 2 <= row["Planet Radius (Earth radii)"] < 10 and 10 <= row["Planet Mass (Earth masses)"] < 50:
        return "Super-Earth"
    elif 10 <= row["Planet Radius (Earth radii)"] < 20 and 50 <= row["Planet Mass (Earth masses)"] < 500:
        return "Neptune-like"
    else:
        return "Gas Giant"

df["Category"] = df.apply(classify_planet, axis=1)

print(df["Category"].value_counts())

print(df.groupby("Category")["Orbital Period (days)"].describe())

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.boxplot(x="Category", y="Orbital Period (days)", data=df)
plt.yscale("log")  # Log scale since periods range widely
plt.xlabel("Planet Category")
plt.ylabel("Orbital Period (days)")
plt.title("Orbital Period Distribution by Planet Type")
plt.show()
