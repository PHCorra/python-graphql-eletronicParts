import strawberry
from typing import List, TYPE_CHECKING, Annotated
from model.Enterprise import Enterprise as EnterpriseModel

if TYPE_CHECKING:
    from .EletronicPartType import EletronicPartType

@strawberry.type
class EnterpriseType:
    id: int
    name: str
    eletronic_parts: List[
        Annotated["EletronicPartType", strawberry.lazy(".EletronicPartType")]
        ]

    @staticmethod
    def from_model(model: EnterpriseModel) -> "EnterpriseType":
        return EnterpriseType(
            id=model.id,
            name=model.name,
            eletronic_parts=[EletronicPartType.from_model(p) for p in model.eletronic_parts]
        )
