from sqlalchemy import Table, Column, Integer, String

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

tribunal_table = Table(
    "tribunal",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("instance", String(45), nullable=False),
    Column("uf", String(45), nullable=False),
)
