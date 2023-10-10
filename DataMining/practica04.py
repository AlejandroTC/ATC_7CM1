import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv('_sloth_data.csv')

# Preaprocesamineto
# Llenar valores faltantes y eliminar registros con edades errorneas
df = df[df['tail_length_cm'] > 0]
print(df.head(2))
# Transformacion 
# Primero, define las condiciones individuales
condition1 = (df['tail_length_cm'] <= 2) | (df['weight_kg'] <= 2)
condition2 = ((2 < df['tail_length_cm']) & (df['tail_length_cm'] <= 4)) | ((2 < df['weight_kg']) & (df['weight_kg'] <= 4))
condition3 = ((4 < df['tail_length_cm']) & (df['tail_length_cm'] <= 6)) | ((4 < df['weight_kg']) & (df['weight_kg'] <= 6))
condition4 = ((6 < df['tail_length_cm']) & (df['tail_length_cm'] <= 8)) | ((6 < df['weight_kg']) & (df['weight_kg'] <= 8))

# Luego, utiliza np.where para asignar los valores correspondientes a cada condición
sleep = np.where(condition1, 22,
         np.where(condition2, 20,
           np.where(condition3, 18,
             np.where(condition4, 16, 0)
           )
         )
       )

df['sleep'] = sleep
print(df.head)
# Crear un objeto OneHotEncoder

cat_features = ['endangered', 'ssssss']

#Crear transformadores para variables categóricas y numéricas
transformers = [
    ('cat', OneHotEncoder(drop='first'), cat_features)
]
preprocessor = ColumnTransformer(transformers)

# Definir las características (X) y la variable objetivo (y)
X = df.drop('ssssss', axis=1)  # Asegúrate de usar el nombre de la columna objetivo correcto
y = df['ssssss']

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