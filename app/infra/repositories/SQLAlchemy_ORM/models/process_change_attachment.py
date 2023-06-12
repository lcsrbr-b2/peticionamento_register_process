from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func


from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

process_change_attachment_table = Table("process_change_attachment", metadata_obj,
                                 Column("id", Integer, primary_key=True, autoincrement=True),
                                 Column("description", String(45)),
                                 Column("process_change_id", ForeignKey("process_change.id"), nullable=False),
                                 Column("document_kind_id", ForeignKey("document_kind.id"), nullable=False),
                                 Column("created_at", DateTime(timezone=True), server_default=func.now()),
                                 Column("tribunal", String(45))
                                 )
