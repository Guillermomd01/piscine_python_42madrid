"""
Garden analytics platform module.
Provides statistics and management for multiple gardens.
"""
class GardenManager():
    number_gardens = 0
    gardens = []
    class GardenStats():
        @staticmethod 
        def total_plant(garden):
            i = 0
            for n in garden.plants:
                i += 1
            return i
        @staticmethod 
        def total_grow(garden):
            i = 0
            for n in garden.plants:
                i += n.grow
            return i   
        @staticmethod
        def count_types(garden):
            regular = 0
            flowering = 0
            prize = 0
            for n in garden.plants:
                if n.prize_points > 0:
                    prize += 1
                elif n.color != None:
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize
    @staticmethod
    def height_validation_test(garden):
        for n in garden.plants:
            if n.height < 0:
                return False
        return True
    @classmethod
    def add_garden(cls, garden):
        cls.gardens.append(garden)
        cls.number_gardens += 1
        return cls.number_gardens
    @classmethod
    def create_garden_network(cls):
        total_plants = 0
        total_grow = 0
        validation = False
        total_scores = {}
        comparation_exit = ""
        for garden in cls.gardens:
            total_plants = cls.GardenStats.total_plant(garden)
            total_grow = cls.GardenStats.total_grow(garden)
            validation = GardenManager.height_validation_test(garden)
            if validation is False:
                score = 0
            else:
                score = total_plants + total_grow
            total_scores[garden.name] = score
        for key, value in total_scores.items():
            comparation_exit += f"{key}: {value}, "
        print(f"Garden scores - {comparation_exit[:-2]}")
        print(f"Total gardens managed: {cls.number_gardens}")

class Garden():
    def __init__(self, name: str):
        self.name = name
        self.plants = []
    def add_plant(self, new_plant):
        self.plants.append(new_plant)
        print(f"Added {new_plant.name} to {self.name}'s garden")
    def grow_all_plants(self, size: int):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.to_grow(size)
    def garden_report(self):
        regular = 0
        flowering = 0
        prize = 0
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if plant.prize_points > 0:
                if plant.bloom == True:
                    print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming), Prize points: {plant.prize_points}\n")
                    prize += 1
                else:
                    print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers, Prize points: {plant.prize_points}\n")
                    prize += 1
            elif plant.color != None:
                if plant.bloom == True:
                    print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")
                    flowering += 1
                else:
                    print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers")
                    flowering += 1
            else:
                print(f"- {plant.name}: {plant.height}cm")
                regular += 1
        print(f"Plants added: {GardenManager.GardenStats.total_plant(self)}, Total growth: {GardenManager.GardenStats.total_grow(self)}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers\n")
        print(f"Height validation test: {GardenManager.height_validation_test(self)}")

class Plant():
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.grow = 0
        self.color = None
        self.prize_points = 0
    def to_grow(self, size: int):
        self.height += size 
        self.grow += size
        print(f"{self.name} grew {size}cm")
class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.bloom = False
        self.prize_points = 0
    def to_bloom(self):
        self.bloom = True
        
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.prize_points = points
        
if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # Crear jardines
    alice = Garden("Alice")
    bob = Garden("Bob")

    # Crear plantas
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    # Hacer que florezcan las plantas con flores
    rose.to_bloom()
    sunflower.to_bloom()

    # Añadir plantas al jardín de Alice
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print()
    # Hacer crecer las plantas
    alice.grow_all_plants(1)
    print()
    # Mostrar informe del jardín de Alice
    alice.garden_report()
    # Registrar jardines en el manager
    GardenManager.add_garden(alice)
    GardenManager.add_garden(bob)
    # Crear red de jardines (estadísticas globales)
    GardenManager.create_garden_network()
