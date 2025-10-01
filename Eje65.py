import requests

def verificar_sitio_web():
    url = input("URL del sitio web: ")
    
    try:
        respuesta = requests.get(url, timeout=10)
        if respuesta.status_code == 200:
            print(f"El sitio está ACTIVO (Código: {respuesta.status_code})")
        else:
            print(f"El sitio responde con código: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar: {e}")

verificar_sitio_web()
