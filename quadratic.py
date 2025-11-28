import cmath

def solve_quadratic(a, b, c):
    if a == 0:
        return "Coefficient 'a' cannot be zero in a quadratic equation."

    discriminant = (b ** 2) - (4 * a * c)
    root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)

    if discriminant > 0:
        nature = "Two distinct real roots"
    elif discriminant == 0:
        nature = "One real root (double root)"
    else:
        nature = "Two complex roots"

    return (nature, root1, root2)

