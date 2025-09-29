def generar_arte_ascii():
    formas = {
        "árbol": """
          *
         ***
        *****
       *******
      *********
         |||
         |||
        """,
        
        "casa": """
         /\\
        /  \\
       /____\\
       |    |
       |____|
        """,
        
        "corazón": """
         **   **
        **** ****
        *********
         *******
          *****
           ***
            *
        """,
        
        "estrella": """
            *
           ***
          *****
         *******
        *********
          |   |
          |   |
        """
    }
    
    print("Formas disponibles:", ", ".join(formas.keys()))
    forma = input("Elige una forma: ").lower()
    
    if forma in formas:
        print(formas[forma])
    else:
        print("Forma no disponible")

generar_arte_ascii()
