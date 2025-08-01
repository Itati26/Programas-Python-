from scipy.optimize import linprog

# Coeficientes de la función objetivo (negativos para maximizar)
c = [-20, -30, -25]  # Maximizar Z = 20x₁ + 30x₂ + 25x₃

# Coeficientes de las restricciones (Ax ≤ b)
A = [
    [1, 1, 3],   # Corte
    [1, 2, 1],   # Ensamblaje
    [1, 1, 1]    # Acabado
]
b = [600, 500, 300]

# Límites de las variables (x ≥ 0)
x_bounds = [(0, None), (0, None), (0, None)]

# Resolver
res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='simplex')

# Mostrar resultados
print("Estado:", res.message)
print("Valor óptimo de Z:", -res.fun)
print("Valores óptimos de las variables:", res.x)
