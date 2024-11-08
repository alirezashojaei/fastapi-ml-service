# Polynomial Regression Model for Insurance Charges Prediction

## Requirements

Ensure you have the following Python libraries installed:
- `pandas`
- `numpy`
- `scikit-learn`
- `joblib`


## Dataset Description

The dataset used in this project is an **insurance dataset** containing information about individual insurance policyholders. The goal is to predict the insurance charges based on various factors such as age, BMI, and smoking status. 

### Features

| Column      | Description                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------|
| `age`       | Age of the individual (numeric).                                                                |
| `sex`       | Gender of the individual (`male` or `female`).                                                  |
| `bmi`       | Body Mass Index of the individual, a measure of body fat based on height and weight (numeric).  |
| `children`  | Number of children/dependents covered by the insurance (numeric).                               |
| `smoker`    | Smoking status of the individual (`yes` or `no`).                                               |
| `region`    | Region where the individual resides (`northeast`, `northwest`, `southeast`, `southwest`).       |
| `charges`   | The target variable, representing the medical insurance charges billed to the individual.       |

### Target

- `charges`: The amount billed to the individual, which is the target variable we are predicting. This is a continuous numeric variable.

## Usage

The main training script is `train.py`. You can use it to train a new model or fine-tune an existing one.

### Arguments

| Argument                  | Type    | Description                                                                                   |
|---------------------------|---------|-----------------------------------------------------------------------------------------------|
| `data_path`               | string  | Required. Path to the CSV data file.                                                          |
| `--model_path`            | string  | Optional. Path to an existing model file for fine-tuning.                                     |
| `--degree`                | integer | Optional. Degree of the polynomial features (default is 2).                                   |
| `--model_output_path`     | string  | Optional. Path to save the trained or fine-tuned model (default is `polynomial_regression_model.pkl`). |
| `--transformer_output_path` | string | Optional. Path to save the polynomial transformer (default is `polynomial_features.pkl`). |

### Training a New Model

To train a new polynomial regression model on your dataset, run:

```bash
python train.py <data_path> --degree <degree> --model_output_path <model_output_path>
```

**Example**:

```bash
python train.py data/insurance.csv --degree 3 --model_output_path models/new_polynomial_model.pkl
```

### Fine-Tuning an Existing Model

To fine-tune an existing model, specify the path to the model you want to update:

```bash
python train.py <data_path> --model_path <existing_model_path> --degree <degree>
```

**Example**:

```bash
python train.py data/insurance.csv --model_path models/existing_polynomial_model.pkl --degree 2
```

## Source: 

https://www.kaggle.com/code/mariapushkareva/medical-insurance-cost-with-linear-regression
