def ft_count_harvest_recursive():
    days = int(input("Enter number of days: "))
    init = 1

    def recursive(days: int, init: int) -> None:
        print(f"Day: {init}")
        if days == 1:
            return
        init += 1
        recursive(days - 1, init)
    recursive(days, init)
    print("Harvest time!")
