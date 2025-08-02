import os
from dotenv import load_dotenv
from sqlmodel import (
    SQLModel,
    Session,
    create_engine
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")


engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_size=20,
    max_overflow=20,
    pool_timeout=60,
)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session