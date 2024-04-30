from pydantic import BaseModel


class MaterialsDTO(BaseModel):
    wood: int
    stone: int
    metal: int
    hq_metal: int