import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

def activation_function(z):
    return z

def cost_function(y, y_pred):
    return np.sum((y - y_pred) ** 2)

def train_adaline(X, y, learning_rate=0.01, max_iterations=100):
    W = np.random.randn(X.shape[1] + 1)
    for _ in range(max_iterations):
        for i in range(len(X)):
            z = np.dot(X[i], W[1:]) + W[0]
            y_pred = activation_function(z)
            W[1:] += learning_rate * (y[i] - y_pred) * X[i]
            W[0] += learning_rate * (y[i] - y_pred)
    return W

def predict_adaline(X_new, W, threshold=0.5):
    z_new = np.dot(X_new, W[1:]) + W[0]
    y_pred_new = activation_function(z_new)
    predicted_class = 1 if y_pred_new >= threshold else 0
    return predicted_class

# Crear un conjunto de datos
X_synthetic, y_synthetic = make_classification(n_samples=2000, n_features=2, n_classes=2, n_clusters_per_class=1, n_redundant=0, random_state=42)

# Dividir el conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(X_synthetic, y_synthetic, test_size=0.2, random_state=42)

# Entrenar el modelo Adaline
W_trained = train_adaline(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
predictions = [predict_adaline(row, W_trained) for row in X_test]

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, predictions)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)

print(f'Matriz:\n', conf_matrix)
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
