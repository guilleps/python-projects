import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# === CONFIGURACIÓN ===
query_embedding_path = "C:/workspace/deep_learning/art-tuning-feat-extract/vit-base/embeddings/alphonse-mucha_cycles-perfecta-1902_vit.json"
embeddings_folder = "C:/workspace/deep_learning/art-tuning-feat-extract/vit-base/embeddings"
top_k = 3

# === FUNCIONES ===
def load_embedding(path):
    with open(path, "r") as f:
        return np.array(json.load(f))

def load_all_embeddings(folder, target_dim=None):
    embeddings = {}
    for file in os.listdir(folder):
        if file.endswith(".json"):
            path = os.path.join(folder, file)
            try:
                vec = load_embedding(path)
                if target_dim is None or len(vec) == target_dim:
                    embeddings[path] = vec
            except Exception as e:
                print(f"[!] Error con {file}: {e}")
    return embeddings

# === CARGAR EMBEDDING DE CONSULTA ===
query_vector = load_embedding(query_embedding_path).reshape(1, -1)
dim = query_vector.shape[1]

# === CARGAR TODOS LOS EMBEDDINGS DEL FOLDER ===
all_embeddings = load_all_embeddings(embeddings_folder, target_dim=dim)

# === CALCULAR SIMILITUD COSENO ===
results = []
for path, vec in all_embeddings.items():
    sim = cosine_similarity(query_vector, vec.reshape(1, -1))[0][0]
    results.append((path, round(sim, 4)))

# === MOSTRAR TOP-K ===
results.sort(key=lambda x: x[1], reverse=True)

print(f"\n🔍 Top-{top_k} más similares a:\n{query_embedding_path}\n")
for i, (path, score) in enumerate(results[:top_k]):
    print(f"{i+1}. {os.path.basename(path)}  |  Similitud: {score}")
