from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int]


class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]


class PredictRequest(BaseModel):
    smoker: bool = Field(..., description="Indicates if the person is a smoker")
    bmi: float = Field(..., ge=0, le=100, description="Body Mass Index, between 0 and 100")
    age: int = Field(..., ge=0, le=120, description="Age in years, between 0 and 120")
    children: int = Field(..., ge=0, description="Number of children (0 or more)")
