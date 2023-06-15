from typing import Annotated
from fastapi import APIRouter, Depends
from app.basemodels.document_basemodels import DocumentInput
from app.services.document_service import DocumentService
from app.infra.repositories.SQLAlchemy_ORM.document_ORM import SQLAlchemyORM
from app.infra.repositories.SQLAlchemy_ORM.enviroment import session

router = APIRouter(
    prefix="/document",
    tags=["register-document"],
    responses={404: {"description": "Not found"}},
)


# DI
def get_service():
    """_summary_

    Returns:
        _type_: _description_
    """
    return DocumentService(SQLAlchemyORM(session()))


@router.post("/register")
async def register(
    document: DocumentInput,
    service: Annotated[DocumentService, Depends(get_service)],
):
    """_summary_

    Args:
        document (DocumentInput): _description_
        service (Annotated[DocumentService, Depends): _description_

    Returns:
        _type_: _description_
    """
    return service.register(document)

