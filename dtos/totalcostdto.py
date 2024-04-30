from pydantic import BaseModel
from .materialsdto import MaterialsDTO
# from .upkeepdto import UpkeepDTO

class TotalCostDTO(BaseModel):
    #upKeepTime: UpkeepDTO
    materialTotalCost: MaterialsDTO
