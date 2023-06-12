from sqlalchemy import Table, Column, Integer, String

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

user_table = Table(
    "user",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("firstname", String(45), nullable=False),
    Column("lastname", String(45), nullable=False),
    Column("oab_number", String(45), nullable=True),
    Column("specialization", String(255), nullable=True),
)
