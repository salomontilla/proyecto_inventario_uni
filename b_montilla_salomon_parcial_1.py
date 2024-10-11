'''
PROBLEMA:
----------
La aplicación permite gestionar un inventario de platos, 
calcular el costo de los platos en función 
de los platos utilizados, y determinar el 
precio ideal de venta para maximizar las ganancias.
----------
TECNOLOGIAS A UTILIZAR:
----------
- Python
----------
PLANIFICACION:
----------
Gestión de platos:
1. Agregar platos: El usuario puede añadir nuevos 
platos al inventario con sus costos respectivos.

2. Actualizar platos: Modificar la información de 
un plato existente (precio, cantidad, etc.).

3. Eliminar platos: Remover platos que ya no 
se utilizan.

Cálculo de Costos y Precios:
1. Calcular Costo de Plato: Determinar el costo total de un 
plato basado en la receta y los precios de los platos.

2. Establecer Precio de Venta: Proponer un precio de venta para el plato basado 
en el costo y el margen de ganancia deseado.
----------
'''
#Esta funcion despliega el menú de opciones
def display_menu():
    salir = 0
    while salir != 1:
        print("---INVENTARIO DE PLATOS---\n")
        print(" 1. Agregar plato\n 2. Eliminar plato\n 3. Modificar Plato\n 4. Ver Platos\n 5. Salir")
        opcion = int(input("\nSelecciona una opción: "))
        match opcion:
            case 1:
                agregrar()
                break
            case 2:
                if len(platos) != 0:
                    eliminar()
                else:
                    print("No hay platos para eliminar!\n")
                    display_menu()
                break
            case 3:
                if len(platos) != 0:
                    modificar()
                else:
                    print("No hay platos para modificar!\n")
                    display_menu()
                break
            case 4:
                ver_platos()
                break
            case 5:
                break
            case _:
                print("Esa opción no está disponible!\n")

#Esta funcion permite agregrar platos al inventario
platos = []
def agregrar():
    salir = 1
    while salir != 0:
        nombre_ingre = input("Ingresa el nombre de el plato: ")
        cantidad = int(input("Ingresa el stock del plato: "))
        precio = float(input("Ingresa el precio del plato: "))
        plato = [nombre_ingre, cantidad, precio]
        platos.append(plato)
        
        salir = int(input("Ingresa 1 para agregar otro plato / 0 para salir: "))
        if salir == 0:
            display_menu()
            salir = 0

# Esta función permite ver los platos en el inventario
def ver_platos():
    print("\n---PLATOS AGREGADOS---\n")
    
    if len(platos) == 0:
        print("No hay platos para mostrar!")
    else:
        # Mostrar platos sin ordenar
        for plato in platos:
            print(f"Nombre: {plato[0]}, Cantidad: {plato[1]}, Precio: {plato[2]:.2f}\n")
    
    opcion = int(input("Ingresa 1 para volver || 2 para ordenar por menor precio: "))
    
    if opcion == 1:
        display_menu()
    elif opcion == 2:
        ordenar_por_precio()
        ver_platos()
    else:
        print("Opción no válida!")
        display_menu()

#Esta funcion permite eliminar platos del inventario     
def eliminar():
    print("\n---ELIMINAR PLATOS---\n")
    platoEliminar = input("Ingresa el nombre del plato que deseas eliminar: ").lower()
    #Busqueda de plato
    for i, plato in enumerate(platos):
        if plato[0].lower() == platoEliminar:
            platos.pop(i)
            print(f"El plato '{platoEliminar}' ha sido eliminado.")
            display_menu()
        else:
            print("No se encontró ese plato!")
            display_menu()

#Esta funcion permite modificar los platos del inventario
def modificar():
    print("\n---MODIFICAR PLATOS---")
    platoModificar = input("Ingresa el nombre del plato que deseas modificar: ").lower()
    for plato in enumerate(platos):
        if plato[0].lower() == platoModificar:
            plato[0] = input("Ingresa el nuevo nombre: ")
            plato[1] = int(input("Ingresa el nuevo stock: "))
            plato[2] = float(input("Ingresa el nuevo precio: "))
            print(f"El plato '{platoModificar}' ha sido modificado!\n")
            display_menu()
        else:
            print("No se encontró ese plato!")
            display_menu()

# Algoritmo de ordenamiento por seleccion del precio
def ordenar_por_precio():
    n = len(platos)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if platos[j][2] < platos[min_idx][2]:  # Comparando el precio
                min_idx = j
        platos[i], platos[min_idx] = platos[min_idx], platos[i]  # Intercambiar platos
if __name__ == "__main__":
    display_menu()
