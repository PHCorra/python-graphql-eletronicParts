import strawberry
from config.database import SessionLocal
from gql.EnterpriseType import EnterpriseType
from gql.EletronicPartType import EletronicPartType
from repository.EnterpriseRepository import EnterpriseRepository
from repository.EletronicPartsRepository import EletronicPartRepository

@strawberry.type
class Query:
    @strawberry.field
    def enterprises(self) -> list[EnterpriseType]:
        session = SessionLocal()
        try:
            repo = EnterpriseRepository(session)
            models = repo.get_all()
            return [EnterpriseType.from_model(m) for m in models]
        finally:
            session.close()


    @strawberry.field
    def eletronic_parts(self) -> list[EletronicPartType]:
        session = SessionLocal()
        try:
            repo = EletronicPartRepository(session)
            models = repo.get_all()
            return [EletronicPartType.from_model(m) for m in models]
        finally:
            session.close()