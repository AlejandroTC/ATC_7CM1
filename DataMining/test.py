import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_csv("Pokemon.csv")
#Ver los primeros datos del DataFrame
print("\n DataFrame Original:")
print(df)

#Se utilizo el metodo replace de la funcion pandas para poder remplazar por categorizacion la columna Type 1
#Bug : 1, Dark : 2, Dragon : 3, Electric : 4, Fairy : 5, Fighting : 6,
#Fire : 7, Flying : 8, Ghost : 9, Grass : 10, Ground : 11, Ice : 12,
#Normal : 13, Poison : 14, Psychic : 15, Rock : 16, Steel : 17,Water : 18,
dfcat = df.replace({"Bug" : 1, "Dark" : 2, "Dragon" : 3, 
                    "Electric" : 4, "Fairy" : 5, "Fighting" : 6,"Fire" : 7, 
                    "Flying" : 8, "Ghost" : 9, "Grass" : 10, "Ground" : 11, 
                    "Ice" : 12,"Normal" : 13, "Poison" : 14, "Psychic" : 15, 
                    "Rock" : 16, "Steel" : 17,"Water" : 18,})
print("\n DataFrame categorizado (Type 1 y 2):")
print(dfcat)

dfcat.drop('Type 2', axis=1)
    
#Modelado
# Features: 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'
X = dfcat[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
# Target: Type 1
y = dfcat['Type 1']

# Dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Implementar y entrenar el modelo de Árbol de Decisiones
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba (incluye el preprocesamiento)
y_pred = clf.predict(X_test)

# Calcular la precisión y la matriz de confusión
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Imprimir los resultados
print(f'Accuracy: {accuracy * 100:.2f}%')
print(f'Confusion Matrix:\n{conf_matrix}')

#Permitimos la entrada de nuevas observaciones y utilizar ambos modelos para predecir el tipo de pokemon mediante la terminal
print("Ingrese los numeros (solo seis) de la siguiente forma 'HP Attack Defense Sp. Atk Sp. Def Speed")
n = 6 # Permite solo el ingreso de 6 numeros
arr = input()   # Array para almacenar los numeros
nueva_observación = list(map(float,arr.split(' '))) # separamos por espacio los números y encontramos ['2','3','6','6','5','5']
tipo_pred_reg_log = predecir_tamaño(reg_log, nueva_observación)
tipo_pred_clf_log = predecir_tamaño(clf, nueva_observación)

    
resultado_tipo1 = type1(tipo_pred_reg_log)
resultado_tipo2 = type2(tipo_pred_clf_log)
print(f'Tipo de Pokemon predicho por Regresión Logística: {resultado_tipo1}')
print(f'Tipo de Pokemon predicho por Árbol de Decisiones: {resultado_tipo2}')