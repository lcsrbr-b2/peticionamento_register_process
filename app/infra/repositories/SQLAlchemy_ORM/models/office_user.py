from sqlalchemy import Table, Column, Integer, ForeignKey

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

office_user_table = Table(
    "office_user",
    metadata_obj,
    Column("office_id", Integer, ForeignKey("office.id")),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("office_permission_id", Integer, ForeignKey("office_permission.id")),
)
