# Importa las bibliotecas necesarias
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression

# Carga de datos
data = pd.read_csv('DataMining/BreastCancerWisconsin.csv')

# Transformacion de Diagnosis a Binario
data['diagnosis'] = data['diagnosis'].replace('B', 0).replace('M', 1)

# Analizar correlacion
predictor_variables = ["radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean", "compactness_mean", "concavity_mean", "concave points_mean", "symmetry_mean", "fractal_dimension_mean", "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se", "compactness_se", "concavity_se", "concave points_se", "symmetry_se", "fractal_dimension_se", "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst", "compactness_worst", "concavity_worst", "concave points_worst", "symmetry_worst", "fractal_dimension_worst"]
target_variable = 'diagnosis'
correlation_matrix = data[predictor_variables + [target_variable]].corr()

# Variables con correlacion más fuertes
strong_correlations = correlation_matrix['diagnosis'][abs(correlation_matrix['diagnosis']) > 0.7].index

# Dividir el conjunto de datos
X = data[strong_correlations].drop('diagnosis', axis=1)
y = data['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar regresion logistica
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
