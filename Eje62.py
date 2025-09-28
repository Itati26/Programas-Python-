import datetime

def obtener_horoscopo(signo, fecha):
    predicciones = {
        'aries': "Hoy es un día para tomar iniciativa. La energía está de tu lado.",
        'tauro': "Concéntrate en la estabilidad. Las decisiones financieras serán importantes.",
        'géminis': "Día de comunicación. Expresa tus ideas con claridad.",
        'cáncer': "Las emociones guiarán tu día. Escucha tu intuición.",
        'leo': "Brilla con tu creatividad. Es tu momento de destacar.",
        'virgo': "Enfócate en los detalles. La organización será clave.",
        'libra': "Busca el equilibrio en tus relaciones. La armonía es importante.",
        'escorpio': "Día de transformación. Aprovecha para renovarte.",
        'sagitario': "La aventura te llama. Explora nuevas posibilidades.",
        'capricornio': "Trabaja en tus metas a largo plazo. La paciencia da frutos.",
        'acuario': "Las ideas innovadoras fluyen. Comparte tu perspectiva única.",
        'piscis': "La creatividad está en su punto máximo. Sueña en grande."
    }
    return predicciones.get(signo.lower(), "Signo no reconocido")

signo = input("Tu signo zodiacal: ")
fecha = datetime.date.today()
print(f"\nHoróscopo para {signo.capitalize()} - {fecha}:")
print(obtener_horoscopo(signo, fecha))
