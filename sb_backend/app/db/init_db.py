from sqlalchemy.orm import Session

from ..crud.user import crud_user
from ..models.users.user import UserCreate
from ...config.application import settings
# from sqlmodel import SQLModel
# from ..db.session import engine

# make sure all SQL Alchemy schemas are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # SQLModel.metadata.create_all(bind=engine)

    user = crud_user.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud_user.user.create(db, obj_in=user_in)  # noqa: F841
