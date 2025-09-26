from model.EletronicPart import EletronicPart
from sqlalchemy.orm import Session

class EletronicPartRepository:
    def __init__(self, db: Session):
        self.db = db

def create(self, name: str, description: str, enterprise_id: int) -> EletronicPart:
    eletronic_part = EletronicPart(name=name, description=description, enterprise_id=enterprise_id)
    self.db.add(eletronic_part)
    self.db.commit()
    self.db.refresh(eletronic_part)
    return eletronic_part

def get_all(self) -> list[EletronicPart]:
    return self.db.query(EletronicPart)