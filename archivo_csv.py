import csv
#Python proporciona una biblioteca estándar para manejar archivos CSV (Comma-Separated Values). Para trabajar con archivos CSV en Python, se utiliza el módulo csv.
#El siguiente ejemplo muestra cómo abrir un archivo CSV, leer los datos y cerrar el archivo:

datos = [
    ["Nombre", "Apellido", "Edad"],
    ["Juan", "Pérez", 25],
    ["María", "Gómez", 30],
    ["Pedro", "López", 40]]

with open('archivo.csv','w') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    for fila in datos:
        escritor_csv.writerow(fila)
archivo_csv.close()

with open('archivo.csv','r') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)
archivo.close()

datos.append(["carlos","montoya",19])
print(datos)

with open('archivo.csv','a') as actualizar_archivo:
    actualizo_csv = csv.writer(actualizar_archivo)
    actualizo_csv.writerows(datos)