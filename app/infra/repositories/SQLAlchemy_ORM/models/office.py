from sqlalchemy import Table, Column, Integer, String

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

office_table = Table(
    "office",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("cnpj", String(16), nullable=False),
)
