def ft_garden_intro(plant_type: str, height: int, age:int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_type}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")
    
    
if __name__ == "__main__":
    ft_garden_intro("rosa", 30, 54)