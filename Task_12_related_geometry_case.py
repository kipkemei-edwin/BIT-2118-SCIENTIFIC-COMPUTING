from scipy.optimize import root

# A circular safety boundary with radius 5 intersects a parabolic road profile.
# Circle: x^2 + y^2 = 25
# Parabola: y = 0.5*x^2 - 2

def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 25,
        y - (0.5*x**2 - 2)
    ]

for guess in ([3.0, 2.5], [-3.0, 2.5]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection (x, y):", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()
