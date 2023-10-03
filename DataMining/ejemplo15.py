import tensorflow as tf
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

iris = datasets.load_iris()
x = iris.data
y = iris.target

encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y.reshape(-1,1))

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)
scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(y_test)

#Construir el modelo ANN
model = tf.keras.models.Sequential([tf.keras.layers.Dense(units=8, activation='relu', input_shape=(4,)), tf.keras.layers.Dense(units=3, activation='softmax')])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=50)
print(f'Loss: {loss}')
print(f'Accuracy: {accuracy}')
