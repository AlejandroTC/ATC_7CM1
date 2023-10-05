import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# Cargar datos de iris
iris = load_iris()
X = iris.data
y = iris.target
# Dividir conjunto de entrenamiento, 20% y 80%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Crear y Entrenar el modelo de regresion logistica
logRec = LogisticRegression(max_iter=1000)
logRec.fit(X_train, y_train)
# Crear y entrenar el modelo de Arbol de decision
albol = DecisionTreeClassifier(random_state=42)
albol.fit(X_train, y_train)
#Calcular y mostrar las precisiones con datos de prueba
log_accuracy = accuracy_score(y_test, logRec.predict(X_test))
albol_accuracy = accuracy_score(y_test, albol.predict(X_test))
print(f'Precisión del modelo de Regresión Logística: {log_accuracy:.2f}')
print(f'Precisión del modelo de Árbol de Decisiones: {albol_accuracy:.2f}')
#Usuario
def predecir(nueva_observacion):
    clases = iris.target_names
    #Regresion Logistica
    log_pred = logRec.predict([nueva_observacion])
    tipo_reg = clases[log_pred[0]]
    print(f'Resultado Regresión Logística: {tipo_reg}')
    #Arboles de decision
    albol_pred = logRec.predict([nueva_observacion])
    tipo_albol = clases[albol_pred[0]]
    print(f'Resultado Árbol de Decisiones: {tipo_albol}')

while True:
    try:
        longitud_sepalo = float(input('Ingrese la longitud del sépalo: '))
        ancho_sepalo = float(input('Ingrese el ancho del sépalo: '))
        longitud_petalo = float(input('Ingrese la longitud del pétalo: '))
        ancho_petalo = float(input('Ingrese el ancho del pétalo: '))
        nueva_observacion = [longitud_sepalo, ancho_sepalo, longitud_petalo, ancho_petalo]
        predecir(nueva_observacion)
        continuar = input('¿Desea ingresar otra observación? (S/N): ')
        if continuar.lower() != 's':
            break
    except ValueError:
        print('Entrada inválida. Por favor, ingrese números válidos para las características de la flor.')
