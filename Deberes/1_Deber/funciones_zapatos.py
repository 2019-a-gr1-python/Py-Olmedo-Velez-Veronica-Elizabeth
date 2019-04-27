import manejo_archivos
import transformar

def anadir_proveedor():
    print("\n***************************")
    print("*     Añadir proveedor:   *")
    print("***************************")
    codigo = input("Ingrese id del proveedor: ")
    cod = input("Ingrese codigo de zapato: ")
    nombre = input("Ingrese nombre: ")
    ciudad = input("Ingrese cuidad: ")
    telf = input("Ingrese teléfono: ")
    proveedor = codigo + ";" + cod + ";" + nombre + ";" + ciudad + ";" + telf
    manejo_archivos.agregar_a_archivo('./proveedores.txt', 'a', proveedor)

def obtener_lista_proveedores():
    archivo_proveedor = manejo_archivos.leer_archivos('./proveedores.txt')
    proveedor = []
    for cadena in archivo_proveedor:
        proveedor.append(transformar.cadenatexto_a_diccionarioproveedor(cadena))
    return proveedor

def guardar_listadediccionarios_como_listadecadenadetexto(lista):
    lista_cadenas = []
    for proveedor in lista:
        cadena = transformar.diccioanrioproveedor_a_cadenatexto(proveedor)
        lista_cadenas.append(cadena)
    manejo_archivos.agregar_a_archivo('./proveedores.txt', 'w', *lista_cadenas)

def anadir_zapato():
    print("\n***************************")
    print("*     Añadir zapato:      *")
    print("***************************")
    codigo = input("Ingrese un codigo: ")
    categoria = input("Ingrese una categoria: ")
    marca = input("Marca: ")
    talla = input("Ingrese una la talla: ")
    color = input("Ingrese el color: ")
    precio = input("Ingrese el precio: ")
    shoe = codigo + ";" + categoria + ";" + marca + ";" + talla + ";" + color + ';' + precio
    manejo_archivos.agregar_a_archivo('./zapatos.txt', 'a', shoe)

def obtener_lista_zapatos():
    archivo_zapatos = manejo_archivos.leer_archivos('./zapatos.txt')
    zapato = []
    for cadena in archivo_zapatos:
        zapato.append(transformar.cadenatexto_a_diccionariozapato(cadena))
    return zapato

def obtener_zapato_por_codigo(codigo):
    lista = obtener_lista_zapatos()
    for zapato in lista:
        if zapato.get('codigo') == codigo:
            break
    else:
        zapato = None
    return zapato

def guardar_listadediccionarios_como_listadecadenadetexto(lista):
    lista_cadenas = []
    for zapato in lista:
        cadena = transformar.diccioanriozapato_a_cadenatexto(zapato)
        lista_cadenas.append(cadena)
    manejo_archivos.agregar_a_archivo('./zapatos.txt', 'w', *lista_cadenas)

def remover_zapato_por_codigo(codigo):
    lista = obtener_lista_zapatos()
    zapato_a_remover = obtener_zapato_por_codigo(codigo)
    if zapato_a_remover != None:
        lista.remove(zapato_a_remover)
    print(f'Eliminando zapato con código {codigo}')
    guardar_listadediccionarios_como_listadecadenadetexto(lista)

def actualizar_zapato_por_diccionario(zapato, dato_actualizado):
    lista = obtener_lista_zapatos()
    index = lista.index(zapato)
    zapato.update(dato_actualizado)
    lista[index] = zapato
    print(f"Actualizando zapato con código {zapato['codigo']}")
    guardar_listadediccionarios_como_listadecadenadetexto(lista)