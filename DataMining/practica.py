import pandas as pd
#Cargar los datos desde un archivo csv
df = pd.read_csv("data_ejemplo06.csv")

#Ver los primeors datos del DigitalFrame
print("Datos originales")
print(df)
print()

#. Drill-Down: Comienza con las ventas totales por año-mes y realiza un "drill-down" para desglosar las ventas por `Fecha`, `Categoría`, y `Producto`.
# 2. Roll-Up: Resumen las ventas por `Municipio` y luego realiza un "roll-up" para obtener las ventas totales.
# 3. Slice and Dice: Haz un "slice" para obtener las ventas de la municipio `Zacatecas` en el mes de `2021-01`, y luego un "dice" para filtrar solo las ventas de `Frutas`.
# 4. Pivot (o Rotate): Genera una tabla pivote que muestre las ventas por`Vendedor` y `Fecha`, donde cada vendedor sea una fila y cada fecha una columna.
# 5. Drill-Through: A partir del total de ventas de la categoría `Frutas` en `2021-01`, realiza un "drill-through" para ver los registros de ventas individuales que componen esa cifra.
# 6. Drill-Across: Cruza este conjunto de datos con un nuevo conjunto de datos que tenga información de `Inventario` para cada `Producto` y `Fecha`. Analiza si las ventas tienen algún impacto en el inventario.
# 7. Consolidación: Calcula la suma, el promedio, y el máximo de `Ventas` y `UnidadesVendidas` por `Vendedor`.
