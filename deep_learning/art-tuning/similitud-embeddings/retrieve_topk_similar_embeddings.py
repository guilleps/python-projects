import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# === CONFIG ===
query_embedding_path = "C:/workspace/deep_learning/art-tuning/similitud-embeddings/embeddings/art_nouveau_alphonse-mucha_cycles-perfecta-1902.jpg_v2b2.json"
embeddings_folder = "C:/workspace/deep_learning/art-tuning/similitud-embeddings"
top_k = 3

# === FUNCIONES ===
def load_embedding(path):
    with open(path, 'r') as f:
        return np.array(json.load(f))

def collect_all_embeddings(folder, target_dim=None):
    all_embeddings = {}
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".json"):
                path = os.path.join(root, file)
                try:
                    vec = load_embedding(path)
                    if target_dim is None or len(vec) == target_dim:
                        all_embeddings[path] = vec
                except Exception as e:
                    print(f"[!] Error cargando {path}: {e}")
    return all_embeddings

# === CARGA DE EMBEDDINGS ===
query_vector = load_embedding(query_embedding_path).reshape(1, -1)
dim = query_vector.shape[1]
all_embeddings = collect_all_embeddings(embeddings_folder, target_dim=dim)

# === CÁLCULO DE SIMILITUD ===
results = []
for path, vec in all_embeddings.items():
    sim = cosine_similarity(query_vector, vec.reshape(1, -1))[0][0]
    results.append((path, round(sim, 4)))

# === TOP-K RESULTADOS ===
results.sort(key=lambda x: x[1], reverse=True)
print(f"\n🔍 Top-{top_k} imágenes más similares a:\n{query_embedding_path}\n")

for i, (path, score) in enumerate(results[:top_k]):
    print(f"{i+1}. {os.path.basename(path)}  |  Similitud: {score}")
