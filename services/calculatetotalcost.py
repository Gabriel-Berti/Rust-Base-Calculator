from dtos.materialsdto import MaterialsDTO

def calculate_total_cost(buildingList):
    totalCost: MaterialsDTO
    for item in buildingList:
        cost = item.cost.keys()
        quantity = item.quantity
        for item in cost:
            totalCost[item] = totalCost[item] + (cost[item] * quantity) 
            