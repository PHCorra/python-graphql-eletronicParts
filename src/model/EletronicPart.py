from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class EletronicPart(Base):
    __tablename__ = "eletronic_parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    enterprise_id = Column(Integer, ForeignKey("enterprises.id"))

    enterprise = relationship("Enterprise", back_populates="eletronic_parts")