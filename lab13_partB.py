import math
 
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.1 + 0.2:.20f}")
print(math.isclose(0.1 + 0.2, 0.3))
 
total = 0.0
for _ in range(10):
    total += 0.1
print(total, total == 1.0)
