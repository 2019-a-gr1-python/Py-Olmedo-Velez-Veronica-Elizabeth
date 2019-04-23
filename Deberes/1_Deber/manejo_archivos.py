# 1) Ingresar un registro
def agregar_a_archivo(path, option, *lineas_a_escribir):
    try:
        archivo = open(path, option)
        for linea in lineas_a_escribir:
            archivo.write(linea + '\n')
        archivo.close()
        print('Guardado con éxito')
    except Exception as e:
        print(e)


def leer_archivos(path):
    try:
        lineas = []
        archivo = open(path)  # Defecto es 'r'
        arreglo_lienas_archivo = archivo.readlines()
        for linea in arreglo_lienas_archivo:
            lineas.append(linea)
        archivo.close()
        return lineas
    except Exception:
        print("No se puede leer el archivo: " + path)