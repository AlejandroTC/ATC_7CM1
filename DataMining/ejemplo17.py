import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
np.random.seed(42)
n_samples = 1000
edades = np.random.randint(18, 70, n_samples)
salarios = np.random.randint(20000, 100000, n_samples)
tipo_producto = np.random.choice(['A', 'B', 'C'], n_samples)
interacciones = np.random.randint(1, 20, n_samples)
churn = np.where(
    (salarios < 30000) | 
    (interacciones > 15), 1, 0
)
df = pd.DataFrame({
    'edad': edades,
    'salario': salarios,
    'tipo_producto': tipo_producto,
    'interacciones': interacciones,
    'Churn': churn
})
indices_faltantes = np.random.choice(df.index, size=int(0.05 * n_samples), replace=False)
df.loc[indices_faltantes, 'salarios'] = np.nan
print(df.head())

# Preaprocesamineto
# Llenar valores faltantes y eliminar registros con edades errorneas
df['salario'].fillna(df['salario'].mean(), inplace=True)
df = df[df['edad'] < 120]
# Transformacion 
# Variables categoricas y numericas
cat_features = ['tipo_producto']
num_features = ['edad', 'salario', 'interacciones']

#Crear transformadores para variables categóricas y numéricas
transformers = [
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(drop='first'), cat_features)
]

preprocessor = ColumnTransformer(transformers)

# Mineria de datos
# Dividir los datos en entrenamiento y prueba
X = df.drop('Churn', axis=1)
Y = df['Churn']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classsifier', LogisticRegression())
])

pipeline.fit(X_train, Y_train)
y_pred = pipeline.predict(X_test)
print(accuracy_score(Y_test, y_pred))
print(classification_report(Y_test, y_pred))