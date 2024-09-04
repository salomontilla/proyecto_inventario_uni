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
#funcion que agrega ingredientes y retorna la lista de ingredientes agregados
def agregarIngrediente ():
    ingredientes = []

    salir = 1
    while salir != 0:
        nombre_ingre= input("Ingresa el nombre del ingrediente para agregar: ")
        precio = float(input("Ingresa el precio del ingrediente: "))   
        ingre = {
        "nombre" : nombre_ingre,
        "precio" : precio
        }
        ingredientes.append(ingre)
        print("Producto Agregado!")

        sal = int(input("Presiona 1 para agregar otro ingrediente, 0 para salir: "))
        if(sal == 0):
            salir = 0
    return ingredientes


if __name__ == "__main__":
    print(agregarIngrediente())    