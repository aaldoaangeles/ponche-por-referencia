import qrcode

def generar_qr(link, nombre_salida):
    img = qrcode.make(link)
    img.save(f"{nombre_salida}.png")
    print(f"QR generado con éxito: {nombre_salida}.png")


if __name__ == "__main__":
    link = input("Introduce el link para el QR: ")
    nombre = input("Nombre del archivo de salida (sin extensión): ")
    generar_qr(link, nombre)
