import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
df = pd.read_csv('/Users/atc/Documentos/Repos/ATC_7CM1/DataMining/sloth_data.csv')

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
#Mineria de datos
plt.scatter(df['size_cm'], df['weight_kg'], color='black')
plt.xlabel('size_cm')
plt.ylabel('weight_kg')
plt.title('Relacion tamaño y peso')
# plt.show()

# Dividir los datos en entrenamiento y prueba
X = df.drop('specie', axis=1)
Y = df['specie']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('classsifier', LogisticRegression())
])

pipeline.fit(X_train, Y_train)
y_pred = pipeline.predict(X_test)
print(accuracy_score(Y_test, y_pred))
print(classification_report(Y_test, y_pred))