import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = b * b - 4 * a * c
print("Discriminant: ", d )
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1, x2)
elif d == 0:
    x1 = (-b) / (2 * a)
    x2 = x1
    print("Result", x1, x2)
elif d < 0:
    print("There is no roots")
exit()