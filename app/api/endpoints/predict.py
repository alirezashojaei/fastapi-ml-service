from fastapi import APIRouter
from app.schemas.request_schemas import PredictRequest
from app.schemas.response_schemas import PredictResponse

router = APIRouter()


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
    # Mock prediction logic for demonstration purposes
    base_cost = 1000.0
    age_factor = data.age * 20.0
    bmi_factor = data.bmi * 10.0
    smoker_factor = 500.0 if data.smoker else 0.0
    children_factor = data.children * 200.0

    # Calculate the prediction
    cost_prediction = base_cost + age_factor + bmi_factor + smoker_factor + children_factor

    return PredictResponse(cost_prediction=cost_prediction)
