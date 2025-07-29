import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

folder_path = "C:/workspace/deep_learning/art-tuning/output_embeddings/cliffs-at-petit-dalles"
exclude_dimensions = []

def load_embeddings(folder):
    grouped = defaultdict(dict)
    for file in os.listdir(folder):
        if file.endswith('.json'):
            path = os.path.join(folder, file)
            with open(path, 'r') as f:
                vector = np.array(json.load(f))
                dim = len(vector)
                grouped[dim][file] = vector
    return grouped

def compute_cosine_matrix(embeddings_dict):
    filenames = list(embeddings_dict.keys())
    vectors = [embeddings_dict[name].reshape(1, -1) for name in filenames]
    matrix = cosine_similarity(np.vstack(vectors))
    return pd.DataFrame(matrix, index=filenames, columns=filenames)

all_groups = load_embeddings(folder_path)

# ---------- USO ----------
for dim, group in all_groups.items():
    if dim in exclude_dimensions:
        print(f"⛔ Excluido grupo de dimensión {dim}")
        continue

    print(f"\n🔍 Comparando embeddings de dimensión {dim} (n={len(group)})")
    df = compute_cosine_matrix(group)
    print(df.round(4))

    # Guardar CSV
    csv_output = os.path.join(folder_path, f"similitud_coseno_{dim}d.csv")
    df.to_csv(csv_output)
    print(f"✅ Matriz exportada en: {csv_output}")