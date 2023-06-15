from abc import ABC, abstractmethod
from app.domains.process_domain import ProcessDomain
from app.domains.tribunal_domain import TribunalDomain
from app.domains.attorney_domain import AttorneyDomain
from app.domains.process_type_domain import ProcessTypeDomain
# from
# from app.domains.user_domain import UserDomain


class ProcessRepository(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def get_tribunal_id(self, tribunal: TribunalDomain):
        ...

    @abstractmethod
    def register_tribunal(self, tribunal: TribunalDomain):
        ...

    @abstractmethod
    def register_attorney(self, attorney: AttorneyDomain, process_id: int):
        ...

    @abstractmethod
    def get_process_type(self, process_type: ProcessTypeDomain):
        ...

    @abstractmethod
    def register_process_type(self, process_type: ProcessTypeDomain):
        ...

    @abstractmethod
    def register_process(
        self,
        process: ProcessDomain,
    ):
        ...

    @abstractmethod
    def find_process_by_id(self, process_id: int):
        ...

    @abstractmethod
    def find_process_change_by_id(self, process_change_id: int):
        ...
