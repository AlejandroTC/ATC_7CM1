import pandas as pd
import random
from datetime import datetime

# # Crear listas con valores posibles para cada columna
# fechas = [f"2021-{str(month).zfill(2)}" for month in range(1, 13)] * 42 
# productos = ['Manzana', 'Leche', 'Pan', 'Platano', 'Jugo de Naranja']
# categorias = ['Frutas', 'Lácteos', 'Panadería', 'Frutas', 'Bebidas']
# municipios = ['Zacatecas', 'Guadalupe', 'Fresnillo','Tlaltenango','Jerez']
# vendedores = ['Ana', 'Héctor', 'Francisco', 'Nora','Clauido']

# # Inicializar listas vacías para almacenar los datos generados
# lista_fechas = []
# lista_productos = []
# lista_categorias = []
# lista_mun = []
# lista_vendedores = []
# lista_ventas = []
# lista_unidades = []

# # Generar 500 filas de datos
# for _ in range(500):
#     fecha = random.choice(fechas)
#     producto = random.choice(productos)
#     categoria = categorias[productos.index(producto)]  
#     municipio = random.choice(municipios)
#     vendedor = random.choice(vendedores)
#     ventas = random.randint(50, 200)  # Ventas en dólares, entre 50 y 200
#     unidades = random.randint(20, 100)  # Unidades vendidas, entre 20 y 100
    
#     # Añadir los datos generados a las listas
#     lista_fechas.append(fecha)
#     lista_productos.append(producto)
#     lista_categorias.append(categoria)
#     lista_mun.append(municipio)
#     lista_vendedores.append(vendedor)
#     lista_ventas.append(ventas)
#     lista_unidades.append(unidades)

# # Crear un DataFrame de pandas con los datos
# df = pd.DataFrame({
#     'Fecha': lista_fechas,
#     'Producto': lista_productos,
#     'Categoría': lista_categorias,
#     'Municipio': lista_mun,
#     'Vendedor': lista_vendedores,
#     'Ventas': lista_ventas,
#     'UnidadesVendidas': lista_unidades
# })

# # Ver las primeras filas del DataFrame para asegurarnos de que se ha creado correctamente
# print(df.head())

# # Opcional: guardar el DataFrame en un archivo CSV
# df.to_csv('datos_ventas.csv', index=False)

#Crear el dataFrame 2
# Crear listas con valores posibles para cada columna en el inventario
fechas_inventario = [f"2021-{str(month).zfill(2)}" for month in range(1, 13)] * 42
productos_inventario = ['Manzana', 'Leche', 'Pan', 'Platano', 'Jugo de Naranja']

# Inicializar listas vacías para almacenar los datos generados para el inventario
lista_fechas_inventario = []
lista_productos_inventario = []
lista_stock = []

# Generar 500 filas de datos para el inventario
for _ in range(500):
    fecha_inventario = random.choice(fechas_inventario)
    producto_inventario = random.choice(productos_inventario)
    stock = random.randint(100, 500)  # Stock entre 100 y 500 unidades
    
    # Añadir los datos generados a las listas del inventario
    lista_fechas_inventario.append(fecha_inventario)
    lista_productos_inventario.append(producto_inventario)
    lista_stock.append(stock)

# Crear un DataFrame de pandas con los datos del inventario
df_inventario = pd.DataFrame({
    'Fecha': lista_fechas_inventario,
    'Producto': lista_productos_inventario,
    'Stock': lista_stock
})


# ##Inicia la practica
df = pd.read_csv('datos_ventas.csv')

# 1. Drill-Down
dd = df.groupby(['Fecha', 'Categoría', 'Producto'])['Ventas'].sum().reset_index()
print("1. Drill-Down Result:")
print(dd)

# 2. Roll-Up
ventas_region = df.groupby('Municipio')['Ventas'].sum().reset_index()
ventas_totales = ventas_region['Ventas'].sum()
print("\n2. Roll-Up Result:")
print(ventas_region)
print(f"Ventas Totales: {ventas_totales}")

# 3. Slice and Dice
slice_result = df[(df['Fecha'].str.startswith('2021-01')) & (df['Municipio'] == 'Zacatecas')]
dice_result = slice_result[slice_result['Categoría'] == 'Frutas']
print("\n3. Slice and Dice Result:")
print(dice_result)

# 4. Pivot (o Rotate)
pivot_result = pd.pivot_table(df, values='Ventas', index=['Vendedor'], columns=['Fecha'], aggfunc=sum, fill_value=0)
print("\n4. Pivot Result:")
print(pivot_result)

# 5. Drill-Through
total_ventas_frutas_2021_01 = df[(df['Fecha'].str.startswith('2021-01')) & (df['Categoría'] == 'Frutas')]['Ventas'].sum()
drill_through_result = df[(df['Fecha'].str.startswith('2021-01')) & (df['Categoría'] == 'Frutas')]
print("\n5. Drill-Through Result:")
print(drill_through_result)

# 6. Drill-Across (Simulación ya que no tenemos un DataFrame real de inventario)
# El df_inventario es el otro conjunto de datos.
drill_across_result = pd.merge(df, df_inventario, on=['Producto', 'Fecha'])
print("\n6. Drill-Across:")
print(drill_across_result)

# 7. Consolidación
consolidation_result = df.groupby('Vendedor').agg({'Ventas': ['sum', 'mean', 'max'], 'UnidadesVendidas': ['sum', 'mean', 'max']}).reset_index()
print("\n7. Consolidación Result:")
print(consolidation_result)