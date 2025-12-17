class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant_error():
    raise PlantError("The tomato plant is wilting!")


def water_error():
    raise WaterError("Not enough water in the tank!")


def caught_error():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        plant_error()
    except GardenError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        water_error()
    except GardenError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


caught_error()
