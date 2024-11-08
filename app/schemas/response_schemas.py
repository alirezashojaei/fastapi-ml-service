from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int]

    class Config:
        orm_mode = True


class PredictResponse(BaseModel):
    cost_prediction: float = Field(..., description="Predicted health insurance premium cost")
