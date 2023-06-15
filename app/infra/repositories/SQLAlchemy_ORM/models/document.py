from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func


from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

document_table = Table("document", metadata_obj,
                                Column("id", Integer, primary_key=True, autoincrement=True),
                                Column("description", String(45)),
                                Column("number_document", String(45)),
                                Column("address", String(45)),
                                Column("process_change_id", ForeignKey("process_change.id"), nullable=False),
                                Column("document_type_id", ForeignKey("document_type.id"), nullable=False),
                                Column("created_at", DateTime(timezone=True), server_default=func.now()),
                                Column("level", String(45))
                                )
