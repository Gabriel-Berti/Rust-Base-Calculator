from pydantic import BaseModel
from .materials_dto import MaterialsDTO
from .upkeep_dto import UpKeepDTO

class TotalCostDTO(BaseModel):
    upKeepCost: UpKeepDTO
    materialTotalCost: MaterialsDTO
