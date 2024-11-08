from pydantic import BaseModel, EmailStr
from typing import Optional


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int]

    class Config:
        orm_mode = True
