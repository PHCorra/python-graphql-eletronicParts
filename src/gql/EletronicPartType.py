import strawberry
from model.EletronicPart import EletronicPart as EletronicPartModel
from typing import List, TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from .EnterpriseType import EnterpriseType

@strawberry.type
class EletronicPartType:
    id: int
    name: str
    description: str
    enterprise: Annotated["EnterpriseType", strawberry.lazy(".EnterpriseType")]

    @staticmethod
    def from_model(model: EletronicPartModel) -> "EletronicPartType":
        return EletronicPartType(
            id=model.id,
            name=model.name,
            description=model.description,
            enterprise=EnterpriseType.from_model(model.enterprise)
        )
