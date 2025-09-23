import qrcode

def generar_qr():
    texto = input("Texto/URL para QR: ")
    nombre_archivo = input("Nombre del archivo (sin extensión): ")
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(texto)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{nombre_archivo}.png")
    print(f"QR guardado como {nombre_archivo}.png")

generar_qr()
