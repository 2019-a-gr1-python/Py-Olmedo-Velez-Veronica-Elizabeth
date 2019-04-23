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