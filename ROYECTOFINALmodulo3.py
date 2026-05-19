import json


videojuegos_iniciales = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}

# Cargar el inventario desde el archivo JSON al iniciar el programa
def cargar_inventario_desde_json():
    try:
        with open("videojuegos_iniciales.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Archivo de inventario no encontrado. Iniciando con inventario vacío.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Iniciando con inventario vacío.")
        return {}



# Función para mostrar el menú principal y manejar la navegación entre opciones
def menu():
    while True:
        menu_principal = input("""===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir

Seleccione una opción: """)

        match menu_principal:
            case "1":
                agregar_videojuego(videojuegos_iniciales)
            case "2":
                mostrar_inventario(videojuegos_iniciales)
            case "3":
                buscar_videojuego(videojuegos_iniciales)
            case "4":
                actualizar_precio(videojuegos_iniciales)
            case "5":
                registrar_venta(videojuegos_iniciales)
            case "6":
                mostrar_estadisticas(videojuegos_iniciales)
            case "7":
                eliminar_videojuego(videojuegos_iniciales)
            case "8":
                print("¡Gracias por usar el sistema de gestión de la tienda de videojuegos! ¡Hasta luego!")
                break
            case _:
                print("Opción no válida, por favor seleccione una opción del 1 al 8.")

# Función para agregar un nuevo videojuego al inventario con validaciones
def agregar_videojuego(videojuegos):
    while True:
        codigo = input("Ingrese el código del videojuego: ").strip().upper()
        if codigo in videojuegos:
            print("Error: El código ya existe. Por favor ingrese un código único.")
            continue
        if not codigo:
            print("Error: El código no puede estar vacío.")
            continue
        break

    while True:
        nombre = input("Ingrese el nombre del videojuego: ").strip().capitalize()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            continue
        break

    while True:
        plataforma = input("Ingrese la plataforma del videojuego: ").strip().capitalize()
        if not plataforma:
            print("Error: La plataforma no puede estar vacía.")
            continue
        break

    while True:
        try:
            precio = float(input("Ingrese el precio del videojuego (en pesos): "))
            if precio <= 0:
                print("Error: El precio debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible del videojuego: "))
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un número entero válido para la cantidad.")

    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }
    print(f"Videojuego '{nombre}' agregado exitosamente con código {codigo}.")

# Función para mostrar el inventario completo con formato de tienda/tabla

