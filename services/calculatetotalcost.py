from dtos.buildinglistdto import BuildingList
from dtos.materialsdto import MaterialsDTO

def calculate_total_cost(buildingList: BuildingList):
    totalCost: MaterialsDTO
    for item in buildingList.list:
        print(item.cost)
        cost = list(item.cost.keys())
        quantity = item.quantity
        for item in cost:
            totalCost[item] = totalCost[item] + (cost[item] * quantity)
    return totalCost