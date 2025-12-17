import sys
import math

tupla1 = tuple(sys.argv[1:])
print(f"position created: {tupla1}")
distance = math.sqrt((int(tupla1[0]) - 0) ** 2 + (int(tupla1[1]) - 0) ** 2 + (int(tupla1[2]) - 0) ** 2)
print(f"Distance between (0, 0, 0) and {tupla1}: {distance:.2f}")
