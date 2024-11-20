import json
'''
PROBLEMA:
----------
La aplicación permite gestionar un inventario de platos.
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

4. Usar algoritmos de ordenamiento para ver los platos
del mas barato al mas caro.

----------
'''

platos = []

class Plato:
    def __init__(self, nombre_plato, precio, stock):
        self.nombre_plato = nombre_plato
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        return f"Plato: {self.nombre_plato}, Stock: {self.stock}, Precio: ${self.precio}"

def cargar_platos():
    global platos
    try:
        with open('platos.txt', 'r') as file:
            data = json.load(file)
            platos = [Plato(p['nombre'], p['precio'], p['stock']) for p in data]
    except FileNotFoundError:
        platos = []

def guardar_platos():
    data = [{'nombre': p.nombre_plato, 'precio': p.precio, 'stock': p.stock} for p in platos]
    with open('platos.txt', 'w') as file:
        json.dump(data, file)

def agregar_plato():
    salir = 1
    while salir != 0:
        nombre_plato = input("Ingresa el nombre de el plato: ")
        stock = int(input("Ingresa el stock del plato: "))
        precio = float(input("Ingresa el precio del plato: "))
        
        plato = Plato(nombre_plato, precio, stock)
        platos.append(plato)
        guardar_platos()  # Guardar después de agregar
        
        salir = int(input("Ingresa 1 para agregar otro plato / 0 para salir: "))
    display_menu()

def ver_platos():
    print("\n---PLATOS AGREGADOS---\n")
    
    if len(platos) == 0:
        print("No hay platos para mostrar!")
    else:
        for plato in platos:
            print(plato)
    
    opcion = int(input("Ingresa 1 para volver || 2 para ordenar por menor precio: "))
    
    if opcion == 1:
        display_menu()
    elif opcion == 2:
        ordenar_por_precio()
        ver_platos()
    else:
        print("Opción no válida!")
        display_menu()

def eliminar_plato():
    print("\n---ELIMINAR PLATOS---\n")
    plato_eliminar = input("Ingresa el nombre del plato que deseas eliminar: ").lower()
    
    for i, plato in enumerate(platos):
        if plato.nombre_plato.lower() == plato_eliminar:
            platos.pop(i)
            guardar_platos()  # Guardar después de eliminar
            print(f"El plato '{plato_eliminar}' ha sido eliminado.")
            display_menu()
            return
    
    print("No se encontró ese plato!")
    display_menu()

def modificar_plato():
    print("\n---MODIFICAR PLATOS---")
    plato_modificar = input("Ingresa el nombre del plato que deseas modificar: ").lower()
    
    for plato in platos:
        if plato.nombre_plato.lower() == plato_modificar:
            plato.nombre_plato = input("Ingresa el nuevo nombre: ")
            plato.stock = int(input("Ingresa el nuevo stock: "))
            plato.precio = float(input("Ingresa el nuevo precio: "))
            guardar_platos()  # Guardar después de modificar
            print(f"El plato '{plato_modificar}' ha sido modificado!\n")
            display_menu()
            return
    
    print("No se encontró ese plato!")
    display_menu()

def ordenar_por_precio():
    platos.sort(key=lambda x: x.precio)
    guardar_platos()  # Guardar después de ordenar

def display_menu():
    salir = False
    while salir == False:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar platos")
        print("2. Ver platos")
        print("3. Modificar platos")
        print("4. Eliminar platos")
        print("5. Salir")
        
        try:
            opcion = int(input("\nSelecciona una opción: "))
            
            if opcion == 1:
                agregar_plato()
            elif opcion == 2:
                ver_platos()
            elif opcion == 3:
                modificar_plato()
            elif opcion == 4:
                eliminar_plato()
            elif opcion == 5:
                print("\n¡Hasta luego!")
                salir = True
            else:
                print("Opción no válida!")
        except ValueError:
            print("Por favor, ingresa un número válido!")

def main():
    cargar_platos()  # Cargar platos al inicio
    display_menu()

if __name__ == "__main__":
    main()