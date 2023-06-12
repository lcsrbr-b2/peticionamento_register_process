from sqlalchemy import Table, Column, Integer, String, ForeignKey

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

attorney_table = Table(
    "attorney",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(45), nullable=False),
    Column("oab_number", String(45), nullable=False),
    Column("process_id", ForeignKey("process.id"), nullable=False),
)
