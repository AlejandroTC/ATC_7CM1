import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1/(1 + np.exp(-x))

def tangent(x):
    return (2 / (1 + np.exp(-2 * x))) - 1

def relu(x):
    return np.maximum(0,x)

def leakyrelu(a, x):
    return np.maximum(a *x, x)

def elu(a, x):
    return np.where(x>0, x, a * (np.exp(x)-1))

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0, keepdims=True)

def graph(x,y, title, xlabel, ylabel):
    plt.figure(figsize=(8,6))
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

x = np.linspace(-10, 10, 100)
y = sigmoid(x)
graph(x, y, "Función Sigmoide", "X", "Sigmoid(x)")

x = np.linspace(-10, 10, 100)
y = tangent(x)
graph(x, y, "Función Tangente Hiperbólica", "X", "Tan(x)")

x = np.linspace(1, 10, 100)
y = relu(x)
graph(x, y, "Rectified Linear Unit", "X", "ReLU(x)")

x = np.linspace(-10, 10, 100)
y = leakyrelu(0.01, x)
graph(x, y, "Leaky Rectified Linear Unit", "X", "Leaky ReLU(x), alpha = 0.01")

x = np.linspace(-10, 10, 100)
y = elu(0.01, x)
graph(x, y, "Element Linear Unit", "X", "ELU(x), alpha = 0.01")

x = np.linspace(-10, 10, 100)
y = softmax(x)
graph(x, y, "Softmax", "X", "Softmax(x)")