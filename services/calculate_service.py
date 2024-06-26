from typing import List
from dtos.building_list_dto import BuildingList
from dtos.materials_dto import MaterialsDTO
from dtos.total_cost_dto import TotalCostDTO
from dtos.upkeep_dto import UpKeepDTO

def calculate_upkeep_cost(upKeepList: List, itemsQuantity: int):  
    wood = 0
    stone = 0
    metal = 0
    hq_metal = 0

    match itemsQuantity:
        case n if 1 <= n <= 15:
            tax = (itemsQuantity * 0.1)/ itemsQuantity
        case n if 16 <= n <= 65:
            tax = (1.5 + ((itemsQuantity - 15) * 0.15))/ itemsQuantity
        case  n if 66 <= n <= 190:
            tax = (9 + ((itemsQuantity - 65) * 0.2))/ itemsQuantity
        case _:
            tax = (34 + ((itemsQuantity - 190) * 0.333))/ itemsQuantity
    
    for item in upKeepList:
        wood = wood + ((item.cost.wood - item.cost.twig) * item.quantity * tax)
        metal = metal + (item.cost.metal * item.quantity * tax)
        stone = stone + (item.cost.stone * item.quantity * tax)
        hq_metal = hq_metal + (item.cost.hq_metal * item.quantity * tax)
        
    cost: MaterialsDTO = {
            "wood": round(wood),
            "stone": round(stone),
            "metal": round(metal),
            "hq_metal": round(hq_metal)
        }
    
    return cost

def calculate_building_cost(buildingList: BuildingList):
    wood = 0
    stone = 0
    metal = 0
    hq_metal = 0

    for item in buildingList.list:
        wood = wood + (item.cost.wood * item.quantity)
        stone = stone + (item.cost.stone * item.quantity)
        metal = metal + (item.cost.metal * item.quantity)
        hq_metal = hq_metal + (item.cost.hq_metal * item.quantity)
    
    materialTotalCost: MaterialsDTO = {
        "wood": wood,
        "stone": stone,
        "metal": metal,
        "hq_metal": hq_metal
    }

    return  materialTotalCost

def calculate_total_cost(buildingList: BuildingList):
    itemsQuantity = 0
    
    upKeepList = list(filter(lambda x: x.isUpKeep, buildingList.list))
    
    for item in upKeepList:
        itemsQuantity = itemsQuantity + item.quantity
    
    materialTotalCost = calculate_building_cost(buildingList)
    upKeepCost: UpKeepDTO = calculate_upkeep_cost(upKeepList, itemsQuantity)

    totalCost: TotalCostDTO = {
        "upKeepCost": upKeepCost,
        "materialTotalCost": materialTotalCost
    }

    return totalCost