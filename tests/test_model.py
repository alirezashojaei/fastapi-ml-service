import pytest
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from unittest.mock import Mock, patch

from app.models.model_loader import load_model_and_transformer, predict_insurance_charges

# Sample input data for testing
sample_input_data = {
    "age": 29,
    "bmi": 27.5,
    "children": 1,
    "smoker": True
}


@pytest.fixture
def load_test_model():
    """Fixture to load the model and transformer for testing."""
    model, poly = load_model_and_transformer()
    return model, poly


def test_load_model_and_transformer(load_test_model):
    """Test if the model and transformer are loaded correctly."""
    model, poly = load_test_model
    assert isinstance(model, LinearRegression), "Loaded model is not a LinearRegression instance"
    assert isinstance(poly, PolynomialFeatures), "Loaded transformer is not a PolynomialFeatures instance"


def test_predict_insurance_charges(load_test_model):
    """Test the prediction function with sample input data."""
    model, poly = load_test_model

    # Run prediction
    predicted_charges = predict_insurance_charges(model, poly, sample_input_data)

    # Check that the output is a float
    assert isinstance(predicted_charges, float), "Prediction output is not a float"
    assert predicted_charges >= 0, "Predicted insurance charges should be non-negative"


@patch('app.models.model_loader.load_model_and_transformer')
def test_predict_insurance_charges_mocked(mock_load_model):
    """Test prediction with a mocked model and transformer."""
    # Create a mock model and transformer
    mock_model = Mock(spec=LinearRegression)
    mock_transformer = Mock(spec=PolynomialFeatures)

    # Mock the transform and predict methods
    mock_transformer.transform.return_value = [[1, 2, 3, 4]]
    mock_model.predict.return_value = [1234.56]

    # Set the mocked model and transformer
    mock_load_model.return_value = (mock_model, mock_transformer)

    # Run prediction with mocked objects
    predicted_charges = predict_insurance_charges(mock_model, mock_transformer, sample_input_data)

    # Assert that the mocked predict method was called and returns the expected result
    mock_transformer.transform.assert_called_once()
    mock_model.predict.assert_called_once()
    assert predicted_charges == 1234.56, "Mocked prediction did not return expected result"
