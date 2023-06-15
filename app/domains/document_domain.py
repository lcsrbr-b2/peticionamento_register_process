from dataclasses import dataclass
from datetime import date


@dataclass
class DocumentDomain:
    description: str
    number_document: str
    address: str
    process_change_id: int
    document_type_id: int
    level: str
