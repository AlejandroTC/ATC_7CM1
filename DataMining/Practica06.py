# Importa las bibliotecas necesarias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

# Exploración de Datos Iniciales:
# • Descarga el conjunto de datos de Kaggle y cárgalo en tu entorno de trabajo.
data = pd.read_csv("DataMining/housing.csv")
# • Explora la estructura del conjunto de datos y verifica la calidad de los datos.
print(f"\n Data Head")
print(data.head())  
print(f"\n Data Info")
print(data.info())  
print(f"\n Data Describe")
print(data.describe())  

#Preprocesar, dado que total_bedrooms tiene valores faltantes, hay que omitirlos
data = data.dropna(subset=['total_bedrooms'])
print(f"\n Data Info sin filas con valores faltantes")
print(data.info())  
print(f"\n Data Describe sin filas con valores faltantes")
print(data.describe())  
# Normaliza las variables numéricas
scaler = MinMaxScaler()
data[['median_income', 'total_rooms', 'longitude', 'latitude', 'housing_median_age', 'total_bedrooms', 'population', 'households']] = scaler.fit_transform(data[['median_income', 'total_rooms', 'longitude', 'latitude', 'housing_median_age', 'total_bedrooms', 'population', 'households']])

# Análisis de Correlación:
# Calcula y visualiza la matriz de correlación entre las variables predictoras (por ejemplo, ingreso medio, número de habitaciones) y el precio de las viviendas.
predictor_variables = ['median_income', 'total_rooms', 'longitude', 'latitude', 'housing_median_age', 'total_bedrooms', 'population', 'households']
target_variable = 'median_house_value'
correlation_matrix = data[predictor_variables + [target_variable]].corr()
plt.figure(figsize=(10, 6))
sns.barplot(x=correlation_matrix.index, y=correlation_matrix['median_house_value'], palette="viridis")
plt.title('Correlación con Precio de Viviendas')
plt.xlabel('Variables Predictoras')
plt.ylabel('Correlación')
plt.xticks(rotation=45)
plt.show()
print("\nMatriz de correlación:\n", correlation_matrix)
# • Identifica las características que están fuertemente correlacionadas con el precio de las viviendas.
strong_correlations = correlation_matrix['median_house_value'][abs(correlation_matrix['median_house_value']) > 0.1].index
# Se accede a la matriz de correlacion en el precio medio de la casa, se usa el absoluto en los valores de correlacion para saber si son mayores a 0.5 y obtener
# el indice, lo que significa que guardamos de las caracteristicas que estan mas fuertemente reslacionadas
print(f"\nCorrelaciones más fuertes (>0.1):\n",strong_correlations)

# Predicción del Precio de Viviendas:
# Divida el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba.
X = data[strong_correlations].drop('median_house_value', axis=1)
y = data['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Utiliza el modelo de regresión lineal y entrénalo utilizando las características seleccionadas.
model = LinearRegression()
model.fit(X_train, y_train)

# Evalúa el rendimiento del modelo en el conjunto de prueba utilizando métricas como el error cuadrático medio (MSE) y el coeficiente de determinación (R²).
print("\nRendimiento Linear Regresion:")
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE: {mse}')
print(f'R^2: {r2}')

# Reducción de Dimensionalidad con Análisis de Componentes Principales (ACP):
print(f"\nPCA 3 Componentes")
# Realiza un Análisis de Componentes Principales (ACP) para reducir la dimensionalidad del conjunto de datos.
n_componentes = 3
pca = PCA(n_components=n_componentes)  
X_pca = pca.fit_transform(X)
# • Visualiza y discute cómo se han reducido las dimensiones y cuánta varianza se conserva.
# Explorar la varianza explicada por cada componente
explained_variance_ratio = pca.explained_variance_ratio_
print(f"\nVarianza: \n{explained_variance_ratio}")

# Predicción con Datos Reducidos:
# • Entrena un nuevo modelo de regresión utilizando las características reducidas obtenidas del ACP.
X_train_pca, X_test_pca, _, _ = train_test_split(X_pca, y, test_size=0.2, random_state=42)
model_pca = LinearRegression()
model_pca.fit(X_train_pca, y_train)

# • Evalúa el rendimiento del modelo reducido en el conjunto de prueba.
print("\nRendimiento Linear Regresion con PCA (3 componentes):")
y_pred_pca = model_pca.predict(X_test_pca)
mse_pca = mean_squared_error(y_test, y_pred_pca)
r2_pca = r2_score(y_test, y_pred_pca)
print(f'MSE (PCA): {mse_pca}')
print(f'R^2 (PCA): {r2_pca}')


# Comparación de Modelos:
# • Compara el rendimiento del modelo original con el modelo reducido en términos de métricas de evaluación.
print(f"\nComparación de rendimiento")
print("\nRendimiento Linear Regresion")
print(f'MSE: {mse}')
print(f'R^2: {r2}')
print("\nRendimiento Linear Regresion con PCA (3 componentes):")
print(f'MSE (PCA): {mse_pca}')
print(f'R^2 (PCA): {r2_pca}')
