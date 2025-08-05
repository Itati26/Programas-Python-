from flask import Flask, render_template, request
from scipy.optimize import minimize
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolver', methods=['POST'])
def resolver():
    try:
        C1 = float(request.form['c1'])
        C2 = float(request.form['c2'])
        C3 = float(request.form['c3'])
    except ValueError:
        return render_template('index.html', error="Por favor ingresa valores numéricos válidos.", c1="", c2="", c3="")

    total_carga = 300.0  # Valor fijo

    # Validaciones
    if C1 <= 0 or C2 <= 0 or C3 <= 0:
        return render_template('index.html',
                               error="Todas las capacidades deben ser mayores que 0.",
                               c1=C1, c2=C2, c3=C3)

    if C1 + C2 + C3 < total_carga:
        return render_template(
            'index.html',
            error=f"La suma de capacidades ({C1 + C2 + C3} Mbps) debe ser mayor o igual a 300 Mbps.",
            c1=C1, c2=C2, c3=C3
        )

    C = np.array([C1, C2, C3])

    def funcion_objetivo(x):
        return np.sum((x ** 2) / C)

    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - total_carga}
    bounds = [(0, C1), (0, C2), (0, C3)]
    x0 = [total_carga / 3] * 3

    resultado = minimize(funcion_objetivo, x0, method='SLSQP', bounds=bounds, constraints=constraints)

    cargas = [round(x, 2) for x in resultado.x]
    penalizacion = round(resultado.fun, 4)
    total_acumulado = round(sum(cargas), 2)

    return render_template(
        'index.html',
        cargas=cargas,
        penalizacion=penalizacion,
        total_acumulado=total_acumulado
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=False, host='0.0.0.0', port=port)
