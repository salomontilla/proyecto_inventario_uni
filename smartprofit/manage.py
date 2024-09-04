#!/usr/bin/env python
"""
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
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartprofit.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
