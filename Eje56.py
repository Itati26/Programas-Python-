MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

def texto_a_morse(texto):
    return ' '.join(MORSE_CODE.get(c.upper(), '') for c in texto)

def morse_a_texto(morse):
    morse_inverso = {v: k for k, v in MORSE_CODE.items()}
    return ''.join(morse_inverso.get(c, '') for c in morse.split())

print("1. Texto a Morse\n2. Morse a Texto")
opcion = input("Opción: ")
if opcion == '1':
    texto = input("Texto: ")
    print("Morse:", texto_a_morse(texto))
else:
    morse = input("Código Morse: ")
    print("Texto:", morse_a_texto(morse))
