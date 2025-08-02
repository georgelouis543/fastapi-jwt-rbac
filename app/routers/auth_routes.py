from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session

from app.config.database import get_session
from app.controllers.auth.login_controller import login_handler
from app.controllers.auth.register_user_controller import register_user_handler
from app.schemas.token import Token
from app.schemas.user import CreateUserRequest

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

oauth2_bearer = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


@router.get("")
async def root() -> dict:
    return {"message": "Auth Routes"}


@router.post("/register")
async def register_user(
        user_request: CreateUserRequest,
        session: Session = Depends(get_session)
):
    result = await register_user_handler(
        user_request,
        session
    )
    return result


@router.post(
    "/login",
    response_model=Token
)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_session)
):
    result = await login_handler(
        form_data.username,
        form_data.password,
        session
    )
    return result