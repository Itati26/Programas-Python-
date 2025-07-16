import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTextEdit, QTabWidget,
                             QGroupBox, QFormLayout)
from PyQt5.QtCore import Qt
from scipy.optimize import minimize
import numpy as np
import re

class NonlinearOptimizationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optimización No Lineal - Soporte para Igualdades")
        self.setGeometry(100, 100, 900, 700)
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        
        self.create_tabs()
        self.add_help_section()
        self.show()
    
    def create_tabs(self):
        self.tabs = QTabWidget()
        
        # Pestaña para el primer problema de ejemplo
        tab1 = QWidget()
        self.setup_example1_tab(tab1)
        self.tabs.addTab(tab1, "Ejemplo Redes")
        
        # Pestaña para el segundo problema de ejemplo
        tab2 = QWidget()
        self.setup_example2_tab(tab2)
        self.tabs.addTab(tab2, "Ejemplo General")
        
        # Pestaña para problemas personalizados
        tab3 = QWidget()
        self.setup_custom_tab(tab3)
        self.tabs.addTab(tab3, "Problema Personalizado")
        
        self.layout.addWidget(self.tabs)
    
    def add_help_section(self):
        help_group = QGroupBox("Instrucciones y Sintaxis")
        help_layout = QVBoxLayout()
        
        help_text = QLabel("""
        <b>Instrucciones para ingresar funciones:</b>
        <ul>
            <li>Puede usar <b>^</b> o <b>**</b> para exponentes: x^2 o x**2</li>
            <li>Operadores matemáticos: +, -, *, / (o puede omitir * en 5x, 3y)</li>
            <li>Variables permitidas: x, y</li>
            <li>Ejemplos válidos: 
                <ul>
                    <li>5x - 0.02x^2 + 4y - 0.01y^2</li>
                    <li>40x + 30y - 0.1x**2 - 0.05y**2</li>
                </ul>
            </li>
        </ul>
        <b>Restricciones:</b>
        <ul>
            <li>Formatos admitidos: 
                <ul>
                    <li>[expresión] <= [valor]</li>
                    <li>[expresión] >= [valor]</li>
                    <li>[expresión] = [valor] (igualdad exacta)</li>
                </ul>
            </li>
            <li>Ejemplos: 2x + y <= 100, x + y = 50, x >= 0</li>
        </ul>
        """)
        help_text.setWordWrap(True)
        help_layout.addWidget(help_text)
        
        self.layout.addWidget(help_group)
        help_group.setLayout(help_layout)
    
    def setup_example1_tab(self, tab):
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Descripción del problema
        desc = QLabel("""<b>Optimización de ancho de banda en red de cómputo:</b>
        <p>Función objetivo: Z = 5x - 0.02x² + 4y - 0.01y²</p>
        <p>Puede ingresarla como: 5x - 0.02x^2 + 4y - 0.01y^2</p>
        <p>Restricciones: x + y ≤ 100, x ≥ 0, y ≥ 0</p>""")
        desc.setWordWrap(True)
        layout.addWidget(desc)
        
        # Botón para resolver
        solve_btn = QPushButton("Resolver Ejemplo de Redes")
        solve_btn.clicked.connect(self.solve_example1)
        layout.addWidget(solve_btn)
        
        # Área de resultados
        self.result1 = QTextEdit()
        self.result1.setReadOnly(True)
        layout.addWidget(self.result1)
    
    def solve_example1(self):
        # Función objetivo (negativa porque minimize busca el mínimo)
        def objective(vars):
            x, y = vars
            expr = "5*x - 0.02*x**2 + 4*y - 0.01*y**2"
            return -eval(expr, {'x': x, 'y': y})
        
        # Restricciones
        constraints = (
            {'type': 'ineq', 'fun': lambda vars: 100 - (vars[0] + vars[1])},  # x + y <= 100
            {'type': 'ineq', 'fun': lambda vars: vars[0]},  # x >= 0
            {'type': 'ineq', 'fun': lambda vars: vars[1]}   # y >= 0
        )
        
        # Punto inicial
        x0 = [50, 50]
        
        # Resolver
        solution = minimize(objective, x0, constraints=constraints)
        
        # Mostrar resultados
        if solution.success:
            x_opt, y_opt = solution.x
            z_opt = -solution.fun  # Negativo porque minimizamos el negativo
            self.result1.setText(
                f"<b>Solución óptima encontrada:</b>\n\n"
                f"x (Nodo A) = {x_opt:.2f} Mbps\n"
                f"y (Nodo B) = {y_opt:.2f} Mbps\n"
                f"Z máximo = {z_opt:.2f}\n\n"
                f"<i>Como se muestra en las diapositivas, la solución óptima es x=50, y=50 con Z=375.</i>"
            )
        else:
            self.result1.setText("<b>No se pudo encontrar una solución óptima.</b>")
    
    def setup_example2_tab(self, tab):
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Descripción del problema
        desc = QLabel("""<b>Ejemplo general de optimización no lineal:</b>
        <p>Función objetivo: Z = 40x + 30y - 0.1x² - 0.05y²</p>
        <p>Puede ingresarla como: 40x + 30y - 0.1x^2 - 0.05y^2</p>
        <p>Restricciones: 2x + y ≤ 100, x ≥ 0, y ≥ 0</p>""")
        desc.setWordWrap(True)
        layout.addWidget(desc)
        
        # Botón para resolver
        solve_btn = QPushButton("Resolver Ejemplo General")
        solve_btn.clicked.connect(self.solve_example2)
        layout.addWidget(solve_btn)
        
        # Área de resultados
        self.result2 = QTextEdit()
        self.result2.setReadOnly(True)
        layout.addWidget(self.result2)
    
    def solve_example2(self):
        # Función objetivo (negativa porque minimize busca el mínimo)
        def objective(vars):
            x, y = vars
            expr = "40*x + 30*y - 0.1*x**2 - 0.05*y**2"
            return -eval(expr, {'x': x, 'y': y})
        
        # Restricciones
        constraints = (
            {'type': 'ineq', 'fun': lambda vars: 100 - (2*vars[0] + vars[1])},  # 2x + y <= 100
            {'type': 'ineq', 'fun': lambda vars: vars[0]},  # x >= 0
            {'type': 'ineq', 'fun': lambda vars: vars[1]}   # y >= 0
        )
        
        # Punto inicial
        x0 = [0, 100]  # Basado en la solución en la diapositiva
        
        # Resolver
        solution = minimize(objective, x0, constraints=constraints)
        
        # Mostrar resultados
        if solution.success:
            x_opt, y_opt = solution.x
            z_opt = -solution.fun  # Negativo porque minimizamos el negativo
            self.result2.setText(
                f"<b>Solución óptima encontrada:</b>\n\n"
                f"x = {x_opt:.2f}\n"
                f"y = {y_opt:.2f}\n"
                f"Z máximo = {z_opt:.2f}\n\n"
                f"<i>Como se muestra en las diapositivas, una solución es x=0, y=100 con Z=2500.</i>"
            )
        else:
            self.result2.setText("<b>No se pudo encontrar una solución óptima.</b>")
    
    def setup_custom_tab(self, tab):
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Grupo para la función objetivo
        obj_group = QGroupBox("Función Objetivo (Z) - Maximizar")
        obj_layout = QFormLayout()
        
        self.obj_input = QLineEdit("0.01x^2 + 0.02y^2")
        obj_layout.addRow(QLabel("Z ="), self.obj_input)
        obj_group.setLayout(obj_layout)
        layout.addWidget(obj_group)
        
        # Grupo para las restricciones
        constr_group = QGroupBox("Restricciones")
        constr_layout = QVBoxLayout()
        
        # Restricción 1
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel("1)"))
        self.constr1 = QLineEdit("x + y = 100")
        hbox1.addWidget(self.constr1)
        constr_layout.addLayout(hbox1)
        
        # Restricción 2
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel("2)"))
        self.constr2 = QLineEdit("x > 0")
        hbox2.addWidget(self.constr2)
        constr_layout.addLayout(hbox2)
        
        # Restricción 3
        hbox3 = QHBoxLayout()
        hbox3.addWidget(QLabel("3)"))
        self.constr3 = QLineEdit("y > 0")
        hbox3.addWidget(self.constr3)
        constr_layout.addLayout(hbox3)
        
        constr_group.setLayout(constr_layout)
        layout.addWidget(constr_group)
        
        # Botón para resolver
        solve_btn = QPushButton("Resolver Problema Personalizado")
        solve_btn.clicked.connect(self.solve_custom)
        layout.addWidget(solve_btn)
        
        # Área de resultados
        self.custom_result = QTextEdit()
        self.custom_result.setReadOnly(True)
        layout.addWidget(self.custom_result)
    
    def convert_to_python_syntax(self, expr):
        """Convierte una expresión matemática natural a sintaxis Python válida"""
        # Paso 1: Manejar exponentes (^ y unicode ²,³)
        expr = expr.replace('²', '^2').replace('³', '^3')
        expr = re.sub(r'(\w+)\^(\d+)', r'\1**\2', expr)  # x^2 -> x**2
        
        # Paso 2: Manejar multiplicación implícita (5x -> 5*x)
        # Caso 1: Número seguido de variable (5x -> 5*x)
        expr = re.sub(r'(\d+)([xy])', r'\1*\2', expr)
        # Caso 2: Variable seguida de número (x2 -> x*2)
        expr = re.sub(r'([xy])(\d+)', r'\1*\2', expr)
        # Caso 3: Variable seguida de variable (xy -> x*y)
        expr = re.sub(r'([xy])([xy])', r'\1*\2', expr)
        
        # Paso 3: Manejar desigualdades unicode
        expr = expr.replace('≤', '<=').replace('≥', '>=')
        
        return expr
    
    def parse_constraint(self, constr):
        """Parsea una restricción en formato natural a una función Python"""
        constr = self.convert_to_python_syntax(constr.strip())
        
        if "<=" in constr:
            parts = constr.split("<=")
            if len(parts) != 2:
                raise ValueError(f"Formato de restricción incorrecto: {constr}")
            left, right = parts
            return {'type': 'ineq', 'fun': lambda vars, l=left, r=right: eval(r) - eval(l, {'x': vars[0], 'y': vars[1]})}
        elif ">=" in constr:
            parts = constr.split(">=")
            if len(parts) != 2:
                raise ValueError(f"Formato de restricción incorrecto: {constr}")
            left, right = parts
            return {'type': 'ineq', 'fun': lambda vars, l=left, r=right: eval(l, {'x': vars[0], 'y': vars[1]}) - eval(r)}
        elif "=" in constr:
            parts = constr.split("=")
            if len(parts) != 2:
                raise ValueError(f"Formato de restricción incorrecto: {constr}")
            left, right = parts
            return {'type': 'eq', 'fun': lambda vars, l=left, r=right: eval(l, {'x': vars[0], 'y': vars[1]}) - eval(r)}
        elif ">" in constr:
            parts = constr.split(">")
            if len(parts) != 2:
                raise ValueError(f"Formato de restricción incorrecto: {constr}")
            left, right = parts
            return {'type': 'ineq', 'fun': lambda vars, l=left, r=right: eval(l, {'x': vars[0], 'y': vars[1]}) - eval(r) - 1e-6}  # Pequeño margen para >
        elif "<" in constr:
            parts = constr.split("<")
            if len(parts) != 2:
                raise ValueError(f"Formato de restricción incorrecto: {constr}")
            left, right = parts
            return {'type': 'ineq', 'fun': lambda vars, l=left, r=right: eval(r) - eval(l, {'x': vars[0], 'y': vars[1]}) - 1e-6}  # Pequeño margen para <
        else:
            raise ValueError(f"Operador no soportado en restricción: {constr}")
    
    def solve_custom(self):
        try:
            # Obtener y convertir la función objetivo
            raw_obj_expr = self.obj_input.text()
            obj_expr = self.convert_to_python_syntax(raw_obj_expr)
            
            # Verificar que la expresión sea válida
            test_vars = {'x': 1, 'y': 1}
            try:
                eval(obj_expr, {}, test_vars)
            except Exception as e:
                raise ValueError(f"Expresión no válida: {raw_obj_expr}\nError: {str(e)}")
            
            # Parsear restricciones
            constraints = []
            constr_inputs = [self.constr1.text(), self.constr2.text(), self.constr3.text()]
            
            for constr in constr_inputs:
                if not constr.strip():
                    continue
                try:
                    constraints.append(self.parse_constraint(constr))
                except ValueError as e:
                    raise ValueError(f"Error en restricción '{constr}': {str(e)}")
            
            # Definir función objetivo para scipy
            def objective(vars):
                x, y = vars
                return eval(obj_expr, {'x': x, 'y': y})
            
            # Punto inicial (puede necesitar ajustes según el problema)
            x0 = [50, 50]  # Punto inicial razonable para el ejemplo dado
            
            # Resolver (ahora usamos 'minimize' directamente ya que podemos tener tanto maximización como minimización)
            solution = minimize(objective, x0, constraints=constraints)
            
            # Mostrar resultados
            if solution.success:
                x_opt, y_opt = solution.x
                z_opt = solution.fun
                
                # Mostrar la expresión original para mejor legibilidad
                display_obj = raw_obj_expr.replace('**', '^').replace('*', '')
                
                self.custom_result.setText(
                    f"<b>Solución óptima encontrada:</b>\n\n"
                    f"x = {x_opt:.4f}\n"
                    f"y = {y_opt:.4f}\n"
                    f"Z óptimo = {z_opt:.4f}\n\n"
                    f"<b>Función evaluada en el óptimo:</b>\n"
                    f"Z = {display_obj.replace('x', f'{x_opt:.2f}').replace('y', f'{y_opt:.2f}')}\n"
                    f" = {z_opt:.4f}"
                )
            else:
                self.custom_result.setText(
                    "<b>No se pudo encontrar una solución óptima.</b>\n\n"
                    "Posibles causas:\n"
                    "- Las restricciones pueden ser contradictorias\n"
                    "- El punto inicial no es adecuado\n"
                    "- La función puede tener múltiples óptimos locales\n"
                    "- Problemas de convergencia numérica"
                )
        
        except Exception as e:
            self.custom_result.setText(
                f"<b>Error al procesar el problema:</b>\n\n"
                f"{str(e)}\n\n"
                "Revise la sintaxis de las expresiones:\n"
                "- Use ^ o ** para exponentes (ej: x^2 o x**2 para x²)\n"
                "- Puede usar multiplicación implícita (ej: 5x en lugar de 5*x)\n"
                "- Formatos de restricciones admitidos: <=, >=, =, <, >"
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NonlinearOptimizationApp()
    sys.exit(app.exec_())
