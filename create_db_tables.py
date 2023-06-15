from sqlalchemy_utils import database_exists, create_database
from app.infra.repositories.SQLAlchemy_ORM.enviroment import engine, url
from app.infra.repositories.SQLAlchemy_ORM.models.office import office_table
from app.infra.repositories.SQLAlchemy_ORM.models.office_permission import (
    office_permission_table,
)
from app.infra.repositories.SQLAlchemy_ORM.models.user import user_table
from app.infra.repositories.SQLAlchemy_ORM.models.office_user import office_user_table
from app.infra.repositories.SQLAlchemy_ORM.models.process_type import process_type_table
from app.infra.repositories.SQLAlchemy_ORM.models.process import process_table
from app.infra.repositories.SQLAlchemy_ORM.models.process_part import process_part_table
from app.infra.repositories.SQLAlchemy_ORM.models.tribunal import tribunal_table
from app.infra.repositories.SQLAlchemy_ORM.models.attorney import attorney_table
from app.infra.repositories.SQLAlchemy_ORM.models.process_change import (
    process_change_table,
)
from app.infra.repositories.SQLAlchemy_ORM.models.process_change_type import (
    process_change_type_table,
)
from app.infra.repositories.SQLAlchemy_ORM.models.document import (
    document_table,
)
from app.infra.repositories.SQLAlchemy_ORM.models.document_type import (
    document_type_table,
)


def createdb():
    """Creates database"""
    if not database_exists(url):
        create_database(url)

    office_table.create(engine)
    user_table.create(engine)
    office_permission_table.create(engine)
    office_user_table.create(engine)
    process_type_table.create(engine)
    tribunal_table.create(engine)
    process_table.create(engine)
    attorney_table.create(engine)
    process_change_type_table.create(engine)
    process_part_table.create(engine)
    process_change_table.create(engine)
    document_type_table.create(engine)
    document_table.create(engine)


if __name__ == "__main__":
    createdb()
