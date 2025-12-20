# import sys
import math

origin_coords = (0, 0, 0)
created_coords = (10, 20, 5)
print(f"Position created: {created_coords}")
x0, y0, z0 = origin_coords
x1, y1, z1 = created_coords
distance = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2)
print(f"Distance between {origin_coords} and {created_coords}: {distance:.2f}")

string_coords = "3,4,0"
print(f'Parsing coordinates: "{string_coords}"')
split_coords = string_coords.split(",")
parsed_coords = []
for coords in split_coords:
    parsed_coords.append(int(coords))
parsed_coords = tuple(parsed_coords)
print(f"Parsed position: {parsed_coords}")
x2, y2, z2 = parsed_coords
distance = math.sqrt((x2 - x0) ** 2 + (y2 - y0) ** 2 + (z2 - z0) ** 2)
print(f"Distance between {origin_coords} and {parsed_coords}: {distance:.1f}")

print('Parsing invalid coordinates: "abc,def,ghi"')
try:
    int("abc")
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f'Error details - Type: {type(e).__name__}, Args: {e.args}')
print("Unpacking demonstration:")
print(f"Player at x={x2}, y={y2}, z={z2}")
print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
