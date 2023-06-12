from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

process_change_table = Table("process_change", metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("process_change_number", String(45), nullable=False),
    Column("process_id", ForeignKey("process.id"), nullable=False),
    Column("process_change_type_id", ForeignKey("process_change_type.id"), nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("deadline", String(45), nullable=True),
    Column("status", Integer, nullable=False),
    )
