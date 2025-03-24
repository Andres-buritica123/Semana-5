import openpyxl

# Diccionario para almacenar productos
productos = {}

# Pedir datos de productos
for i in range(3):
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input(f"Introduce el precio de {nombre}: "))
    categoria = input(f"Introduce la categoría de {nombre}: ")
    productos[nombre] = (precio, categoria)

# Crear un nuevo libro de Excel
libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Inventario"

# Encabezados
hoja['A1'] = 'Producto'
hoja['B1'] = 'Precio'
hoja['C1'] = 'Categoría'

fila = 2

# Agregar datos al Excel
for nombre, (precio, categoria) in productos.items():
    hoja[f'A{fila}'] = nombre
    hoja[f'B{fila}'] = precio
    hoja[f'C{fila}'] = categoria
    fila += 1

# Guardar el archivo
libro.save("inventario_productos.xlsx")

print("¡Inventario guardado en inventario_productos.xlsx!")