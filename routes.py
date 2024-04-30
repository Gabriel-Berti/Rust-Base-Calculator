import re
from fastapi import APIRouter, Body, Query, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Optional
from dtos.buildinglistdto import BuildingList
from dtos.totalcostdto import TotalCostDTO


from models import Book, BookUpdate, BuildingBlock, BuildingBlocksCollection
from services.calculatetotalcost import calculate_total_cost

router = APIRouter()

@router.post("/", response_description="Create a new book", status_code=status.HTTP_201_CREATED, response_model=Book)
def create_book(request: Request, book: Book = Body(...)):
    book = jsonable_encoder(book)
    new_book = request.app.database["books"].insert_one(book)
    created_book = request.app.database["books"].find_one(
        {"_id": new_book.inserted_id}
    )

    return created_book

@router.get("/", response_description="List all books", response_model=List[Book])
def list_books(request: Request):
    books = list(request.app.database["books"].find(limit=100))
    return books

@router.get("/{id}", response_description="Get a single book by id", response_model=Book)
def find_book(id: str, request: Request):
    if (book := request.app.database["books"].find_one({"_id": id})) is not None:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

@router.put("/{id}", response_description="Update a book", response_model=Book)
def update_book(id: str, request: Request, book: BookUpdate = Body(...)):
    book = {k: v for k, v in book.model_dump().items() if v is not None}
    if len(book) >= 1:
        update_result = request.app.database["books"].update_one(
            {"_id": id}, {"$set": book}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

    if (
        existing_book := request.app.database["books"].find_one({"_id": id})
    ) is not None:
        return existing_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

@router.delete("/{id}", response_description="Delete a book")
def delete_book(id: str, request: Request, response: Response):
    delete_result = request.app.database["books"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

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

@router.post("/calculate", response_description="Calculates total cost based on the building list received", response_model=TotalCostDTO)
def post_calcute(buildindList: BuildingList = Body(...)):
    return calculate_total_cost(buildindList)