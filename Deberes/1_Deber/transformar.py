def cadenatexto_a_diccionarioproveedor(line):
    partes_line = (line + "").replace("\n", "").split(';')
    proveedor = {
        'codigo': partes_line[0],
        'cod': partes_line[1],
        'nombre': partes_line[2],
        'cuidad': partes_line[3],
        'telf': partes_line[4]
    }
    return proveedor

def diccioanrioproveedor_a_cadenatexto(zapato):
    return f"{proveedor['codigo']};{proveedor['cod']};{proveedor['nombre']};{proveedor['ciudad']};{proveedor['telf']}"

def cadenatexto_a_diccionariozapato(linea):
    partes_linea = (linea + "").replace("\n", "").split(';')
    zapato = {
        'codigo': partes_linea[0],
        'categoria': partes_linea[1],
        'marca': partes_linea[2],
        'talla': int(partes_linea[3]),
        'color': partes_linea[4],
        'precio': float(partes_linea[5])
    }
    return zapato

def diccioanriozapato_a_cadenatexto(zapato):
    return f"{zapato['codigo']};{zapato['categoria']};{zapato['marca']};{zapato['talla']};{zapato['color']};{zapato['precio']}"


