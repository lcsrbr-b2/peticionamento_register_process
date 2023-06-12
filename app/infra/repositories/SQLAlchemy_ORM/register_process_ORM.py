from sqlalchemy import select, insert
from app.domains.process_domain import ProcessDomain
from app.infra.repositories.SQLAlchemy_ORM.models.process import process_table

from app.domains.tribunal_domain import TribunalDomain
from app.infra.repositories.SQLAlchemy_ORM.models.tribunal import tribunal_table

from app.domains.attorney_domain import AttorneyDomain
from app.infra.repositories.SQLAlchemy_ORM.models.attorney import attorney_table

from app.domains.process_type_domain import ProcessTypeDomain
from app.infra.repositories.SQLAlchemy_ORM.models.process_type import process_type_table

from app.domains.process_change_type_domain import ProcessChangeTypeDomain
from app.infra.repositories.SQLAlchemy_ORM.models.process_change_type import process_change_type_table

from app.domains.process_change_domain import ProcessChangeDomain
from app.infra.repositories.SQLAlchemy_ORM.models.process_change import process_change_table

from app.domains.process_type_domain import ProcessTypeDomain
from app.infra.repositories.SQLAlchemy_ORM.models.process_type import process_type_table



from app.domains.repositories.register_process_repository import RegisterProcessRepository
# from app.infra.repositories.SQLAlchemy_ORM.models.user import user_table
# from app.domains.repositories.user_repository import UserRepository
# from app.domains.user_domain import UserDomain


class SQLAlchemyORM(RegisterProcessRepository):
    def __init__(self, session):
        self.session = session

    def get_tribunal_id(self, tribunal: TribunalDomain):
        result = self.session.execute(select(tribunal_table).filter_by(
            uf=tribunal.uf, instance=tribunal.instance
            ))
        return result.mappings().first()

    def register_tribunal(self, tribunal: TribunalDomain):
        inserted = self.session.execute(insert(tribunal_table).values(
            tribunal.__dict__))
        self.session.commit()
        return inserted.inserted_primary_key[0]

    def register_attorney(self, attorney: AttorneyDomain, process_id: int):
        inserted = self.session.execute(insert(attorney_table).values(
            name=attorney.name,
            process_id=process_id,
            oab_number=attorney.oab
        ))
        self.session.commit()
        return inserted.inserted_primary_key[0]

    def get_process_type(self, process_type: ProcessTypeDomain):
        result = self.session.execute(select(process_type_table).filter_by(
            name=process_type))
        return result.mappings().first()

    def register_process_type(self, process_type: ProcessTypeDomain):
        inserted = self.session.execute(insert(process_type_table).values(name=process_type))
        self.session.commit()
        return inserted.inserted_primary_key[0]

    def register_process(
        self,
        process: ProcessDomain,
    ):
        inserted = self.session.execute(insert(process_table).values(
            system=process["system"],
            system_version=process["system_version"],
            office=process["office"],
            process_number=process["process_number"],
            tribunal_id=process["tribunal_id"],
            office_user_office_id=process["office_user_office_id"],
            office_user_user_id=process["office_user_user_id"],
            office_user_office_permission_id=process["office_user_office_permission_id"],
            process_type_id=process["process_type_id"]
        ))
        self.session.commit()
        return inserted.inserted_primary_key[0]

    def get_process_change_type(self, process_change: ProcessChangeTypeDomain):
        result = self.session.execute(select(process_change_type_table).filter_by(
            name=process_change))
        return result.mappings().first()

    def register_process_change_type(self, process_change_type: ProcessChangeTypeDomain):
        inserted = self.session.execute(insert(process_change_type_table).values(name=process_change_type))
        self.session.commit()
        return inserted.inserted_primary_key[0]

    def register_process_change(self, process_change: ProcessChangeDomain):
        inserted = self.session.execute(insert(process_change_table).values(
            process_change_number=process_change["process_change_number"],
            process_id=process_change["process_id"],
            process_change_type_id=process_change["process_change_type_id"],
            created_at=process_change["created_at"],
            deadline=process_change["deadline"],
            status=process_change["status"],
        ))
        self.session.commit()
        return inserted.inserted_primary_key[0]
