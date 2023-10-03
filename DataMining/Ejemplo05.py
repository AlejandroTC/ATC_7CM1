#pip install pandas

import pandas as pd

#Supongamos que tenemos un conjunto de datos de ventas en un DataFrame
data = {
    'Fecha': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Producto': ['Manzana', 'Banana', 'Manzana', 'Banana'],
    'Ciudad': ['Nueva York', 'Nueva York', 'Chicago', 'Chicago'],
    'Ventas': [100, 150, 200, 50]
}

df = pd.DataFrame(data)

#Pivot para crear un cubo simple (suma de Ventas por Fecha y Producto)

cube = pd.pivot_table(df, values='Ventas', index='Fecha', columns='Producto', aggfunc='sum')

print("Cubo simple:")
print(cube)

#Se puede realizar un análisis más complejo agregando más dimensiones.
#Por ejemplo, podríamos quere saber las ventas por ciudad y producto.

cube_multi_dimension = pd.pivot_table(df, values='Ventas', index=['Fecha', 'Ciudad'], columns='Producto', aggfunc='sum')

print("\nCubo multi-dimsensión:")
print(cube_multi_dimension)

#Podríamos querer "rodar" (roll-up) el cubo para tener las ventas por Prodcut
cube_rollup = pd.pivot_table(df, values='Ventas', columns='Producto', aggfunc='sum')

print("\n Cubo rodado (roll-up):")
print(cube_rollup)