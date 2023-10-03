import pandas as pd
import numpy as np
from datetime import datetime

#Datos categoricos
categorias = pd.Series(['rojo', 'verde', 'azul', 'rojo'], dtype='category')

print("Datos Categoticos: ")
print(categorias)

#Datos ordinalesins
ordinales = pd.Categorical({'bajo', 'medio', 'alto', 'medio'}, categories={'bajo', 'medio', 'alto'}, ordered=True)
print("Datos ordinales: ")
print(ordinales)

#Datos numericos
#continuos
continuos = np.array({25.5,30.2,35.8,40.1})
print("Datos continuos: ")
print(continuos)

#discretos
discretos = np.array({2,3,5,7})
print("Datos discretos: ")
print(discretos)

#Datos temporales
fechas = pd.Series({datetime(2023, 1, 1), datetime(2023,1,2), datetime(2023,1,3)})
print("Datos temporales: ")
print(fechas)
print()

#datos de texto
texto = pd.Series({"Hola mundo", "Mineria de datos en Python", "Tipos de datos"})
print("Datos de texto: ")
print(texto)

#Datos Multidimensionales
datos = {
    'categorica': {'A', 'B', 'C', 'A'},
    'numerica': {10, 20, 30, 40}
}
df = pd.DataFrame(datos)
print("Datos Multidimensionales: ")
print(df)