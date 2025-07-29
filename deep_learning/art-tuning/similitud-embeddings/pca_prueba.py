import os
import json
import numpy as np
import plotly.express as px
from sklearn.decomposition import PCA

# === CONFIGURACIÓN ===
embedding_dir = "C:/workspace/deep_learning/art-tuning/similitud-embeddings/embeddings"
modelo = "v2b2"  # o "efficientnetv2b2", etc.
embeddings = {}

# === CARGAR EMBEDDINGS ===
for file in os.listdir(embedding_dir):
    if file.endswith(".json") and modelo in file:
        with open(os.path.join(embedding_dir, file), 'r') as f:
            embeddings[file.replace(".json", "")] = np.array(json.load(f))

vectors = np.array(list(embeddings.values()))
labels = list(embeddings.keys())

# PCA a 3 componentes
pca = PCA(n_components=3)
projected = pca.fit_transform(vectors)

# Graficar con Plotly
fig = px.scatter_3d(
    x=projected[:, 0],
    y=projected[:, 1],
    z=projected[:, 2],
    hover_name=labels, 
    color=labels,  # opcional
    title=f"PCA 3D de embeddings - {modelo}",
    labels={'x': 'PC1', 'y': 'PC2', 'z': 'PC3'}
)

fig.update_traces(marker=dict(size=5), selector=dict(mode='markers'))
fig.show()