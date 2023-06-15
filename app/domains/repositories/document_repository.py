from abc import ABC, abstractmethod
from app.domains.document_type_domain import DocumentTypeDomain
from app.domains.document_domain import DocumentDomain

class DocumentRepository(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def find_process_change_by_id(self, process_change_id: int):
        ...

    @abstractmethod
    def register_document_type(self, document_type: DocumentTypeDomain):
        ...

    @abstractmethod
    def get_document_type_id(self, document_type_id: DocumentTypeDomain):
        ...

    @abstractmethod
    def find_document_by_id(self, document_id: int):
        ...

    @abstractmethod
    def register_document(self, document: DocumentDomain):
        ...

    @abstractmethod
    def get_process_change_id(self, process_change: str):
        ...
