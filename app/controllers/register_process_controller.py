from typing import Annotated
from fastapi import APIRouter, Depends
from app.controllers.basemodels.register_process_basemodels import RegisterProcessInput
from app.controllers.basemodels.register_process_basemodels import StandardOutput
from app.services.register_process_service import RegisterProcessService
from app.infra.repositories.SQLAlchemy_ORM.register_process_ORM import SQLAlchemyORM
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
    return RegisterProcessService(SQLAlchemyORM(session()))


@router.post("/register")
async def register(
    process: RegisterProcessInput,
    service: Annotated[RegisterProcessService, Depends(get_service)],
):
    """_summary_

    Args:
        process (RegisterProcessInput): _description_
        service (Annotated[UserService, Depends): _description_

    Returns:
        _type_: _description_
    """

    register_id = service.register(process)
    return StandardOutput(status="OK", id=register_id)
