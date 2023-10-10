import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv('Pokemon.csv')


#Entendimiennto de los datos
contadores_tipo = df['Type 1'].value_counts()
print(contadores_tipo)
descripcion_estadistica = df.describe()
print(descripcion_estadistica)
# Preaprocesamineto
# Llenar valores faltantes y eliminar registros con edades errorneas
df = df.drop('Type 2', axis=1)
print(df.head(2))

# Transformacion 
# Crear un objeto OneHotEncoder
cat_features = ['Type 1']
#Crear transformadores para variables categóricas
transformers = [
    ('cat', OneHotEncoder(drop='first'), cat_features)
]
preprocessor = ColumnTransformer(transformers)

# Definir las características (X) y la variable objetivo (y)
X = df
y = df['Type 1']

# Crear un pipeline que incluya el preprocesamiento y el clasificador de árbol de decisiones
pipeline = Pipeline([
    ('preprocessor', preprocessor),  # Aquí se aplica el preprocesamiento
    ('classifier', DecisionTreeClassifier(random_state=42))
])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar el modelo (incluye el preprocesamiento)
pipeline.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba (incluye el preprocesamiento)
y_pred = pipeline.predict(X_test)

# Calcular la precisión y la matriz de confusión
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Imprimir los resultados
print(f'Accuracy: {accuracy * 100:.2f}%')
print(f'Confusion Matrix:\n{conf_matrix}')


while True:
    try:
        hp = float(input('Ingrese el valor de HP: '))
        attack = float(input('Ingrese el valor de Attack: '))
        defense = float(input('Ingrese el valor de Defense: '))
        sp_atk = float(input('Ingrese el valor de Sp. Atk: '))
        sp_def = float(input('Ingrese el valor de Sp. Def: '))
        speed = float(input('Ingrese el valor de Speed: '))
        
        # Crear una lista con las estadísticas ingresadas por el usuario
        nueva_observacion = [hp, attack, defense, sp_atk, sp_def, speed]

        # Convertir la lista en un DataFrame con las mismas columnas que el conjunto de datos original
        user_data = pd.DataFrame([nueva_observacion], columns=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])

        # Utilizar el modelo para predecir el tipo de Pokémon
        predicted_type = pipeline.predict(user_data)

        # Imprimir el resultado de la predicción
        print(f'El tipo de Pokémon predicho es: {predicted_type[0]}')

        continuar = input('¿Desea ingresar otra observación? (S/N): ')
        if continuar.lower() != 's':
            break
    except ValueError:
        print('Entrada inválida. Por favor, ingrese números válidos para las estadísticas de Pokémon.')
