import pandas as pd

#Cargar los datos desde un archivo csv
df = pd.read_csv("data_ejemplo06.csv")

#Ver los primeors datos del DigitalFrame
print("Datos originales")
print(df)
print()

#Agregar bentas por producto (simulando un cubo QLAP)
print("Ventas totales por producto:")
ventas_por_producto = df.groupby("Producto")["Ventas"].sum()
print(ventas_por_producto)
print()

#Agreagar ventas por region
print("Ventas totales por region")
ventas_por_region = df.groupby("Region")["Ventas"].sum()
print(ventas_por_region)
print()

#Agregar ventas por prodcuto y region
print("Ventas totales por producto y region")
ventas_por_producto_y_region = df.groupby(["Producto", "Region"])["Ventas"].sum().unstack()
print(ventas_por_producto_y_region)
print()