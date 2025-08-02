import datetime

from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.project import Project
from app.schemas.project import UpdateProjectRequest


async def update_project_handler(
        project_id: int,
        update_data: UpdateProjectRequest,
        session: Session,
        access_token: dict
):
    try:
        user_id = access_token.get("user_id")
        query = select(Project).where(Project.id == project_id)
        existing_project = session.exec(query).first()

        if not existing_project:
            raise HTTPException(status_code=404, detail="Project not found!")

        if update_data.project_name is not None:
            query = select(Project).where(Project.project_name == update_data.project_name)
            existing_project_name = session.exec(query).first()
            if existing_project_name:
                raise HTTPException(status_code=409, detail="A project exists with the same name!")

            existing_project.project_name = update_data.project_name

        if update_data.project_description is not None:
            existing_project.project_description = update_data.project_description

        existing_project.updated_at = datetime.datetime.now(datetime.UTC)
        existing_project.updated_by = user_id

        session.add(existing_project)
        session.commit()
        session.refresh(existing_project)

        return {
            "message": f"Project with id {project_id} updated successfully!"
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Could not update project! Exited with Exception: {e}"
        )