from typing import Optional

from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    project_name: str = Field(
        ...,
        min_length=4,
        description="Your project's title"
    )
    project_description: str = Field(
        ...,
        min_length=5,
        description="Your project's description"
    )


class CreateProjectRequest(ProjectBase):
    pass


class UpdateProjectRequest(BaseModel):
    project_name: Optional[str] = Field(None, min_length=4)
    project_description: Optional[str] = Field(None, min_length=5)
