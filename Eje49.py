from datetime import datetime
año_nacimiento = int(input("Año de nacimiento: "))
año_actual = datetime.now().year
print(f"Edad: {año_actual - año_nacimiento} años")
