from typing import Optional

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

    class Config:
        orm_mode = True
