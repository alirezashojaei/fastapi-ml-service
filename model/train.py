import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import argparse
import os


def train_model(data_path, model_path=None, degree=2, model_output_path='polynomial_regression_model.pkl',
                transformer_output_path='polynomial_features.pkl'):
    # Load dataset
    df = pd.read_csv(data_path)

    # Encode categorical features
    label = LabelEncoder()
    df['sex'] = label.fit_transform(df['sex'])
    df['smoker'] = label.fit_transform(df['smoker'])
    df['region'] = label.fit_transform(df['region'])

    # Select features and target
    X = df.drop(['charges', 'sex', 'region'], axis=1)  # dropping non-numeric features as indicated
    y = df['charges']

    # Apply polynomial transformation
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=0)

    # Load model if path is provided, else train a new model
    if model_path and os.path.exists(model_path):
        model = joblib.load(model_path)
        print(f"Loaded model from {model_path} for fine-tuning.")
    else:
        model = LinearRegression()
        print("Training a new model.")

    # Fit model
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Evaluation metrics
    print("Training Data Evaluation:")
    print("Score: ", model.score(X_test, y_test))
    print(f"Mean Absolute Error: {mean_absolute_error(y_train, y_train_pred):.2f}")
    print(f"Mean Squared Error: {mean_squared_error(y_train, y_train_pred):.2f}")
    print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_train, y_train_pred)):.2f}\n")

    print("Testing Data Evaluation:")
    print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_test_pred):.2f}")
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_test_pred):.2f}")
    print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_test, y_test_pred)):.2f}")

    # Save the model and polynomial features transformer
    joblib.dump(model, model_output_path)
    joblib.dump(poly, transformer_output_path)
    print("Model and transformer saved successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train or fine-tune a polynomial regression model.")
    parser.add_argument('data_path', type=str, help="Path to the CSV data file.")
    parser.add_argument('--model_path', type=str, default=None,
                        help="Path to an existing model for fine-tuning. If not provided, a new model will be trained.")
    parser.add_argument('--degree', type=int, default=2, help="Degree of the polynomial features. Default is 2.")
    parser.add_argument('--model_output_path', type=str, default='polynomial_regression_model.pkl',
                        help="Path to save the trained or fine-tuned model.")
    parser.add_argument('--transformer_output_path', type=str, default='polynomial_features.pkl',
                        help="Path to save the polynomial transformer.")

    args = parser.parse_args()

    # Ensure data path exists
    if not os.path.exists(args.data_path):
        raise FileNotFoundError(f"The specified data file does not exist: {args.data_path}")

    # Train the model (or fine-tune if a model path is provided)
    train_model(
        data_path=args.data_path,
        model_path=args.model_path,
        degree=args.degree,
        model_output_path=args.model_output_path,
        transformer_output_path=args.transformer_output_path
    )