def mostrar_inventario(videojuegos):
    if not videojuegos:
        print("El inventario está vacío.")
        return

    print(f"{'Código':<10} {'Nombre':<30} {'Plataforma':<20} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 80)
    for codigo, info in videojuegos.items():
        print(f"{codigo:<10} {info['nombre']:<30} {info['plataforma']:<20} ${info['precio']:<10,.2f} {info['cantidad']:<10}")

# Función para buscar un videojuego por código con validación
def buscar_videojuego(videojuegos):
    codigo = input("Ingrese el código del videojuego a buscar: ").strip().upper()
    if codigo in videojuegos:
        info = videojuegos[codigo]
        print(f"Información del videojuego '{info['nombre']}':")
        print(f"Plataforma: {info['plataforma']}")
        print(f"Precio: ${info['precio']:.2f}")
        print(f"Cantidad disponible: {info['cantidad']}")
    else:
        print("Videojuego no encontrado con el código proporcionado.")

# Función para actualizar el precio de un videojuego con validación
def actualizar_precio(videojuegos):
    codigo = input("Ingrese el código del videojuego para actualizar el precio: ").strip().upper()
    if codigo in videojuegos:
        while True:
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio del videojuego (en pesos): "))
                if nuevo_precio <= 0:
                    print("Error: El precio debe ser mayor a 0.")
                    continue
                break
            except ValueError:
                print("Error: Por favor ingrese un número válido para el precio.")
        videojuegos[codigo]['precio'] = nuevo_precio
        print(f"Precio del videojuego '{videojuegos[codigo]['nombre']}' actualizado a ${nuevo_precio:.2f}.")
    else:
        print("Videojuego no encontrado con el código proporcionado.")

# Función para registrar una venta con validación de stock y descuento inteligente

def registrar_venta(videojuegos):
    codigo = input("Ingrese el código del videojuego a vender: ").strip().upper()
    if codigo in videojuegos:
        while True:
            try:
                cantidad_vender = int(input("Ingrese la cantidad a vender: "))
                if cantidad_vender <= 0:
                    print("Error: La cantidad a vender debe ser mayor a 0.")
                    continue
                if cantidad_vender > videojuegos[codigo]['cantidad']:
                    print(f"Error: No hay suficiente stock. Cantidad disponible: {videojuegos[codigo]['cantidad']}.")
                    continue
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido para la cantidad.")

        precio_unitario = videojuegos[codigo]['precio']
        total_venta = precio_unitario * cantidad_vender

        # Aplicar descuento
        if total_venta > 500000:
            descuento = total_venta * 0.10
            total_venta -= descuento
            print(f"¡Descuento aplicado! Descuento: ${descuento:.2f}")

        # Actualizar inventario
        videojuegos[codigo]['cantidad'] -= cantidad_vender

        # Generar factura
        print("\n===== FACTURA DE VENTA =====")
        print(f"Juego: {videojuegos[codigo]['nombre']}")
        print(f"Precio unitario: ${precio_unitario:.2f}")
        print(f"Cantidad: {cantidad_vender}")
        print(f"Total: ${total_venta:.2f}")
        print("============================\n")
        print("¡Venta registrada exitosamente!")
    else:
        print("Videojuego no encontrado con el código proporcionado.")

    


# Función para mostrar estadísticas del inventario
def mostrar_estadisticas(videojuegos):
    if not videojuegos:
        print("El inventario está vacío. No hay estadísticas para mostrar.")
        return

    total_videojuegos = len(videojuegos)
    valor_total_inventario = sum(info['precio'] * info['cantidad'] for info in videojuegos.values())
    videojuego_mas_costoso = max(videojuegos.values(), key=lambda x: x['precio'])
    videojuego_mayor_cantidad = max(videojuegos.values(), key=lambda x: x['cantidad'])
    promedio_precios = sum(info['precio'] for info in videojuegos.values()) / total_videojuegos

    print("\n===== ESTADÍSTICAS DEL INVENTARIO =====")
    print(f"Total de videojuegos registrados: {total_videojuegos}")
    print(f"Valor total insumos (videojuegos): ${valor_total_inventario:.2f}")
    print(f"Videojuego más costoso: {videojuego_mas_costoso['nombre']} (${videojuego_mas_costoso['precio']:.2f})")
    print(f"Mayor cantidad disponible: {videojuego_mayor_cantidad['nombre']} ({videojuego_mayor_cantidad['cantidad']} unidades)")
    print(f"Promedio de precios de todos los juegos: ${promedio_precios:.2f}")
    print("======================================\n")

# Función para eliminar un videojuego del inventario
def eliminar_videojuego(videojuegos):
    codigo = input("Ingrese el código del videojuego a eliminar: ").strip().upper()
    if codigo in videojuegos:
        nombre_eliminado = videojuegos[codigo]['nombre']
        del videojuegos[codigo]
        print(f"Videojuego '{nombre_eliminado}' eliminado exitosamente.")
    else:
        print("Videojuego no encontrado con el código proporcionado.")






# -----------------------------------------------------------------------------
# 9. EJEMPLOS DE EJECUCIÓN
# -----------------------------------------------------------------------------
cargar_inventario_desde_json()
menu()


# para guardar el inventario en un archivo JSON

videojuegos_iniciales_json = json.dumps(videojuegos_iniciales, indent=4)
with open("videojuegos_iniciales.json", "w") as file:
    file.write(videojuegos_iniciales_json)



