from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive
import pandas as pd
import os

data_dir = "../data"
file_path = f"{data_dir}/exoplanets.csv"

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# NASA Exoplanet Archive API URL (Fetching only useful columns)
url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,pl_orbper,pl_rade,pl_bmasse+from+pscomppars&format=csv"

# Convert to Pandas DataFrame
df = pd.read_csv(url)

# Save to CSV
df.to_csv(file_path, index=False)

print(f"Fetched {len(df)} exoplanets and saved to {file_path}")
