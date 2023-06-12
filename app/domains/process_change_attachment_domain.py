from dataclasses import dataclass
from datetime import date


@dataclass
class ProcessChangeAttachmentDomain:
    description: str
    process_change_id: int
    document_kind_id: int
    created_at: date
