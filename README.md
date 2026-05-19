# PROYECTO FINAL - MÓDULO 3: SISTEMA DE GESTIÓN DE TIENDA DE VIDEOJUEGOS
---
# Docente: Carlos Fadul
# Fecha: 14/05/2026
---

# -----------------------------------------------------------------------------
# 1. OBJETIVO GENERAL DEL PROYECTO
# -----------------------------------------------------------------------------
"""
Desarrollar un programa completo en Python que permita administrar el inventario
y las ventas de una tienda de videojuegos. Este proyecto integrador tiene como
meta aplicar de manera práctica todos los conceptos aprendidos en el módulo 3:

✓ Variables y tipos de datos
✓ Condicionales (if, elif, else)
✓ Ciclos (while, for)
✓ Funciones con parámetros y retorno
✓ Colecciones (diccionarios y listas)
✓ Validación de datos
✓ Cálculos básicos

El resultado final será un sistema de consola completamente funcional que
demuestre el dominio de los fundamentos de Python.
"""

# -----------------------------------------------------------------------------
# 2. CONTEXTO Y ANÁLISIS DEL PROBLEMA
# -----------------------------------------------------------------------------
"""
CONTEXTO EMPRESARIAL:
Una tienda de videojuegos necesita un sistema informático para gestionar su
inventario y controlar las ventas diarias. Actualmente, toda la gestión se
realiza manualmente, lo que genera errores, pérdida de tiempo y dificultades
para obtener estadísticas de ventas.

PROBLEMA A RESOLVER:
- Controlar el inventario de videojuegos de manera automática
- Gestionar ventas con validaciones de stock
- Generar reportes y estadísticas de negocio
- Mantener la integridad de los datos

ESTRUCTURA DE DATOS PRINCIPAL:
Cada videojuego se representa como un diccionario anidado con la siguiente
información esencial para el negocio:
"""

# -----------------------------------------------------------------------------
# 3. ESPECIFICACIONES TÉCNICAS - ESTRUCTURA DE DATOS
# -----------------------------------------------------------------------------
# Modelo de datos para cada videojuego
videojuego_modelo = {
    "codigo": "VG001",           # Identificador único (string)
    "nombre": "FIFA 26",         # Nombre del juego (string)
    "plataforma": "PlayStation 5", # Plataforma (string)
    "precio": 250000,            # Precio en pesos (int/float)
    "cantidad": 10               # Unidades disponibles (int)
}

# -----------------------------------------------------------------------------
# 4. ENUNCIADO DETALLADO DEL PROYECTO
# -----------------------------------------------------------------------------
"""
DESARROLLAR UN SISTEMA DE GESTIÓN que permita a la tienda de videojuegos:

1. ADMINISTRAR INVENTARIO:
   - Agregar nuevos videojuegos al catálogo
   - Consultar el inventario completo
   - Buscar productos específicos
   - Actualizar precios
   - Eliminar productos obsoletos

2. GESTIONAR VENTAS:
   - Registrar ventas con validación de stock
   - Generar facturas automáticas
   - Controlar inventario en tiempo real

3. OBTENER ESTADÍSTICAS:
   - Reportes de inventario
   - Análisis de precios y stock
   - Métricas de negocio

El sistema debe funcionar a través de un menú interactivo que permita al
usuario navegar entre las diferentes opciones de manera intuitiva.
"""

# -----------------------------------------------------------------------------
# 5. INTERFAZ DE USUARIO - MENÚ PRINCIPAL
# -----------------------------------------------------------------------------
"""
El programa debe mostrar repetidamente el siguiente menú hasta que el usuario
elija salir:

===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir

Seleccione una opción (1-8): _
"""

# -----------------------------------------------------------------------------
# 6. REQUISITOS FUNCIONALES DETALLADOS
# -----------------------------------------------------------------------------
"""
Cada opción del menú debe implementar las siguientes funcionalidades:
"""

# 6.1 AGREGAR VIDEOJUEGO
"""
Función: agregar_videojuego(videojuegos)
Descripción: Solicita datos al usuario y agrega un nuevo videojuego al inventario

ENTRADAS (input del usuario):
- Código del videojuego
- Nombre del juego
- Plataforma
- Precio
- Cantidad inicial

VALIDACIONES REQUERIDAS:
✓ Código único (no debe existir en el diccionario)
✓ Precio > 0
✓ Cantidad >= 0
✓ Nombre y plataforma no vacíos

SALIDA:
- Mensaje de confirmación si se agrega correctamente
- Mensaje de error si hay validaciones fallidas
"""

# 6.2 MOSTRAR INVENTARIO
"""
Función: mostrar_inventario(videojuegos)
Descripción: Muestra todos los videojuegos registrados en formato tabular

ENTRADAS:
- Diccionario de videojuegos

SALIDA:
- Lista formateada con todos los productos
- Mensaje especial si el inventario está vacío
"""

