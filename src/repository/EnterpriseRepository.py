from model.Enterprise import Enterprise
from sqlalchemy.orm import Session

class EnterpriseRepository:
    def __init__(self, db: Session):
        self.db = db


    def create(self, name: str) -> Enterprise:
        enterprise = Enterprise(name=name)
        self.db.add(enterprise)
        self.db.commit()
        self.db.refresh(enterprise)
        return enterprise



    def get_all(self) -> list[Enterprise]:
        return self.db.query(Enterprise).all()