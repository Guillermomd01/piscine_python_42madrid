class GardenManager():
    number_gardens = 0
    def __init__(self):
        pass
    
    def add_garden(self):
        number_gardens += 1
        return number_gardens
    @classmethod
    def create_garden_network(cls):
        pass

class Plant():
    def __init__(self, name: str, height: int, grow: int):
        self.name = name
        self.height = height
        self.grow = grow

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, grow: int, color: str):
        super().__init__(name, height, grow)
        self.color = color

class PrizeFlower(Plant, FloweringPlant):
    def __init__(self, name, height, grow, color):
        super().__init__(name, height, grow, color)
        
class Garden():
    def __init__(self, name: str, plant_list: list, ):
        self.name = name
        self.plant_list = plant_list