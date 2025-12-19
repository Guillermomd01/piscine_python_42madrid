def check_temperature(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    temperature = None
    try:
        temperature = int(temp_str)
    except ValueError:
        print(f"Error '{temp_str}' is not a valid number")
    if temperature is not None:

        if temperature >= 0 and temperature <= 40:
            print(f"Temperature {temperature}ºC i sperfect for plants!")
        elif temperature > 40:
            print(f"Error: {temperature}ºC is too hot for plants (max 40ºC)")
        elif temperature < 0:
            print(f"Error: {temperature}ºC is too cold for plants (min 0ºC)")
    print("All test completed - program didnt't crash!")


check_temperature("25")
check_temperature("abc")
check_temperature("100")
check_temperature(-50)
check_temperature("-50")
