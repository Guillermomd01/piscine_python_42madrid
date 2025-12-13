class GardenError(Exception):
    pass
class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass 
class GardenManager():
    def __init__(self, list_plant_dicc):
        self.plants = []
        for plant_dicc in list_plant_dicc:
            individual_plant = {
                'name_plant' : plant_dicc.get('nombre'),
                'water_level' : plant_dicc.get('agua'),
                'sunlight_hours' : plant_dicc.get('sol')
            }
            self.plants.append(individual_plant)
    def add_plant(self):
        print("Adding plant to garden...")
        for n in self.plants:
            for name in n['name_plant']:
                if name == "":
                    raise PlantError("Plant name cannot be empty!")
            else:
                print(f"Added {name} succesfully")
        
        
        