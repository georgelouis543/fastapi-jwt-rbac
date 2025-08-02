from fastapi import HTTPException
from sqlmodel import Session, select

from app.controllers.auth.hash_pwd_controller import hash_password
from app.models.user import User
from app.schemas.user import CreateUserRequest


async def register_user_handler(
        user_request: CreateUserRequest,
        session: Session
):
    try:
        # Check for existing User!
        query = select(User).where(
            User.user_name == user_request.user_name
        )
        is_existing_user = session.exec(query).first()

        if is_existing_user:
            raise HTTPException(
                status_code=409,
                detail="Username already exists."
            )

        hashed_pw = hash_password(user_request.password)

        user = User(
            user_name=user_request.user_name,
            hashed_password=hashed_pw,
            user_role=user_request.user_role
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        return {
            "id": user.id,
            "user_name": user.user_name,
            "user_role": user.user_role
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Something went wrong! Exited with Exception {e}"
        )