# 6.3 BUSCAR VIDEOJUEGO POR CÓDIGO
"""
Función: buscar_videojuego(videojuegos)
Descripción: Busca y muestra la información completa de un videojuego

ENTRADAS:
- Código del videojuego a buscar

SALIDA:
- Información completa del producto si existe
- Mensaje de "no encontrado" si no existe
"""

# 6.4 ACTUALIZAR PRECIO
"""
Función: actualizar_precio(videojuegos)
Descripción: Permite modificar el precio de un videojuego existente

ENTRADAS:
- Código del videojuego
- Nuevo precio

VALIDACIONES:
✓ El videojuego debe existir
✓ Nuevo precio > 0

SALIDA:
- Confirmación de actualización exitosa
"""

# 6.5 REGISTRAR VENTA
"""
Función: registrar_venta(videojuegos)
Descripción: Procesa una venta y actualiza el inventario

ENTRADAS:
- Código del videojuego
- Cantidad a vender

VALIDACIONES:
✓ El videojuego debe existir
✓ Cantidad disponible >= cantidad solicitada
✓ Cantidad a vender > 0

ACCIONES:
- Restar cantidad del inventario
- Calcular total de la venta
- Mostrar factura detallada

SALIDA:
Factura con:
- Nombre del juego
- Precio unitario
- Cantidad vendida
- Total a pagar
"""

# 6.6 MOSTRAR ESTADÍSTICAS
"""
Función: mostrar_estadisticas(videojuegos)
Descripción: Genera reportes estadísticos del inventario

MÉTRICAS A CALCULAR:
✓ Total de videojuegos registrados
✓ Valor total del inventario (suma de precio * cantidad)
✓ Videojuego más costoso
✓ Videojuego con mayor cantidad disponible
✓ Promedio de precios de todos los juegos

SALIDA:
- Reporte formateado con todas las estadísticas
"""

# 6.7 ELIMINAR VIDEOJUEGO
"""
Función: eliminar_videojuego(videojuegos)
Descripción: Remueve un videojuego del inventario

ENTRADAS:
- Código del videojuego a eliminar

VALIDACIONES:
✓ El videojuego debe existir

SALIDA:
- Confirmación de eliminación
- Mensaje de error si no existe
"""

# 6.8 SALIR
"""
Función: menu() debe terminar el programa
Descripción: Finaliza la ejecución del programa
"""

# -----------------------------------------------------------------------------
# 7. REQUISITOS TÉCNICOS OBLIGATORIOS
# -----------------------------------------------------------------------------
"""
FUNCIONES QUE DEBES IMPLEMENTAR (mínimo obligatorio):

def agregar_videojuego(videojuegos: dict) -> None:
    pass

def mostrar_inventario(videojuegos: dict) -> None:
    pass

def buscar_videojuego(videojuegos: dict) -> None:
    pass

def actualizar_precio(videojuegos: dict) -> None:
    pass

def registrar_venta(videojuegos: dict) -> None:
    pass

def mostrar_estadisticas(videojuegos: dict) -> None:
    pass

def eliminar_videojuego(videojuegos: dict) -> None:
    pass

def menu() -> None:
    pass

RECOMENDACIONES DE IMPLEMENTACIÓN:
- Usa funciones puras cuando sea posible
- Implementa validaciones robustas
- Maneja errores de manera elegante
- Usa nombres descriptivos para variables y funciones
- Comenta tu código adecuadamente
"""

# -----------------------------------------------------------------------------
# 8. DATOS DE PRUEBA INICIALES
# -----------------------------------------------------------------------------
"""
Para facilitar las pruebas, inicia tu programa con este diccionario:
"""
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

# -----------------------------------------------------------------------------
# 9. EJEMPLOS DE EJECUCIÓN
# -----------------------------------------------------------------------------
"""
EJEMPLO 1: Agregar un videojuego
=====================================
Código: VG004
Nombre: God of War Ragnarök
Plataforma: PlayStation 5
Precio: 280000
Cantidad: 12

Resultado: "Videojuego agregado exitosamente"

EJEMPLO 2: Registrar una venta
=====================================
Código del videojuego: VG001
Cantidad a vender: 2

Resultado - Factura:
==================
Juego: FIFA 26
Precio unitario: $250,000
Cantidad: 2
Total: $500,000
==================
¡Venta registrada exitosamente!

EJEMPLO 3: Mostrar estadísticas
=====================================
Estadísticas del Inventario:
-----------------------------
Total de videojuegos: 3
Valor total del inventario: $6,950,000
Videojuego más costoso: FIFA 26 ($250,000)
Mayor cantidad disponible: FIFA 26 (10 unidades)
Promedio de precios: $230,000
"""

