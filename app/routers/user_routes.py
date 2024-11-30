"""Routes for user management."""

from typing import Any
from fastapi import HTTPException
from app.db.firestore import db
from app.schemas.user_schema import User
from app.routers.api_router import router


# Add a new user
@router.post("/add_users")
def create_user(user: User) -> dict[str, Any]:
    """Add a new user to Firestore."""

    users_collection = db.collection("employee")
    user_id = users_collection.document().id
    user_data = user.dict(exclude_unset=True)
    users_collection.document(user_id).set(user_data)
    return {"user_id": user_id, **user_data}


# Retrieve all users
@router.get("/get_users")
def get_users() -> dict[str, list[dict[str, Any]]]:
    """Retrieve all users from Firestore."""
    users_collection = db.collection("employee")
    users = [doc.to_dict() for doc in users_collection.stream()]
    return {"users": users}


@router.patch("/update_users/{user_id}")
def update_user(user_id: int, user: User) -> dict[str, Any]:
    """
    Update user details by user_id (integer).

    Args:
        user_id (int): The unique ID of the user.
        user (User): The updated user data.
    """
    users_collection = db.collection("employee")

    # Query Firestore to find the document with the matching user_id
    query = users_collection.where("id", "==", user_id).limit(1).stream()

    doc = next((doc for doc in query), None)  # Get the first matching document
    if not doc:
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )

    # Update the document with the new data
    doc_ref = users_collection.document(doc.id)
    doc_ref.update(user.dict(exclude_unset=True))

    return {
        "user_id": user_id,
        "updated_data": user.dict(exclude_unset=True),
    }


@router.delete("/delete_users/{user_id}")
def delete_user(user_id: int) -> dict[str, str]:
    """
    Deletes a user from Firestore based on their integer user_id.

    Args:
        user_id (int): The unique ID of the user to delete.

    Returns:
        dict: A confirmation message upon successful deletion.
    """
    users_collection = db.collection("employee")

    # Query Firestore to find the document with the matching user_id
    query = users_collection.where("id", "==", user_id).limit(1).stream()

    # Get the first matching document
    doc = next((doc for doc in query), None)
    if doc is None:
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )

    # Delete the document using its reference
    doc.reference.delete()

    return {"detail": f"User with ID {user_id} has been deleted"}



