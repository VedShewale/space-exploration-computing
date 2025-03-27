import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create the Space Exploration folder if it doesn't exist
output_folder = "Space Exploration"
os.makedirs(output_folder, exist_ok=True)

def boxplot_mass_by_category(df):
    """Creates and saves a boxplot of planet mass distribution by category."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Category", y="Planet Mass (Earth masses)", data=df)
    plt.yscale("log")
    plt.xlabel("Planet Category")
    plt.ylabel("Planet Mass (Earth masses)")
    plt.title("Planet Mass Distribution by Category")
    plt.savefig(f"{output_folder}/planet_mass_boxplot.png")
    plt.show()

def scatter_mass_vs_radius(df):
    """Creates and saves a scatter plot with trend line for mass vs. radius."""
    plt.figure(figsize=(8, 6))
    sns.regplot(x="Planet Radius (Earth radii)", y="Planet Mass (Earth masses)", 
                data=df, logx=True, scatter_kws={"s": 10})
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Planet Radius (Earth radii)")
    plt.ylabel("Planet Mass (Earth masses)")
    plt.title("Mass vs. Radius with Trend Line")
    plt.savefig(f"{output_folder}/mass_radius_trend.png")
    plt.show()

def bar_chart_planet_types(df):
    """Creates and saves a bar chart for planet type distribution."""
    plt.figure(figsize=(8, 6))
    df["Category"].value_counts().plot(kind="bar", color=["blue", "green", "purple", "red"])
    plt.xlabel("Planet Category")
    plt.ylabel("Number of Planets")
    plt.title("Distribution of Planet Types")
    plt.xticks(rotation=45)
    plt.savefig(f"{output_folder}/planet_type_distribution.png")
    plt.show()

def heatmap_correlation(df):
    """Creates and saves a heatmap of the correlation matrix."""
    correlation_matrix = df.select_dtypes(include=['number']).corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")
    plt.savefig(f"{output_folder}/correlation_heatmap.png")
    plt.show()
