from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.config.database import get_session
from app.controllers.project.create_project_controller import create_project_handler
from app.controllers.project.delete_project import delete_project_handler
from app.controllers.project.get_projects import get_projects_handler
from app.controllers.project.update_project_controller import update_project_handler
from app.middleware.verify_jwt import verify_access_token
from app.middleware.verify_roles import verify_user_role
from app.schemas.project import CreateProjectRequest, UpdateProjectRequest

router = APIRouter(
    prefix="/project",
    tags=["project"]
)


@router.get("")
async def root() -> dict:
    return {"message": "Projects' Routes"}


@router.get("/projects")
async def get_all_projects(
        verified_token: dict = Depends(verify_access_token),
        session: Session = Depends(get_session)
):
    verify_user_role(verified_token, ["admin", "user"])
    result = await get_projects_handler(session)
    return result


@router.post("/create-project")
async def create_project(
        project_request: CreateProjectRequest,
        verified_token: dict = Depends(verify_access_token),
        session: Session = Depends(get_session)
):
    verify_user_role(verified_token, ["admin"])
    result = await create_project_handler(
        verified_token,
        project_request,
        session
    )
    return result


@router.delete("/delete-project/{project_id}")
async def delete_single_project(
        project_id: int,
        verified_token: dict = Depends(verify_access_token),
        session: Session = Depends(get_session)
):
    verify_user_role(verified_token, ["admin"])
    result = await delete_project_handler(
        project_id,
        session
    )
    return result


@router.put("edit-project/{project_id}")
async def update_single_feed(
        project_id: int,
        update_data: UpdateProjectRequest,
        verified_token: dict = Depends(verify_access_token),
        session: Session = Depends(get_session)
):
    verify_user_role(verified_token, ["admin"])
    result = await update_project_handler(
        project_id,
        update_data,
        session,
        verified_token
    )
    return result