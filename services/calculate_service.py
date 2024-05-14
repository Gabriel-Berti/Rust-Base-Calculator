from dtos.building_list_dto import BuildingList
from dtos.materials_dto import MaterialsDTO
from dtos.total_cost_dto import TotalCostDTO
from dtos.upkeep_dto import UpKeepDTO

def calculate_upkeep_cost(buildingList: BuildingList, blocksQuantity: int):
    wood = 0
    stone = 0
    metal = 0
    hq_metal = 0

    match blocksQuantity:
        case n if 1 <= n <= 15:
            tax = (blocksQuantity * 0.1)/ blocksQuantity
        case n if 16 <= n <= 65:
            tax = ((15 * 0.1) + (blocksQuantity - 15 * 0.15))/ blocksQuantity
        case  n if 66 <= n <= 190:
            tax = ((15 * 0.1) + (50 + 0.15) + (blocksQuantity - 65 * 0.2))/ blocksQuantity
        case _:
            tax = ((15 * 0.1) + (50 + 0.15) + (125 * 0.2) + (blocksQuantity - 190 * 0.333))/ blocksQuantity
    
    for item in buildingList.list:
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
    blocksQuantity = 0

    for item in buildingList.list:
        blocksQuantity = blocksQuantity + item.quantity
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

    return  materialTotalCost, blocksQuantity

def calculate_total_cost(buildingList: BuildingList):
    
    materialTotalCost, blocksQuantity = calculate_building_cost(buildingList)
    upKeepCost: UpKeepDTO = calculate_upkeep_cost(buildingList, blocksQuantity)

    totalCost: TotalCostDTO = {
        "upKeepCost": upKeepCost,
        "materialTotalCost": materialTotalCost
    }

    return totalCost