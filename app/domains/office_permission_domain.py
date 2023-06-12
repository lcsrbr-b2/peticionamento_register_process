from dataclasses import dataclass


@dataclass
class OfficePermissionDomain:
    level: int
    description: str
