import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from product_selection.main_search import main as main_search
from product_selection.main_filter import main as main_filter

if __name__ == "__main__":
    choice = input("Selecciona el flujo a ejecutar (1: Búsqueda, 2: Filtrado): ")
    if choice == "1":
        asyncio.run(main_search())
    elif choice == "2":
        asyncio.run(main_filter())
    else:
        print("Opción no válida")