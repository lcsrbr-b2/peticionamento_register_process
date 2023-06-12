from dataclasses import dataclass


@dataclass
class ProcessChange:
    """_summary_

    Args:
    (_type_): _description_
    """

    process_change_number: str
    process_change_type: str
    deadline: str
    status: int


@dataclass
class Process:
    """_summary_

    Args:
    (_type_): _description_
    """

    system: str
    system_version: str
    office: str
    process_number: str
    process_type: str
    tribunal: dict[str, str]
    attorney: dict[str, str]
    client: dict[str, str, str]
    process_changes: list[ProcessChange]


@dataclass
class RegisterProcessDomain:
    """_summary_

    Args:
    (_type_): _description_
    """

    status: str
    data: dict[Process]
