import datetime
from app.basemodels.document_basemodels import DocumentInput
from app.domains.repositories.document_repository import (
    DocumentRepository
)


class DocumentService:
    """_summary_"""

    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    def register(self, document: DocumentInput):
        """_summary_

        Args:
            document (DocumentInput): _description_

        Returns:
            _type_: _description_
        """
        process_change_id = self.repository.get_process_change_id(document.number_process_change)
        process_change_id = process_change_id.id

        documents = []

        for document_info in document.documents:

            document_type_id = self.repository.get_document_type_id(document_info.description)
            if document_type_id is None:
                document_type_id = self.repository.register_document_type(document_info.description)
            else:
                document_type_id = document_type_id.id

            document_data = {
                "description": document_info.description,
                "number_document": document_info.number_document,
                "address": document_info.address,
                "process_change_id": process_change_id,
                "document_type_id": document_type_id,
                "created_at": datetime.datetime.now(),
                "level": document_info.level
                }

            document_id = self.repository.register_document(document_data)
            documents.append(self.repository.find_document_by_id(document_id))

        return documents
