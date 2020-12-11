import math
a = float(input("digite o a: "))
b = float(input("digite o b: "))
c = float(input("digite o c: "))
delta = b ** 2 - 4 * a *c
x = (-b + math.sqrt(delta)) / (2 * a)
x2= (-b - math.sqrt(delta)) / (2 * a)
if delta == 0:
    print("a conta tem apenas 1 resultado", x)
elif delta >= 0:
    print("a conta tem duas raizes que são:", x, x2)


