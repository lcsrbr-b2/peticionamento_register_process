from typing import Annotated
from fastapi import APIRouter, Depends
from app.basemodels.process_basemodels import RegisterProcessInput
from app.services.process_service import ProcessService
from app.infra.repositories.SQLAlchemy_ORM.process_ORM import SQLAlchemyORM
from app.infra.repositories.SQLAlchemy_ORM.enviroment import session

router = APIRouter(
    prefix="/process",
    tags=["register-process"],
    responses={404: {"description": "Not found"}},
)


# DI
def get_service():
    """_summary_

    Returns:
        _type_: _description_
    """
    return ProcessService(SQLAlchemyORM(session()))


@router.post("/register")
async def register(
    process: RegisterProcessInput,
    service: Annotated[ProcessService, Depends(get_service)],
):
    """_summary_

    Args:
        process (RegisterProcessInput): _description_
        service (Annotated[UserService, Depends): _description_

    Returns:
        _type_: _description_
    """

    return service.register(process)

