import datetime
from app.domains.register_process_domain import RegisterProcessDomain
from app.domains.repositories.register_process_repository import (
    RegisterProcessRepository,
)


class RegisterProcessService:
    """_summary_"""

    def __init__(self, repository: RegisterProcessRepository):
        self.repository = repository

    def register(self, process: RegisterProcessDomain):
        """_summary_
        Args:
            process (RegisterProcessDomain): _description_
        Returns:
            _type_: _description_
        """
        tribunal_id = self.repository.get_tribunal_id(process.data.process.tribunal)
        if tribunal_id is None:
            tribunal_id = self.repository.register_tribunal(process.data.process.tribunal)
        else:
            tribunal_id = tribunal_id.id
        process_type_id = self.repository.get_process_type(
            process.data.process.process_type
            )
        if process_type_id is None:
            process_type_id = self.repository.register_process_type(
                process.data.process.process_type
                )
        else:
            process_type_id = process_type_id.id
        process_data = {
            "system": process.data.process.system,
            "system_version": process.data.process.system_version,
            "office": process.data.process.office,
            "process_number": process.data.process.process_number,
            "tribunal_id": tribunal_id,
            "office_user_office_id": 1,
            "office_user_user_id": 1,
            "office_user_office_permission_id": 1,
            "process_type_id": process_type_id
        }

        process_id = self.repository.register_process(process_data)
        self.repository.register_attorney(process.data.process.attorney, process_id)
        
        for process_change in process.data.process.process_changes:
            
            process_change_type_id = self.repository.get_process_change_type(process_change.process_change_type)
            if process_change_type_id is None:
                process_change_type_id = self.repository.register_process_change_type(
                process_change.process_change_type
                )
            else:
                process_change_type_id = process_change_type_id.id
            process_change_data = {
                "process_change_number": process_change.process_change_number,
                "process_id": process_id,
                "process_change_type_id": process_change_type_id,
                "created_at": datetime.datetime.now(),
                "deadline": process_change.deadline,
                "status": process_change.status
            }
            self.repository.register_process_change(process_change_data)
        
        return process_id
