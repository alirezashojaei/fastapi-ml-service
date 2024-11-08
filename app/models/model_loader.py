import os
from typing import Tuple
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def load_model_and_transformer(model_path: str =
                               f'{os.path.dirname(os.path.abspath(__file__))}/polynomial_regression_model.pkl',
                               transformer_path: str =
                               f'{os.path.dirname(os.path.abspath(__file__))}/polynomial_features.pkl') -> Tuple[
                                LinearRegression, PolynomialFeatures]:
    """
    Loads the pre-trained model and polynomial features transformer.

    Parameters:
        model_path (str): Path to the pre-trained model file.
        transformer_path (str): Path to the polynomial features transformer file.

    Returns:
        Tuple[LinearRegression, PolynomialFeatures]: The loaded regression model and transformer.
    """
    model = joblib.load(model_path)
    poly = joblib.load(transformer_path)
    return model, poly


def predict_insurance_charges(model: LinearRegression, poly: PolynomialFeatures, input_data: dict) -> float:
    """
    Predicts insurance charges based on input data.

    Parameters:
        model (LinearRegression): Trained regression model for predictions.
        poly (PolynomialFeatures): Polynomial features transformer to preprocess input data.
        input_data (dict): Dictionary containing input features for a single prediction, with keys:
                           - 'age' (int): Age of the individual.
                           - 'bmi' (float): Body Mass Index.
                           - 'children' (int): Number of children/dependents.
                           - 'smoker' (bool): Smoking status.

    Returns:
        float: Predicted insurance charges.
    """

    df = pd.DataFrame([input_data])
    df['smoker'] = 1 if df['smoker'][0] else 0
    x_poly = poly.transform(df)
    prediction = model.predict(x_poly)

    return float(prediction[0])
