from fastapi import APIRouter, HTTPException
from app.db_control.crud_user import create_user
from app.schemas.request_schemas import UserCreate
from app.schemas.response_schemas import UserResponse

router = APIRouter()


@router.post("/create", response_model=UserResponse, status_code=201)
async def create_user_endpoint(user_data: UserCreate):
    """
    Endpoint to create a new user.
    """
    try:
        user = create_user(
            name=user_data.name,
            email=user_data.email,
            age=user_data.age
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return user
