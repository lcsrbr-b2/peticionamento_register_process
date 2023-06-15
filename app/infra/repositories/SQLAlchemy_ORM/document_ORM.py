from sqlalchemy import select, insert
from app.infra.repositories.SQLAlchemy_ORM.models.process_change import process_change_table
from app.infra.repositories.SQLAlchemy_ORM.models.document_type import document_type_table
from app.infra.repositories.SQLAlchemy_ORM.models.document import document_table
from app.domains.document_domain import DocumentDomain

from app.domains.repositories.document_repository import DocumentRepository

class SQLAlchemyORM(DocumentRepository):
    """_summary_

    Args:
        DocumentRepository (_type_): _description_
    """
    def __init__(self, session):
        self.session = session

    def find_process_change_by_id(self, process_change_id: int):
        result = self.session.execute(select(process_change_table).filter_by(id=process_change_id))
        return result.mappings().first()

    def register_document_type(self, document_type: str):
        inserted = self.session.execute(insert(document_type_table).values(name=document_type))
        self.session.commit()
        return inserted.inserted_primary_key[0]

    def get_document_type_id(self, document_type: str):
        result = self.session.execute(select(document_type_table).filter_by(
            name=document_type))
        return result.mappings().first()

    def find_document_by_id(self, document_id: int):
        result = self.session.execute(select(document_table).filter_by(id=document_id))
        return result.mappings().first()

    def get_process_change_id(self, process_change: str):
        result = self.session.execute(select(process_change_table).filter_by(process_change_number=process_change))
        return result.mappings().first()
    
    def register_document(self, document: DocumentDomain):
        # document_data = {
        #     "description": document_info.description,
        #     "number_document": document_info.number_document,
        #     "address": document_info.address,
        #     "process_change_id": process_change_id,
        #     "document_type_id": document_type_id,
        #     "created_at": datetime.datetime.now(),
        #     "level": document_info.level
        #         }
        inserted = self.session.execute(insert(document_table).values(
            description=document["description"],
            number_document=document["number_document"],
            address=document["address"],
            process_change_id=document["process_change_id"],
            document_type_id=document["document_type_id"],
            created_at=document["created_at"],
            level=document["level"]
        ))
        self.session.commit()
        return inserted.inserted_primary_key[0]
