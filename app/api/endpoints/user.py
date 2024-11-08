from fastapi import APIRouter, HTTPException
from app.db_control.crud_user import create_user, get_user_by_id, update_user, delete_user
from app.schemas.request_schemas import UserCreate, UserUpdate
from app.schemas.response_schemas import UserResponse

router = APIRouter()


@router.post("/create", response_model=UserResponse, status_code=201, summary="Create a new user", tags=["User"])
async def create_user_endpoint(user_data: UserCreate):
    """
    Creates a new user in the system.

    - **name**: The user's full name.
    - **email**: The user's email address (must be a valid format).
    - **age**: The user's age (optional).
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


@router.get("/{user_id}", response_model=UserResponse, summary="Retrieve a user by ID", tags=["User"])
async def get_user_endpoint(user_id: int):
    """
    Retrieves a user by their unique ID.

    - **user_id**: The ID of the user you want to retrieve.
    """
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse, summary="Update a user's information", tags=["User"])
async def update_user_endpoint(user_id: int, user_data: UserUpdate):
    """
    Updates an existing user's details by ID.

    - **user_id**: The ID of the user you want to update.
    - **name**: Updated name of the user (optional).
    - **email**: Updated email of the user (optional).
    - **age**: Updated age of the user (optional).
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


@router.delete("/{user_id}", status_code=204, summary="Delete a user by ID", tags=["User"])
async def delete_user_endpoint(user_id: int):
    """
    Deletes a user by their unique ID.

    - **user_id**: The ID of the user you want to delete.
    """
    result = delete_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
