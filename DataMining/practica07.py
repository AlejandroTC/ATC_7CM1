# Importa las bibliotecas necesarias
import re
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
# Carga de datos
data = pd.read_csv('DataMining/combined_data.csv', nrows=5000)
# Exploracion de datos
print("Exploración de Datos\n")
print(f"\n Data Head")
print(data.head())  
print(f"\n Data Info")
print(data.info())  
print(f"\n Data Describe")
print(data.describe())  

# Preprocesamiento de Datos
print("\n\nPreprocesamiento de Datos\n")
# Limpieza de datos, eliminar caracteres y transformar a minusculas
data['text'] = data['text'].apply(lambda x: re.sub('[^a-zA-Z]', ' ', x))  
data['text'] = data['text'].apply(lambda x: x.lower())
# Valores faltantes
data.dropna(inplace=True) 
# Vectorización de textos - TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(data['text'])
print(f"Data Head")
print(data.head())  


# Division de Datos
X = tfidf_vectors 
y = data['label']
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

# Construccion de Modelos
# Gaussian Naives Bayes
gnb = GaussianNB()
gnb.fit(X_train.toarray(), y_train)
# Support Vector Classification 
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
# Decision Trees
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

# Matriz de confusion y metricas de evaluacion
print("\n\nMatriz de confusión y métricas de evaluación\n")
print("Gaussian Naives Bayes\n")
predictions_nb = gnb.predict(X_test.toarray())
conf_matrix_nb = confusion_matrix(y_test, predictions_nb)
accuracy_nb = accuracy_score(y_test, predictions_nb)
precision_nb = precision_score(y_test, predictions_nb)
recall_nb = recall_score(y_test, predictions_nb)
f1_nb = f1_score(y_test, predictions_nb)
print("Matriz de Confusión Naive Bayes:")
print(conf_matrix_nb)
print(f"Exactitud (Accuracy) Naive Bayes: {accuracy_nb}")
print(f"Precisión (Precision) Naive Bayes: {precision_nb}")
print(f"Sensibilidad (Recall) Naive Bayes: {recall_nb}")
print(f"Puntuación F1 (F1 Score) Naive Bayes: {f1_nb}")

print("\nSupport Vector Classification \n")
predictions_svm = svm.predict(X_test)
conf_matrix_svm = confusion_matrix(y_test, predictions_svm)
accuracy_svm = accuracy_score(y_test, predictions_svm)
precision_svm = precision_score(y_test, predictions_svm)
recall_svm = recall_score(y_test, predictions_svm)
f1_svm = f1_score(y_test, predictions_svm)
print("Matriz de Confusión SVM:")
print(conf_matrix_svm)
print(f"Exactitud (Accuracy) SVM: {accuracy_svm}")
print(f"Precisión (Precision) SVM: {precision_svm}")
print(f"Sensibilidad (Recall) SVM: {recall_svm}")
print(f"Puntuación F1 (F1 Score) SVM: {f1_svm}")

print("\nDecision Tree \n")
predictions_tree = dtree.predict(X_test)
conf_matrix_tree = confusion_matrix(y_test, predictions_tree)
accuracy_tree = accuracy_score(y_test, predictions_tree)
precision_tree = precision_score(y_test, predictions_tree)
recall_tree = recall_score(y_test, predictions_tree)
f1_tree = f1_score(y_test, predictions_tree)
print("Matriz de Confusión Árboles de Decisión:")
print(conf_matrix_tree)
print(f"Exactitud (Accuracy) Árboles de Decisión: {accuracy_tree}")
print(f"Precisión (Precision) Árboles de Decisión: {precision_tree}")
print(f"Sensibilidad (Recall) Árboles de Decisión: {recall_tree}")
print(f"Puntuación F1 (F1 Score) Árboles de Decisión: {f1_tree}")

# Validación Cruzada
print("\n\nValidación Cruzada \n")
# Validación cruzada para Naive Bayes
scores_nb = cross_val_score(gnb, X.toarray(), y, cv=5)
print("Puntuaciones de Validación Cruzada Naive Bayes:")
print(scores_nb)

# Validación cruzada para SVM
scores_svm = cross_val_score(svm, X.toarray(), y, cv=5)
print("Puntuaciones de Validación Cruzada SVM:")
print(scores_svm)

# Validación cruzada para Árboles de decisión
scores_tree = cross_val_score(dtree, X.toarray(), y, cv=5)
print("Puntuaciones de Validación Cruzada Árboles de Decisión:")
print(scores_tree)

print("\n\nBootstrap\n")
# Número de iteraciones Bootstrap
n_iterations = 100
accuracy_scores_nb = []
accuracy_scores_svm = []
accuracy_scores_tree = []

for _ in range(n_iterations):
    indices = np.random.choice(X_train.shape[0], X_train.shape[0], replace=True)
    X_bootstrap_train = X_train[indices].toarray()
    y_bootstrap_train = y_train.iloc[indices]
    
    # Gaussian Naive Bayes
    gnb.fit(X_bootstrap_train, y_bootstrap_train)
    predictions_nb = gnb.predict(X_test.toarray())
    accuracy_nb = accuracy_score(y_test, predictions_nb)
    accuracy_scores_nb.append(accuracy_nb)

    # Support Vector Classification
    if len(np.unique(y_bootstrap_train)) > 1:
        svm.fit(X_bootstrap_train, y_bootstrap_train)
        predictions_svm = svm.predict(X_test.toarray())
        accuracy_svm = accuracy_score(y_test, predictions_svm)
        accuracy_scores_svm.append(accuracy_svm)

    # Decision Trees
    dtree.fit(X_bootstrap_train, y_bootstrap_train)
    predictions_tree = dtree.predict(X_test.toarray())
    accuracy_tree = accuracy_score(y_test, predictions_tree)
    accuracy_scores_tree.append(accuracy_tree)

print("Puntuaciones de exactitud (Accuracy) de Bootstrap Naive Bayes:")
print(accuracy_scores_nb)

print("Puntuaciones de exactitud (Accuracy) de Bootstrap SVM:")
print(accuracy_scores_svm)

print("Puntuaciones de exactitud (Accuracy) de Bootstrap Decision Trees:")
print(accuracy_scores_tree)