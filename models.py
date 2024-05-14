import uuid
from typing import List
from pydantic import BaseModel, Field

class Materials(BaseModel):
    twig: int = Field(...)
    wood: int = Field(...)
    stone: int = Field(...)
    metal: int = Field(...)
    hq_metal: int = Field(...)

class BuildingBlock(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    cost: Materials

class BuildingBlocksCollection(BaseModel):
    buildingBlocks: List[BuildingBlock]



