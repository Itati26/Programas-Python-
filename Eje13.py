def generar_matricula(anio_ingreso, numero_carrera, numero_alumno):
    # Aseguramos que los números tengan el formato adecuado (rellenando con ceros si es necesario)
    anio = str(anio_ingreso)
    carrera = str(numero_carrera).zfill(2)  # Suponiendo que hay menos de 100 carreras
    alumno = str(numero_alumno).zfill(4)    # Suponiendo hasta 9999 alumnos por carrera y año

    # Concatenamos todos los elementos para formar la matrícula
    matricula = f"{anio}{carrera}{alumno}"
    return matricula
