print("💉 CALENDARIO DE VACUNACIÓN")

try:
    edad = int(input("Ingresa la edad en meses: "))
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad <= 2:
        print("🟢 Vacunas recomendadas:")
        print("   - Hepatitis B")
        print("   - BCG (Tuberculosis)")
    elif edad <= 4:
        print("🟢 Vacunas recomendadas:")
        print("   - Pentavalente")
        print("   - Polio")
        print("   - Rotavirus")
    elif edad <= 6:
        print("🟡 Vacunas recomendadas:")
        print("   - Influenza")
        print("   - Neumococo")
    elif edad <= 18:
        print("🟠 Vacunas recomendadas:")
        print("   - Triple viral")
        print("   - Hepatitis A")
        print("   - VPH (a partir de 12 años)")
    else:
        print("🔴 Consulta con tu médico")
        print("   - Refuerzos adultos")
        print("   - Vacuna antigripal anual")
        
except ValueError:
    print("❌ Ingresa una edad válida en meses")
