import pandas as pd
from dashboard import boxplot_mass_by_category, scatter_mass_vs_radius, bar_chart_planet_types, heatmap_correlation
from data_processing import load_data, add_planet_category
from predict import predict_exoplanet
from habitability import predict_habitability, main, get_user_input

df = pd.read_csv("data/exoplanets.csv")

# Load and clean the data
df = load_data()

# Add planet category
df = add_planet_category(df)

# Call visualization functions
boxplot_mass_by_category(df)
scatter_mass_vs_radius(df)
bar_chart_planet_types(df)
heatmap_correlation(df)

#Predictions for Planet Type
predict_exoplanet()

#Prediction for habitability
main()