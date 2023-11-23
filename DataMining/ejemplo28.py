from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage

X, _ = make_blobs(n_samples=30, centers=3, random_state=42)

linked = linkage(X, method='single')
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)

plt.title("Denograma de Agrupamiento Jerarquico")
plt.xlabel("Indice del Punto de Datos")
plt.ylabel("Distancia")
plt.show()