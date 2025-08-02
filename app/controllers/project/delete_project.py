from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.project import Project


async def delete_project_handler(
        project_id: int,
        session: Session
):
    try:
        query = select(Project).where(Project.id == project_id)
        project = session.exec(query).first()

        if not project:
            raise HTTPException(
                status_code=404,
                detail="Project not found!"
            )

        session.delete(project)
        session.commit()

        return {
            "message": f"Project with id {project_id} deleted successfully."
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="Could not delete project!")