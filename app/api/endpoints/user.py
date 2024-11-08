from fastapi import APIRouter, HTTPException
from app.db_control.crud_user import create_user, get_user_by_id, update_user, delete_user
from app.schemas.request_schemas import UserCreate, UserUpdate
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


@router.get("/{user_id}", response_model=UserResponse)
async def get_user_endpoint(user_id: int):
    """
    Endpoint to retrieve a user by ID.
    """
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user_endpoint(user_id: int, user_data: UserUpdate):
    """
    Endpoint to update an existing user's details.
    """
    user = update_user(
        user_id=user_id,
        name=user_data.name,
        email=user_data.email,
        age=user_data.age
    )
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=204)
async def delete_user_endpoint(user_id: int):
    """
    Endpoint to delete a user by ID.
    """
    result = delete_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
