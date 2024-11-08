from fastapi import APIRouter

from app.models.model_loader import load_model_and_transformer, predict_insurance_charges
from app.schemas.request_schemas import PredictRequest
from app.schemas.response_schemas import PredictResponse

router = APIRouter()
model, poly = load_model_and_transformer()


@router.post("/predict", response_model=PredictResponse, summary="Predict Insurance Cost", tags=["Prediction"])
async def predict_cost(data: PredictRequest):
    """
    Predicts the health insurance premium cost based on given parameters.

    - **smoker**: Boolean, True for smoker, False for non-smoker.
    - **bmi**: Body Mass Index as a float, typically between 0 and 100.
    - **age**: Age as a positive integer between 0 and 120.
    - **children**: Number of children as a non-negative integer.

    Returns the predicted insurance cost.
    """
    input_data = {
        "age": data.age,
        "bmi": data.bmi,
        "children": data.children,
        "smoker": data.smoker
    }
    predicted_charges = predict_insurance_charges(model, poly, input_data)

    return PredictResponse(cost_prediction=predicted_charges)
