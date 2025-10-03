def calculadora_propinas():
    total_cuenta = float(input("Total de la cuenta: $"))
    porcentaje_propina = float(input("Porcentaje de propina: "))
    personas = int(input("Número de personas: "))
    
    propina = total_cuenta * (porcentaje_propina / 100)
    total_con_propina = total_cuenta + propina
    por_persona = total_con_propina / personas
    
    print(f"\nPropina: ${propina:.2f}")
    print(f"Total con propina: ${total_con_propina:.2f}")
    print(f"Por persona: ${por_persona:.2f}")

calculadora_propinas()