# -----------------------------------------------------------------------------
# 10. RETOS ADICIONALES (OPCIONALES - PARA NIVEL AVANZADO)
# -----------------------------------------------------------------------------
"""
Si completas el proyecto básico antes del tiempo estimado, implementa estas
funcionalidades adicionales:

🔹 BÚSQUEDA AVANZADA:
- Buscar videojuegos por plataforma
- Buscar videojuegos por rango de precios

🔹 ALERTAS DE INVENTARIO:
- Mostrar videojuegos con inventario bajo (cantidad < 3)
- Alertas automáticas al registrar ventas

🔹 DESCUENTOS INTELIGENTES:
- Aplicar 10% de descuento en ventas mayores a $500.000
- Descuentos por cantidad (3x2, etc.)

🔹 HISTORIAL DE VENTAS:
- Guardar todas las ventas en una lista de diccionarios
- Mostrar historial completo de ventas
- Calcular videojuego más vendido

🔹 EXPORTACIÓN DE DATOS:
- Guardar inventario en archivo JSON
- Generar reportes en formato texto
"""

# -----------------------------------------------------------------------------
# 11. CONCEPTOS FUNDAMENTALES QUE PRACTICARÁS
# -----------------------------------------------------------------------------
"""
Este proyecto te permitirá demostrar dominio de:

📊 ESTRUCTURAS DE DATOS:
- Diccionarios anidados
- Listas para almacenamiento temporal
- Manipulación de colecciones

🔧 FUNCIONES Y MODULARIDAD:
- Funciones con parámetros y retorno
- Separación de responsabilidades
- Reutilización de código

⚡ CONTROL DE FLUJO:
- Condicionales (if/elif/else)
- Ciclos while para menús
- Ciclos for para iteración

✅ VALIDACIÓN Y MANEJO DE ERRORES:
- Validación de entrada de usuario
- Manejo de casos edge
- Mensajes de error informativos

📈 LÓGICA DE NEGOCIO:
- Cálculos matemáticos (totales, promedios)
- Lógica condicional compleja
- Algoritmos de búsqueda y filtrado
"""

# -----------------------------------------------------------------------------
# 12. CRITERIOS DE EVALUACIÓN
# -----------------------------------------------------------------------------
"""
El proyecto será evaluado según:

✅ FUNCIONALIDAD (60%):
- Todas las funciones implementadas correctamente
- Validaciones funcionando
- Menú operativo

✅ CÓDIGO (25%):
- Legibilidad y organización
- Comentarios adecuados
- Nombres descriptivos
- Estructura modular

✅ VALIDACIONES (10%):
- Manejo correcto de errores
- Mensajes informativos
- Casos edge considerados

✅ CREATIVIDAD (5%):
- Funcionalidades adicionales implementadas
- Interfaz de usuario mejorada
"""

# -----------------------------------------------------------------------------
# 13. ENTREGA Y PRESENTACIÓN
# -----------------------------------------------------------------------------
"""
INSTRUCCIONES DE ENTREGA:
1. El código debe estar bien comentado
2. Incluir datos de prueba iniciales
3. El programa debe ejecutarse sin errores
4. Demostrar todas las funcionalidades en funcionamiento

ARCHIVO A ENTREGAR:
- PROYECTOFINALmodulo3.py (código completo)
- Documentación breve de las decisiones tomadas

TIEMPO DE PRESENTACIÓN:
- 5 minutos explicando la lógica implementada
- 5 minutos demostrando funcionalidades
- 5 minutos respondiendo preguntas del docente
"""

# -----------------------------------------------------------------------------
# 14. RECOMENDACIONES PARA EL DESARROLLO
# -----------------------------------------------------------------------------
"""
CONSEJOS PARA UN DESARROLLO EXITOSO:

1. PLANIFICACIÓN:
   - Lee todo el enunciado antes de empezar
   - Diseña la estructura de funciones primero
   - Identifica las validaciones necesarias

2. DESARROLLO POR PARTES:
   - Implementa función por función
   - Prueba cada función individualmente
   - Integra gradualmente al menú principal

3. TESTING:
   - Prueba casos normales y casos edge
   - Verifica validaciones con datos inválidos
   - Confirma cálculos matemáticos

4. DEPURACIÓN:
   - Usa print() temporales para debugging
   - Verifica tipos de datos
   - Revisa lógica condicional

5. MEJORAS FINALES:
   - Limpia código no utilizado
   - Mejora mensajes al usuario
   - Agrega comentarios finales
"""

# =============================================================================
# ¡ÉXITO EN TU PROYECTO FINAL!
# =============================================================================
"""
Recuerda: este proyecto es tu oportunidad de demostrar todo lo aprendido.
Tómate tu tiempo, planifica bien, y disfruta el proceso de creación.

Si tienes dudas durante el desarrollo, no dudes en consultar con tu docente.

¡Mucho éxito! 🚀
""" """