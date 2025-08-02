from typing import Optional

from pydantic import BaseModel, Field, field_validator


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

    @field_validator(
        "project_name",
        "project_description"
    )
    def remove_leading_or_trailing_spaces(
            cls,
            v: str
    ) -> str:
        return v.strip()


class CreateProjectRequest(ProjectBase):
    pass


class UpdateProjectRequest(BaseModel):
    project_name: Optional[str] = Field(None, min_length=4)
    project_description: Optional[str] = Field(None, min_length=5)

    @field_validator(
        "project_name",
        "project_description"
    )
    def remove_leading_or_trailing_spaces(
            cls,
            v: Optional[str]
    ) -> Optional[str]:
        return v.strip() if v is not None else None
