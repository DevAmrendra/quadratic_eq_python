import math, cmath

def solve_quadratic(a, b, c):
    discriminant = (b**2 - 4*a*c)
    if discriminant > 0:
       root1 = (-b + math.sqrt(discriminant))/2*a
       root2 = (-b - math.sqrt(discriminant))/2*a
       return root1, root2
    elif discriminant == 0:
        root = (-b/2*a)
        return root
    else:
        root1 = (-b + cmath.sqrt(discriminant))/2*a
        root2 = (-b - cmath.sqrt(discriminant))/2*a
        return root1, root2

a = int(input("Enter Coefficient Of x^2: "))
b = int(input("Enter Coefficient Of x: "))
c = int(input("Enter Constant Number: "))

solutions = solve_quadratic(a, b, c)
print(f"Roots of your quadratic equation are {solutions}")