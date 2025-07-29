import os
import json
import torch
import numpy as np
from PIL import Image
from transformers import AutoImageProcessor, AutoModel

# === CONFIGURACIÓN ===
input_base_path = "C:/workspace/data/train_sampled_100"
output_dir = "C:/workspace/deep_learning/art-tuning-feat-extract/embeddings"
os.makedirs(output_dir, exist_ok=True)

# === Cargar modelo DINOv2 ===
processor = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
model = AutoModel.from_pretrained("facebook/dinov2-base")

# === Procesar todas las imágenes ===
supported_exts = ('.jpg', '.jpeg', '.png')

for root, _, files in os.walk(input_base_path):
    for file in files:
        if not file.lower().endswith(supported_exts):
            continue

        try:
            image_path = os.path.join(root, file)
            img = Image.open(image_path).convert("RGB")
            inputs = processor(images=img, return_tensors="pt")

            with torch.no_grad():
                outputs = model(**inputs)
                embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()  # (768,)

            # Abreviado: nombre base sin extensión ni ruta
            image_name = os.path.splitext(file)[0]
            json_path = os.path.join(output_dir, f"{image_name}_dinov2.json")

            with open(json_path, "w") as f:
                json.dump(embedding.tolist(), f)

            print(f"✅ Procesado: {file}")

        except Exception as e:
            print(f"[!] Error procesando {file}: {e}")
