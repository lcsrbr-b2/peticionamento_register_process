from pydantic import BaseModel


class Document(BaseModel):
    level: str
    number_document: str
    address: str
    description: str


class DocumentInput(BaseModel):
    status: str
    number_process: str
    number_process_change: str
    documents: list[Document]
