from sqlalchemy import Table, Column, Integer, String, ForeignKey

from app.infra.repositories.SQLAlchemy_ORM.enviroment import metadata_obj

process_part_table = Table("process_part", metadata_obj,
                           Column("id", Integer, primary_key=True, autoincrement=True),
                           Column("process_id", ForeignKey("process.id"), nullable=False),
                           Column("cpf_cnpj", String(45), nullable=False),
                           Column("name", String(45)),
                           Column("role", Integer, nullable=False)
                           )
