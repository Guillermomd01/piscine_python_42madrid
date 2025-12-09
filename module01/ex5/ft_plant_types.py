class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int, shade_size: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_size = shade_size
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")
    def produce_shade(self):
        print(f"{self.name} provides {self.shade_size} square meters of shade\n")

class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, {self.age} days, {self.color} color")
    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutricional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutricional_value = nutricional_value
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutricional_value}\n")

print("=== Garden Plant Types ===\n")
rose = Flower("Rose", 25, 30, "red")
rose.bloom()
oak = Tree("Oak", 500, 1825, 50, 78)
oak.produce_shade()
tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")