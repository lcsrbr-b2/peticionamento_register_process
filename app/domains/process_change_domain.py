from dataclasses import dataclass
from datetime import date


@dataclass
class ProcessChangeDomain:
    process_change_number: int
    process_id: int
    process_change_type_id: int
    created_at: date
    deadline: str
    status: int

    # def process_status(self):
    #     if self.solved_at is not None:
    #         return True
    #     return False
