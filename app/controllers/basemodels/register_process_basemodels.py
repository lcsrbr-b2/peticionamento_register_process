from pydantic import BaseModel


class ProcessChange(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    process_change_number: str
    process_change_type: str
    deadline: str
    status: int


class Tribunal(BaseModel):
    uf: str
    instance: str


class Attorney(BaseModel):
    name: str
    oab: str


class Client(BaseModel):
    name: str
    client_doc: str
    role: str


class Process(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    system: str
    system_version: str
    office: str
    process_number: str
    process_type: str
    tribunal: Tribunal
    attorney: Attorney
    client: Client
    process_changes: list[ProcessChange]


class Data(BaseModel):
    process: Process


class RegisterProcessInput(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    status: str
    data: Data


class StandardOutput(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    status: str
    id: int
