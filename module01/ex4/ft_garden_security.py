class SecurePlant:
    def __init__(self, name:str, height:int, days:int):
        self.name = name
        self.set_height = height
        self.set_age = days
        print(f"Plant created: {self.name}")
        
    @property
    def get_height(self):
        return self._height
    @get_height.setter
    def set_height(self, height:int):
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")
    
    @property
    def get_age(self):
        return self._age
    @get_age.setter
    def set_age(self, age: int):
        if (age < 0):
            print(f"invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")
        
    def get_info(self):
        print(f"Current plant: {self.name} ({self._height}cm, {self._age} days)")    
    
rose = SecurePlant("rose", 32, 43)
print(rose.get_age)
rose.get_info()
#setter es ideal para validaciones
#propperty es ideal para leer
