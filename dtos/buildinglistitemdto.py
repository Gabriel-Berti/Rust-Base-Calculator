from pydantic import BaseModel
from .materialsdto import MaterialsDTO

class BuildingListItem(BaseModel):
    cost: MaterialsDTO
    quantity: int
