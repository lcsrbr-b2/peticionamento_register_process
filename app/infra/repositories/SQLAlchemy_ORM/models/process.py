from sqlalchemy import Table, Column, Integer, String, ForeignKey

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

process_table = Table(
    "process",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("system", String(45), nullable=False),
    Column("system_version", String(45), nullable=False),
    Column("office", String(45), nullable=False),
    Column("process_number", String(45)),
    Column("tribunal_id", ForeignKey("tribunal.id"), nullable=False),
    Column(
        "office_user_office_id", ForeignKey("office_user.office_id"), nullable=False
    ),
    Column("office_user_user_id", ForeignKey("office_user.user_id"), nullable=False),
    Column(
        "office_user_office_permission_id",
        ForeignKey("office_user.office_permission_id"),
        nullable=False,
    ),
    Column("process_type_id", ForeignKey("process_type.id"), nullable=False),
)
