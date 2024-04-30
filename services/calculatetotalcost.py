from dtos.buildinglistdto import BuildingList
from dtos.materialsdto import MaterialsDTO


def calculate_total_cost(buildingList: BuildingList):
    wood = 0
    stone = 0
    metal = 0
    hq_metal = 0
    
    for item in buildingList.list:
        quantity = item.quantity
        wood = wood + (item.cost.wood * quantity)
        stone = stone + (item.cost.stone * quantity)
        metal = metal + (item.cost.metal * quantity)
        hq_metal = hq_metal + (item.cost.hq_metal * quantity)
    
    totalCost: MaterialsDTO = {
        "wood": wood,
        "stone": stone,
        "metal": metal,
        "hq_metal": hq_metal
    }
    
    return totalCost