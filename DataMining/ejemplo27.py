from matplotlib import axes, figure, pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans

X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11], [8, 2], [10, 3], [9, 3]])
linkage_methods = ['single', 'complete', 'average', 'centroid', 'ward']

figure, axes = plt.subplots(1, len(linkage_methods) + 1, figsize=(20, 4))
for i, method in enumerate(linkage_methods):
    linked = linkage(X, method=method)
    dendrogram(linked, ax=axes[i])
    axes[i].set_title(f"Agrupamiento Jerarquico ({method})")
    axes[i].set_xlabel("Indice de Muestra")
    axes[i].set_ylabel("Distancia")

kmeans = KMeans(n_clusters=6, random_state=0).fit(X)
axes[-1].scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="rainbow")  # Corrección aquí
axes[-1].set_title("K-Means Clustering")
axes[-1].set_xlabel("X")
axes[-1].set_ylabel("Y")

plt.tight_layout()
plt.show()
