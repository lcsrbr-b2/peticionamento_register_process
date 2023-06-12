from dataclasses import dataclass


@dataclass
class OfficeUserDomain:
    office_id: int
    user_id: int
    office_permission_id: int
