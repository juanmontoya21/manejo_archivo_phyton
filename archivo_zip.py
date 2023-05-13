import zipfile
import tarfile
"""
El manejo de archivos comprimidos es una habilidad importante para cualquier persona que trabaje con archivos digitales. Un archivo comprimido es un archivo que ha sido reducido en tamaño mediante la eliminación de redundancias y la utilización de algoritmos de compresión.

Existen varios formatos de archivos comprimidos, pero los más comunes son ZIP, RAR y 7Z. Para manejar archivos comprimidos, necesitará un software de descompresión, como WinZip, 7-Zip o WinRAR. Estos programas permiten abrir, descomprimir y crear archivos comprimidos.

Para descomprimir un archivo, simplemente haga clic derecho en el archivo y seleccione "Extraer aquí" o "Extraer en" en el menú contextual. Si está utilizando un software de descompresión, también puede hacer doble clic en el archivo para abrirlo en el programa y luego seleccionar la opción de extracción.

Para crear un archivo comprimido, seleccione los archivos que desea comprimir, haga clic derecho en ellos y seleccione "Agregar a archivo" o "Comprimir" en el menú contextual. Elija el formato de archivo que desee y especifique la ubicación donde desea guardar el archivo comprimido.

También puede agregar archivos a un archivo comprimido existente. Abra el archivo comprimido en su software de descompresión, seleccione "Agregar" o "Añadir" en el menú y luego seleccione los archivos que desea agregar.

Recuerde que la compresión de archivos puede reducir significativamente su tamaño, lo que puede facilitar su envío o almacenamiento. Sin embargo, algunos archivos, como imágenes y videos, ya están comprimidos y pueden no reducirse mucho más al comprimirlos.
"""
with zipfile.ZipFile("archivo.zip","w") as archivo_zip:
  archivo_zip.write("archivo1.txt")
  archivo_zip.write("archivo2.txt")
  archivo_zip.write("archivo2.txt")


# with tarfile.open("archivo.tar","w") as archivo_tar:
#   archivo_tar.add("archivo1.txt")
#   archivo_tar.add("archivo2.txt")
#   archivo_tar.add("archivo3.txt")

# with tarfile.open("archivo.tar","r") as archivo_tar:
#   archivo_tar.extractall()
