class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager():
    def __init__(self):
        self.plants = []

    def add_plant(self, name, water, sun):
        if name == "":
            raise PlantError("Plant name cannot be empty!")
        else:
            individual_plant = {
                'name_plant': name,
                'water_level': water,
                'sunlight_hours': sun
            }
            self.plants.append(individual_plant)
            print(f"Added {name} successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            for name in self.plants:
                print(f"Watering {name['name_plant']} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        print("Checking plant health...")
        try:
            for plant in self.plants:
                hour = plant['sunlight_hours']
                water = plant['water_level']
                if water > 10:
                    raise PlantError(
                        f"Water level {water} is too high (max 10)"
                        )
                elif water < 0:
                    raise PlantError(f"Water level {water} is too low (min 1)")
                elif hour < 2:
                    raise PlantError(
                        f"Sunlight hours {hour} is too low (min 2)"
                        )
                elif hour > 12:
                    raise PlantError(
                        f"Sunlight hours {hour} is too high (max 12)"
                        )
                else:
                    print(
                        f"{plant['name_plant']}: healthy (water: {water}, "
                        f"sun: {hour})")
        except PlantError as e:
            print(f"Error checking {plant['name_plant']}: {e}")


print("=== Garden Management System ===\n")

manager = GardenManager()

print("Adding plants to garden...")
try:
    manager.add_plant("tomato", 5, 8)
except PlantError as e:
    print(f"Error adding plant: {e}")

try:
    manager.add_plant("lettuce", 15, 6)
except PlantError as e:
    print(f"Error adding plant: {e}")

try:
    manager.add_plant("", 4, 5)
except PlantError as e:
    print(f"Error adding plant: {e}")

print("\nWatering plants...")
manager.water_plants()
print()
manager.check_plant_health()

print("\nTesting error recovery...")
try:
    raise WaterError("Not enough water in tank")
except GardenError as e:
    print(f"Caught GardenError: {e}")

print("System recovered and continuing...")
print("Garden management system test complete!")
