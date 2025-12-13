def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    days = range(days)
    for n in days:
        print("Day", n + 1)
    print("Harvest time!")

if __name__ == "__main__":
    ft_count_harvest_iterative()