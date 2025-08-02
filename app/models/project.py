import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

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

    created_by: int = Field(foreign_key="user.id")
    created_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.UTC)
    )

    updated_by: int = Field(foreign_key="user.id")
    updated_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.UTC)
    )