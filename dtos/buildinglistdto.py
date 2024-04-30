from pydantic import BaseModel
from typing import List
from .buildinglistitemdto import BuildingListItem

class BuildingList(BaseModel):
    list: List[BuildingListItem]