# Importa las bibliotecas necesarias
import pandas as pd
import numpy as np

# Exploración de Datos Iniciales:
# • Descarga el conjunto de datos de Kaggle y cárgalo en tu entorno de trabajo.
data = pd.read_csv("DataMining/healthcare_dataset.csv")
# • Explora la estructura del conjunto de datos y verifica la calidad de los datos.
print(f"\n Data Head")
print(data.head())  
print(f"\n Data Info")
print(data.info())  
print(f"\n Data Describe")
print(data.describe())  

