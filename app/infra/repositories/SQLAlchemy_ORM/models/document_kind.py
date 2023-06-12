from sqlalchemy import Table, Column, Integer, String

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

document_kind_table = Table("document_kind", metadata_obj,
                            Column("id", Integer, primary_key=True, autoincrement=True),
                            Column("name", String(255), nullable=True)
                            )
