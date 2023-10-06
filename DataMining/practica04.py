import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv('DataMining/sloth_data.csv')

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

#Mineria
#Mineria de datos
plt.scatter(df['size_cm'], df['weight_kg'], color='black')
plt.xlabel('size_cm')
plt.ylabel('weight_kg')
plt.title('Relacion tamaño y peso')
plt.show()
# Examinar la relación entre las dimensiones y la clasificación de peligro.
# Relación entre el tamaño (size_cm) con la clasificación de peligro
critically_endangered = []
vulnerable = []
least_concern = []
for i in range(df.shape[0]):
    if df["endangered"].iloc[i] == "critically_endangered":
        critically_endangered.append(df["size_cm"].iloc[i])
    elif df["endangered"].iloc[i] == "vulnerable":
        vulnerable.append(df["size_cm"].iloc[i])
    elif df["endangered"].iloc[i] == "least_concern":
        least_concern.append(df["size_cm"].iloc[i])

mean_critically = np.mean(critically_endangered)
print(
    "Promedio de tamaño(cm) de los perezosos que su clasificación de peligro es critica: ",
    mean_critically,
)
mean_vulnerable = np.mean(vulnerable)
print(
    "Promedio de tamaño(cm) de los perezosos que su clasificación de peligro es vulnerable: ",
    mean_vulnerable,
)
mean_least_concern = np.mean(least_concern)
print(
    "Promedio de tamaño(cm) de los perezosos que su clasificación de peligro es de menor preocupación: ",
    mean_least_concern,
)

#Modelado
#Variables categoricas
cat_features = ['endangered', 'specie']
#Crear transformadores para variables categóricas, pasa a 1 y 0
transformers = [
    ('cat', OneHotEncoder(drop='first'), cat_features)
]
#Usar un prerocesador para guardar las variables transformadas
preprocessor = ColumnTransformer(transformers)

# Definir las características (X todo el dataframe) y la variable objetivo (y las especies, clasficiar)
X = df
y = df['specie']

# Crear un pipeline que incluya el preprocesamiento y el clasificador de árbol de decisiones
pipeline = Pipeline([
    ('preprocessor', preprocessor), 
    ('classifier', DecisionTreeClassifier(random_state=42))
])

# Dividir los datos en conjuntos de entrenamiento 80% y prueba 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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