"""
Plant factory module.
Creates multiple plants efficiently.
"""
class Plant:
    count = 0
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.days = age
        Plant.count += 1
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")
print("=== Plant Factory Output ===")
rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 365)
cactus = Plant("Cactus", 5, 90)
sunflower = Plant("Sunflower", 90, 45)
fern = Plant("Fern", 15, 120)
print(f"\nTotal plants created: {Plant.count}")