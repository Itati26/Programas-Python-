print("🎥 RECOMENDADOR DE PELÍCULAS")

try:
    edad = int(input("¿Cuántos años tienes? "))
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad < 7:
        print("📽️ Recomendamos: Películas AA (aptas para todos)")
        print("🍿 Ejemplos: Toy Story, Frozen, Buscando a Nemo")
    elif edad < 13:
        print("📽️ Recomendamos: Películas A (aptas para todo público)")
        print("🍿 Ejemplos: Harry Potter, Spider-Man, Cars")
    elif edad < 16:
        print("📽️ Recomendamos: Películas B (adolescentes 12+)")
        print("🍿 Ejemplos: Avengers, Jurassic Park, Star Wars")
    elif edad < 18:
        print("📽️ Recomendamos: Películas B15 (15 años+)")
        print("🍿 Ejemplos: Joker, Deadpool, John Wick")
    else:
        print("📽️ Recomendamos: Películas C (adultos 18+)")
        print("🍿 Ejemplos: El Padrino, Pulp Fiction, Taxi Driver")
        
except ValueError:
    print("❌ Ingresa una edad válida")
