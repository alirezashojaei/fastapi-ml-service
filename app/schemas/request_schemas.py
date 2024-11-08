from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    age: int = None
