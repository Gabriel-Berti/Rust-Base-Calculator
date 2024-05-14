import re
from fastapi import APIRouter, Body, Query, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Optional
from dtos.building_list_dto import BuildingList
from dtos.total_cost_dto import TotalCostDTO


from models import BuildingBlock, BuildingBlocksCollection
from services.calculate_service import calculate_total_cost

router = APIRouter()

@router.post("/building-blocks",response_description="Adding New Building Blocks", status_code=status.HTTP_201_CREATED)
def create_building_blocks(request: Request, blocks: List[BuildingBlock] = Body(...)):
    insertedBlock =  []
    for block in blocks:
        block = jsonable_encoder(block)
        new_block = request.app.database["building-blocks"].insert_one(block)
        created_block = request.app.database["building-blocks"].find_one(
            {"_id": new_block.inserted_id}
        )
        insertedBlock.append(created_block)
    return {"building-blocks": insertedBlock}

@router.get("/building-blocks/", response_description="List searched blocks", response_model=BuildingBlocksCollection)
def get_building_blocks(request: Request, name: Optional[str] = Query(None)):
    if name:
        regex = re.compile(name, re.IGNORECASE)
        blocks = list(request.app.database["building-blocks"].find({"name": {"$regex" : regex}}))
        return BuildingBlocksCollection(buildingBlocks=blocks)
    
    blocks = list(request.app.database["building-blocks"].find())
    return BuildingBlocksCollection(buildingBlocks=blocks)

@router.post("/calculate", response_description="Calculates total cost based on the building list received")
def post_calcute(buildingList: BuildingList = Body(...)):
    totalCost = calculate_total_cost(buildingList)
    return totalCost