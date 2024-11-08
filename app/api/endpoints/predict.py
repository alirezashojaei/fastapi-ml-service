from fastapi import APIRouter
from app.schemas.request_schemas import PredictRequest
from app.schemas.response_schemas import PredictResponse

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
async def predict_cost(data: PredictRequest):
    """
    Predict the health insurance premium cost based on user details.
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
