from fastapi import HTTPException
from passlib.context import CryptContext
from sqlmodel import Session, select

from app.controllers.auth.tokens_controller import create_access_token
from app.models.user import User

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


async def login_handler(
        user_name: str,
        password: str,
        session: Session
):
    try:
        query = select(User).where(User.user_name == user_name)
        result = session.exec(query)
        user = result.first()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized!"
            )

        if not pwd_context.verify(password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        access_token = create_access_token(
            user.id,
            user.user_name,
            user.user_role
        )

        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Something went wrong! Exited with Exception {e}"
        )