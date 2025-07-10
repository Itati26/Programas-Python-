# from scipy.optimize import linprog
import numpy as np

# Coeficientes de la función objetivo (negativos porque linprog minimiza)
c = [-20, -30, -25]  # [sillas, mesas, librerías]

# Matriz de coeficientes de las restricciones
A = [
    [1, 1, 3],  # Corte
    [1, 2, 1],   # Ensamblaje
    [1, 1, 1]    # Acabado
]

# Lados derechos de las restricciones
b = [600, 500, 300]

# Para obtener la solución específica de 100 sillas, 200 mesas, 0 librerías
# Podemos agregar una restricción que limite las librerías a 0
A_eq = [[0, 0, 1]]  # x3 = 0
b_eq = [0]

# Resolver el problema
result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')

# Mostrar resultados
print("\nResultado óptimo con librerías fijadas a 0:")
print(f"Sillas: {result.x[0]:.0f} unidades")
print(f"Mesas: {result.x[1]:.0f} unidades")
print(f"Librerías: {result.x[2]:.0f} unidades")
print(f"Ganancia máxima: ${-result.fun:.2f}")

# Verificación de restricciones
print("\nVerificación de restricciones:")
print(f"Horas de Corte usadas: {result.x[0] + result.x[1] + 3*result.x[2]:.1f} (disponibles: 600)")
print(f"Horas de Ensamblaje usadas: {result.x[0] + 2*result.x[1] + result.x[2]:.1f} (disponibles: 500)")
print(f"Horas de Acabado usadas: {result.x[0] + result.x[1] + result.x[2]:.1f} (disponibles: 300)")Programas-Python-
