from dataclasses import dataclass


@dataclass
class AttorneyDomain:
    process_id: int
    name: str
    oab_number: str
