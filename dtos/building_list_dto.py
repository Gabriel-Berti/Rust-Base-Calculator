from pydantic import BaseModel
from typing import List
from .building_list_item_dto import BuildingListItem

class BuildingList(BaseModel):
    list: List[BuildingListItem]