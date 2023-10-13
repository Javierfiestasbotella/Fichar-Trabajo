import os

def buscar_imagen_por_nombre(directorio, nombre):
    resultados = []
    for root, _, files in os.walk(directorio):
        for file in files:
            if nombre.lower() in file.lower() and file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                resultados.append(os.path.join(root, file))
    return resultados

directorio = input("Ingrese la ubicación del directorio para buscar imágenes: ")
nombre_imagen = input("Ingrese el nombre de la imagen que desea buscar: ")

resultados = buscar_imagen_por_nombre(directorio, nombre_imagen)

if resultados:
    print("Se encontraron las siguientes imágenes:")
    for resultado in resultados:
        print(resultado)
else:
    print("No se encontraron imágenes con ese nombre en el directorio especificado.")
