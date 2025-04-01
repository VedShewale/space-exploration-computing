# Exoplanet Habitability Prediction

This project predicts the habitability of exoplanets based on their physical characteristics, such as radius, mass, and orbital period. It utilizes machine learning models, including a Random Forest Classifier, to classify planets as habitable or not. The project includes data visualization, model training, and prediction functionalities.

## Features

- **Exoplanet Classification**: Classifies exoplanets into categories based on their physical characteristics.
- **Habitability Prediction**: Predicts whether an exoplanet is habitable (1: habitable, 0: not habitable) based on radius and mass.
- **Data Visualizations**: Provides various graphs to visualize the relationship between planet features and their classifications.
- **Machine Learning Models**: Trains and saves models for classification and habitability prediction.

## Project Structure

- **src/**: Contains the main code for the project.
  - `ai_model.py`: Defines and trains the machine learning models.
  - `habitability_check.py`: Script for assigning habitability to a dataset.
  - `habitability.py`: Code for predicting habitability based on input data.
  - `analyze_exoplanets.py`: Main script for analyzing exoplanet data and making predictions.
  - `data_processing.py`: Functions for loading and processing the data.
  - `predict.py`: Prediction functions for exoplanet classification.

- **data/**: Directory containing exoplanet data files in CSV format.
- **models/**: Directory where trained models are saved (e.g., `exoplanet_classifier.pkl` and `habitability_classifier.pkl`).
- **notebooks/**: Jupyter notebooks for exploring and analyzing the data interactively (optional).

## Requirements

To run this project, you'll need the following dependencies:

- pandas
- numpy
- scikit-learn
- matplotlib
- joblib

You can install them using `pip`:

```bash
pip install -r requirements.txt
```
## How to Use
- **Data Preprocessing:** The load_data() function loads and processes exoplanet data, ensuring the necessary columns (such as radius and mass) are available and cleaned.

- **Model Training:** Run ai_model.py to train the classification and habitability prediction models. The models are saved to the models/ directory as .pkl files.

- **Example:**
```bash
python src/ai_model.py
```
## Prediction:

- To predict the habitability of an exoplanet, run the habitability.py file and provide input values for the planet's radius and mass.

- **Example:**
```bash
python src/habitability.py
```

## Analyze Exoplanets:

- Run the analyze_exoplanets.py script to visualize and make predictions for exoplanets using the trained models. This script will also generate graphs and display them using Matplotlib.

- **Example:**
```bash
python src/analyze_exoplanets.py
```

# Example Usage

After running analyze_exoplanets.py, you'll be able to see various visualizations and make predictions about the habitability of exoplanets using input values for their radius and mass.
```python
radius = 1.2  # Example planet radius (in Earth radii)
mass = 2.1    # Example planet mass (in Earth masses)

habitability = predict_habitability(habitability_model, radius, mass)
print(f"Predicted Habitability: {habitability}")
```

# Future Improvements
- Implement additional features (e.g., orbital period, star type) for more accurate predictions.

- Experiment with other machine learning models and fine-tune hyperparameters.

- Add more comprehensive data preprocessing and error handling.

# License
- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
