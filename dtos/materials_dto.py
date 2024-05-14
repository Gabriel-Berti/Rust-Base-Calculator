from pydantic import BaseModel


class MaterialsDTO(BaseModel):
    twig: int
    wood: int
    stone: int
    metal: int
    hq_metal: int