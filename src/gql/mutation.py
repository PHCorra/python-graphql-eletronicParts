import strawberry
from config.database import SessionLocal
from gql.EnterpriseType import EnterpriseType
from gql.EletronicPartType import EletronicPartType
from repository.EnterpriseRepository import EnterpriseRepository
from repository.EletronicPartsRepository import EletronicPartRepository

@strawberry.type
class Mutation:
    @strawberry.field
    def create_enterprise(self, name: str) -> EnterpriseType:
        session = SessionLocal()
        try:
            repo = EnterpriseRepository(session)
            enterprise_model = repo.create(name=name)
            return EnterpriseType.from_model(enterprise_model)
        finally:
            session.close()


    @strawberry.field
    def create_eletronic_part(self, name: str, description: str, enterprise_id: int) -> EletronicPartType:
        session = SessionLocal()
        try:
            repo = EletronicPartRepository(session)
            part_model = repo.create(name=name, description=description, enterprise_id=enterprise_id)
            return EletronicPartType.from_model(part_model)
        finally:
            session.close()