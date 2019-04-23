import funciones_zapatos

def imprimir_encabezado_zapatos():
    print("\n*********************************************************************************************")
    print('%-10s%-20s%-20s%-15s%-15s%-20s' % ('Codigo', 'Categoria', 'Marca', 'Talla', 'Color', 'Precio'))
    print("*********************************************************************************************")

def imprimir_fila_zapato(zapato):
    print('%(codigo)-10s%(categoria)-20s%(marca)-20s%(talla)-15s%(color)-15s%(precio)-20s' % zapato)


def mostrar_lista_zapatos():
    print("\n***************************")
    print("*    Lista de zapatos:    *")
    print("***************************")
    lista = funciones_zapatos.obtener_lista_zapatos()
    imprimir_encabezado_zapatos()
    for zapato in lista:
        imprimir_fila_zapato(zapato)
    ordenar = True
    while (ordenar):
       respuesta = input("\nDesea ordenar la lista por medio de algún parámetro (Yes/No): ")
       if (True if respuesta == "Yes" else False):
           ordenar = True
           orden = input("Ordenar de forma ascendente -> 'A' o descendente -> 'D': ")
           if (True if orden == "A" else False):
               ordenar = False
           else:
               ordenar = True
           print("\n***************************") 
           print("* Parámetros para ordenar *")
           print("***************************")  
           print("0.- Código")
           print("1.- Categoria")
           print("2.- Marca")
           print("3.- Talla")
           print("4.- Color")
           print("5.- Precio")
           llave = input('Ingrese una opción: ')
           def llaves(value):
               try:
                   return {
                       0: 'codigo',
                       1: 'categoria',
                       2: 'marca',
                       3: 'talla',
                       4: 'color',
                       5: 'precio',
                   }[value]
               except KeyError:
                   print("Opción no definida")
           if (llave.isnumeric()):
               llave = int(llave)
               llave_a_ordennar = llaves(llave)
               def sortBy(elem):
                   return elem[llave_a_ordennar]
               imprimir_encabezado_zapatos()
               lista.sort(key=sortBy, reverse=ordenar)
               for zapato in lista:
                   imprimir_fila_zapato(zapato)
           else:
               ordenar = False
       else:
           ordenar = False

# mostar interfaz para la busqueda de datos
def buscar_zapato():
    print("\n***************************")
    print("*   Búsqueda de zapato:   *")
    print("***************************")
    codigo = input("Ingrese el codigo de zapato a buscar: ")
    zapato = funciones_zapatos.obtener_zapato_por_codigo(codigo)
    if zapato != None:
        imprimir_encabezado_zapatos()
        imprimir_fila_zapato(zapato)
    else:
        print(f"Zapato con código {codigo} no existe")


# mostar interfaz para la eliminación de datos
def eliminar_zapato():
    print("\n***************************")
    print("*    Eliminar zapato:     *")
    print("***************************")
    codigo = input("Ingrese el codigo del zapato a eliminar: ")
    funciones_zapatos.remover_zapato_por_codigo(codigo)

# mostar interfax para la actualización de datos
def actualizar_zapato():
    print("\n*******************************")
    print("* Modificar datos del zapato: *")
    print("*******************************")
    codigo = input("Ingrese el codigo del zapato a modificar: ")
    zapato = funciones_zapatos.obtener_zapato_por_codigo(codigo)
    def opciones(value):
        try:
            return {
                0: 'codigo',
                1: 'categoria',
                2: 'marca',
                3: 'talla',
                4: 'color',
                5: 'precio',
            }[value]
        except KeyError:
            print("Opción no definida")
    if zapato != None:
        imprimir_encabezado_zapatos()
        imprimir_fila_zapato(zapato)
        print("\n***************************")
        print("*       Opciones:         *")
        print("***************************")
        print("0.- Modificar categoria")
        print("1.- Modificar marca")
        print("2.- Modificar talla")
        print("3.- Modificar color")
        print("4.- Modificar precio")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            opcion_actualizar = int(read)
        try:
            llave_a_actualizar = opciones(opcion_actualizar)
            valor = input('Ingrese el nuevo valor: ')
            dato_a_actualizar = {
                llave_a_actualizar: valor
            }
            funciones_zapatos.actualizar_zapato_por_diccionario(zapato, dato_a_actualizar)
        except TypeError:
            print(f'Option {option}')
    else:
        print(f"El zapato con código {codigo} no existe")

# seleccionador de acciones principales
def acciones(value):
    try:
        return {
            0: None,
            1: funciones_zapatos.anadir_zapato,
            2: mostrar_lista_zapatos,
            3: buscar_zapato,
            4: eliminar_zapato,
            5: actualizar_zapato
        }[value]
    except KeyError:
        print("No existe esta acción")

# función principal
def main(option):
    while option != 0:
        print("\n***************************")
        print("*       Opciones:         *")
        print("***************************")
        print("1.- Ingresar zapato")
        print("2.- Mostrar lista de zapatos")
        print("3.- Buscar zapato")
        print("4.- Eliminar zapato")
        print("5.- Modificar datos")
        print("0.- Salir")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            option = int(read)
        try:
            acciones(option)()
        except TypeError:
            print(f'Option {option}')

main(-1)

