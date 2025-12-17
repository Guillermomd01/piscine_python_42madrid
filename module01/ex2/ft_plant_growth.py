"""
Plant growth simulator module.
Simulates plant growth over time.
"""


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.days = age

    def grow(self):
        self.height += 1

    def grow_older(self):
        self.days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


plant1 = Plant("Rose", 25, 30)
start_height = plant1.height
i = 0
print("=== Day 1 ===")
plant1.get_info()
while (i < 6):
    plant1.grow()
    plant1.grow_older()
    i += 1
print("=== Day 7 ===")
plant1.get_info()
plant_grow = plant1.height - start_height
print(f"Growth this week: +{plant_grow}cm")
