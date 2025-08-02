from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.project import Project
from app.schemas.project import CreateProjectRequest


async def create_project_handler(
        access_token: dict,
        project_data: CreateProjectRequest,
        session: Session
):
    try:
        user_id = access_token.get("user_id")

        query = select(Project).where(
            (Project.created_by == user_id) & (Project.project_name == project_data.project_name)
        )
        is_existing_project = session.exec(query).first()

        if is_existing_project:
            raise HTTPException(
                status_code=409,
                detail="A project with the same title exists for this user!"
            )

        project = Project(
            project_name=project_data.project_name,
            project_description=project_data.project_description,
            created_by=user_id,
            updated_by=user_id
        )

        session.add(project)
        session.commit()
        session.refresh(project)

        return {
            "id": project.id,
            "project_name": project.project_name,
            "project_description": project.project_description
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Could not create Project! Exception {e} occurred")