import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt

# Crear listas con valores posibles para cada columna
nombres = ['Domingo', 'Eloisa', 'Carlos', 'Maria', 'Eusebio', 'India', 'Claudio', 'Odalys', 'Regina', 'Isabel']
materias = ['Geografia', 'Historia', 'Fisica', 'Mecanografia', 'Matematicas', 'Confiteria']
semestres = ['Primer', 'Segundo', 'Tercer','Cuarto','Quinto', 'Sexto', 'Septimo', 'Octavo']
#calificaciones = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9', '10']

# Inicializar listas vacías para almacenar los datos generados
lista_nombre = []
lista_materia = []
lista_semestre = []
lista_calificaciones = []

# Generar 500 filas de datos
for _ in range(500):
    nombre = random.choice(nombres)
    materia = random.choice(materias)
    semestre = random.choice(semestres)
    calificacion = random.randint(0, 10)

    
    # Añadir los datos generados a las listas
    lista_nombre.append(nombre)
    lista_materia.append(materia)
    lista_semestre.append(semestre)
    lista_calificaciones.append(calificacion)

# Crear un DataFrame de pandas con los datos
df = pd.DataFrame({
    'Nombre': lista_nombre,
    'Materia': lista_materia,
    'Semestre': lista_semestre,
    'Calificacion': lista_calificaciones
})

# Ver las primeras filas del DataFrame para asegurarnos de que se ha creado correctamente
print(df.head())

# Opcional: guardar el DataFrame en un archivo CSV
# df.to_csv('datos_ventas.csv', index=False)

#Crear cubo de datos con grourp.by
cubo = df.groupby(['Materia', 'Semestre'])['Calificacion'].mean().reset_index()
print("Cubo: ")
print(cubo)

#Visualizacion
sns.barplot(x='Materia', y='Calificacion', hue='Semestre', data=cubo)
plt.show()