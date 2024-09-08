'''
PROBLEMA:
----------
La aplicación permite gestionar un inventario de ingredientes, 
calcular el costo de los platos en función 
de los ingredientes utilizados, y determinar el 
precio ideal de venta para maximizar las ganancias.
----------
TECNOLOGIAS A UTILIZAR:
----------
- Python
- Django
- Sqlite
----------
PLANIFICACION:
----------
Gestión de Ingredientes:
1. Agregar Ingredientes: El usuario puede añadir nuevos 
ingredientes al inventario con sus costos respectivos.

2. Actualizar Ingredientes: Modificar la información de 
un ingrediente existente (precio, cantidad, etc.).

3. Eliminar Ingredientes: Remover ingredientes que ya no 
se utilizan.

Cálculo de Costos y Precios:
1. Calcular Costo de Plato: Determinar el costo total de un 
plato basado en la receta y los precios de los ingredientes.

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
                eliminar()
                break
            case 3:
                modificar()
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
        plato = {"nombre":nombre_ingre, "cantidad":cantidad, "precio":precio}
        platos.append(plato)
        
        salir = int(input("Ingresa 1 para agregar otro plato / 0 para salir: "))
        if salir == 0:
            display_menu()
            salir = 0

def ver_platos():
    print("---PLATOS AGREGADOS---\n")
    print(platos)
def eliminar():
    print("eliminar")
def modificar():
    print("modificar")
if __name__ == "__main__":
    display_menu()
