import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    'edad': [25, 30, 35, 40, 45],
    'salario': [50000, 55000, 58000, 62000, 64000]
}

df = pd.DataFrame(data)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
print(df_scaled)