class MaterialsDto(BaseModel):
    wood: int = Field(...)
    stone: int = Field(...)
    metal: int = Field(...)
    hq_metal: int = Field(...)