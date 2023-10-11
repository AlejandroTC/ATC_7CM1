import pandas as pd 
data = {
    'edad': [25, 30, 35, None, 40],
    'salario': [50000, 55000, None, 50000, 60000]
}
df = pd.DataFrame(data)
df['edad'].fillna(df['edad'].mean(), inplace=True)
df['salario'].fillna(df['salario'].mean(), inplace=True)
print(df)
#Se añade una columna categórica al dataframe
df['departamento'] = ['ventas', 'ingenieria', 'ventas', None, 'ingenieria']
df['departamento'].fillna(df['departamento'].mode()[0], inplace=True)
print(df)