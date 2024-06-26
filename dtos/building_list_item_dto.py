from pydantic import BaseModel
from .materials_dto import MaterialsDTO

class BuildingListItem(BaseModel):
    cost: MaterialsDTO
    quantity: int
    isUpKeep: bool
