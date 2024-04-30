from pydantic import BaseModel
from .materialsdto import MaterialsDTO

class UpkeepDTO(BaseModel):
    cost: MaterialsDTO