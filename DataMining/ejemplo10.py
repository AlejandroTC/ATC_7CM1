import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

iris = datasets.loead_iris()
x = iris.data[:, np.newaxis, 0]
y = iris.data[:, np.newaxis, 1]

x_train =x[:-20]
x_test = x[-20:]
y_train = y[:-20]
y_test = y[-20:]

regr = linear_model.LinearRegression()

regr.fot(x_train, y_train)
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)

print("Coeficientes: \n", regr.coef_)
print("Mean squared error: %.2f" %r2_score(y_test, y_pred))
plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, y_pred, color='blue', linewidth=3)
plt.xlabel('sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.tittle('Linear Regression Example')
plt.show()