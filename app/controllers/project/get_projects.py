from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.project import Project


async def get_projects_handler(
        session: Session
):
    try:
        query = select(Project)
        projects = session.exec(query).all()

        return projects

    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not fetch projects!")
