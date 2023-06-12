from sqlalchemy import Table, Column, Integer, String

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

office_permission_table = Table(
    "office_permission",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("level", Integer, nullable=False),
    Column("description", String(45), nullable=True),
)
