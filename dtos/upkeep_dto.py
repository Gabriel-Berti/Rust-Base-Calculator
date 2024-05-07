from pydantic import BaseModel
from .materials_dto import MaterialsDTO

class UpKeepDTO(BaseModel):
    cost: MaterialsDTO