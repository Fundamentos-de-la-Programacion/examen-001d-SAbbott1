#Examen 
#Sebastian Abbott 
#Forma H

def leer_opcion():
    while True:
        entrada = input("Ingrese una opcion: ")
        try:
            opcion = int(entrada)
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida.")
        except ValueError:
            print("Debe seleccionar una opcion valida.")

def no_vacio(dato):
    return len(dato.strip()) > 0

def validar_entero(valor):
    try:
        int(valor) > 0
    except ValueError:
        return False
    
def validar_negativo(valor):
    try:
        return int(valor) >= 0
    except ValueError:
        return False
        
def validar_clasificacion(clasificacion):
    return clasificacion() in ['S', 'M', 'L']

def validar_codigo(codigo, tamano):
    return codigo.upper() in [clasificacion.upper() for clasificacion in tamano.keys()]

def unidades_tipo(rama, arreglos, bodega):
    total = 0
    for codigo in rama:
        if rama[1].lower() == arreglos.lower():
            total += bodega[codigo][1]
    print(f"El total de stock disponible es {total}")

def busqueda_precio(p_min, p_max, unidades, temporada):
    encontrados = []
    for arreglos, bodega in arreglos.items():
        precio, arreglos = bodega
        if p_min <= precio <= p_max and temporada > 0: 
            tipo = unidades[arreglos][0]
            encontrados.append("f{tipo}--{arreglos}")

def actualizar_precio(codigo, nuevo_precio, bodega):
    if validar_clasificacion(codigo, bodega):
        for clasificacion in bodega.keys():
            if clasificacion.upper() == codigo.upper():
                bodega[clasificacion][0] = nuevo_precio
                return True
    return False

def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades):
    if validar_clasificacion(arreglo, unidades):
        return False
    unidades[arreglo.upper()] = [codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada]
    bodega[arreglo] = [precio, unidades]
    return True

def eliminar_arreglo(codigo, arreglos, bodega):
    if validar_clasificacion(codigo,arreglos):
        for x in list(bodega.keys()):
            if x.upper() == codigo.upper():
                del arreglos[x]
                del bodega[x]
                return True
    return False

def main():
    arreglos = {
'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}
bodega = {
'FLO1': [15990, 8],
'FLO2': [29990, 3],
'FLO3': [9990, 12],
'FLO4': [24990, 5],
'FLO5': [19990, 0],
'FLO6': [22990, 6],
}

while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

    opcion = leer_opcion()

    if opcion == -1: 
        print("Ingrese una opcion valida")
    
    elif opcion == 1: 
        option = input("Ingrese una opcion: ")
        validar_codigo(codigo, arreglo, bodega)
    
    elif opcion == 2:
        try:
            p_min = int(input("Ingrese el precio minimo: "))
            p_max = int(input("Ingrese el precio maximo: "))
            busqueda_precio(p_min, p_max, bodega, arreglo)
        except ValueError:
            print("Ingrese un valor entero")

    elif opcion == 3:
        arreglo = ("Ingrese el codigo de la flor: ")
        precio = int(input("Ingrese el precio de la flor: "))
        if actualizar_precio(arreglo, precio, bodega):
            print("Precio actualizado")
        else:
            print("El codigo de la planta no existe.")
        if input("Desea actualizar el precio? (s/n): ").lower() != 's' 'n':
            break

    elif opcion == 4:
        codigo = input("Ingrese el arreglo que desea agregar: ")
        if not validar_clasificacion(codigo, bodega, arreglo):
            arreglo1 = input("Ingrese codigo de arreglo: ")
            nombre1 = input("Ingrese nombre: ")
            tipo1 = input("Ingrese tipo: ")
            color1 = input("Ingrese color principal: ")
            tamano1 = input("Ingrese tamaño (S/M/L): ")
            tarjeta1 = input("¿Incluye tarjeta? (s/n): ")
            temporada1 = input("Ingrese temporada: ")
            precio1 = int(input("Ingrese precio: "))
            unidades1= int(input("Ingrese unidades: "))
            if agregar_arreglo(codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades):
                print("Arreglo agregado.")
            else:
                print("El arreglo ya estaba agregado anteriormente.")
        
    elif opcion == 5:
        codigo = input("Ingrese arreglo que desea eliminar: ")
        if eliminar_arreglo(codigo, arreglo, bodega):
            print("Arreglo eliminado.")
        else:
            print("El arreglo no existe.")

    elif opcion == 6:
        print("Programa finalizado. ")
        break

main()










    









            







    
