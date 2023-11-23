# Importa las bibliotecas necesarias
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
import warnings
# Ingonorar las warnings para la funcion sigmoide
warnings.filterwarnings("ignore", category=RuntimeWarning)


# Carga de datos
data = pd.read_csv('DataMining/BreastCancerWisconsin.csv')
# Exploracion de datos
print("Exploración de Datos/n")
print(f"\n Data Head")
print(data.head())  
print(f"\n Data Info")
print(data.info())  
print(f"\n Data Describe")
print(data.describe())  

# Preprocesamientoo de datos
# Transformacion de Diagnosis a Binario
data['diagnosis'] = data['diagnosis'].replace('B', 0).replace('M', 1)

# Exploracion de datos
print("Exploración de Datos procesados\n")
print(f"\n Data Head")
print(data.head())  
print(f"\n Data Info")
print(data.info())  
print(f"\n Data Describe")
print(data.describe())  

# Analizar correlacion
# Matriz de correlacion
predictor_variables = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]
target_variable = 'diagnosis'
correlation_matrix = data[predictor_variables + [target_variable]].corr()
plt.figure(figsize=(10, 6))
sns.barplot(x=correlation_matrix.index, y=correlation_matrix['diagnosis'], palette="viridis")
plt.title('Correlación con Diagnostico')
plt.xlabel('Variables Predictoras')
plt.ylabel('Correlación')
plt.xticks(rotation=45)
plt.show()
print("\nMatriz de correlación:\n", correlation_matrix)
# Variables con correlacion más fuertes
strong_correlations = correlation_matrix['diagnosis'][abs(correlation_matrix['diagnosis']) > 0.7].index
print(f"\nCorrelaciones más fuertes (>0.7):\n",strong_correlations)

# Dividir el conjunto de datos
X = data[strong_correlations].drop('diagnosis', axis=1)
y = data['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Modelo
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def train_logistic_regression(X, y, learning_rate=0.01, max_iterations=10000, convergence_criterion=0.0001):
    # Inicializar pesos con valores pequeños o aleatorios
    W = np.random.randn(X.shape[1])
    iterations = 0
    converged = False

    while iterations < max_iterations and not converged:
        z = np.dot(X, W)
        y_pred = sigmoid(z)
        error = y - y_pred
        gradient = np.dot(X.T, error)
        W += learning_rate * gradient
        if np.linalg.norm(learning_rate * gradient) < convergence_criterion:
            converged = True
        iterations += 1
    return W

def predict(X_new, W):
    z_new = np.dot(X_new, W)
    y_pred_new = sigmoid(z_new)
    predicted_class = 1 if y_pred_new >= 0.5 else 0
    return predicted_class


# Entrenar el modelo
W_trained = train_logistic_regression(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
predictions = [predict(row, W_trained) for row in X_test.values]

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, predictions)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)

print(f'Matriz:\n', conf_matrix)
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')