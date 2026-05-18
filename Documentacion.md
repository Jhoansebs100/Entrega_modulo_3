**Sistema de Gestión Tienda de Videojuegos — Documentación**

El programa es un sistema de inventario de consola que permite administrar productos de una tienda de videojuegos. Desde un menú interactivo de 8 opciones el usuario puede agregar juegos, consultar el stock, actualizar precios, registrar ventas, ver estadísticas y eliminar productos.

**Estructura de datos**

La información se almacena en un diccionario anidado. La clave exterior es el código único de cada juego, y su valor es otro diccionario con cuatro campos: nombre, plataforma, precio y cantidad. Esta estructura permite acceder, modificar o eliminar cualquier registro en tiempo constante gracias al sistema de hash interno de Python.

**Persistencia**

Al iniciar, el inventario predefinido se guarda en un archivo JSON. Una función de carga lo recupera al arrancar el programa y maneja los errores posibles: si el archivo no existe o está dañado, simplemente inicia con un inventario vacío. La limitación actual es que los cambios hechos en ejecución no se escriben de vuelta al archivo.

**Funciones principales**

El menú usa la estructura match/case de Python 3.10 para despachar cada opción. Cada función recibe el diccionario completo y opera directamente sobre él. Las funciones de escritura validan todos los datos antes de modificar el inventario, usando bucles que repiten la solicitud hasta recibir un valor correcto. Las funciones de lectura iteran sobre los valores del diccionario para calcular totales, promedios y máximos.

**Regla de negocio**

Al registrar una venta, si el total supera los $500.000, el sistema aplica automáticamente un descuento del 10% sobre el monto bruto antes de descontar el stock y generar la factura.

**Mejora principal sugerida**

Persistir los cambios al archivo JSON después de cada operación de escritura, para que el inventario no se pierda entre ejecuciones.