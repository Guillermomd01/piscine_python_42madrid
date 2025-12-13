def garden_operations(error_type):
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        10 / 0
    elif error_type == "file":
        open("missing.txt")
    elif error_type == "key":
        plants = {"rose": 3}
        print(plants["missing_plant"])
def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    try:
        print("Testing FileNotFoundError...")
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")
    try:
        print("Testing KeyError")
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    print("Testing multiple error together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")
test_error_types()


def garden_operations(error_type):
    if error_type == "zero":
        1 / 0
    elif error_type == "key":
        plants = {"rose": 3}
        print(plants["missing\_plant"])

def test_error_types():
    print("=== Garden Error Types Demo ===")

    try:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()")
    except ValueError:
        pass

    try:
        print("Testing ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except FileNotFoundError:
        pass
    try:
        print("Testing KeyError")
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    print("Testing multiple errors together...")
    try:
        {}["another_missing"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


test_error_types()

