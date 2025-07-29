import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetV2B2
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image

# CONFIG
IMG_SIZE = (256, 256)  # Tamaño común, cambia según modelo si deseas
EMBEDDING_LAYER = 'avg_pool'  # nombre interno del último pooling

# Ruta de la imagen
input_base_path = "C:/workspace/data/train_sampled_100"
output_dir = "C:/workspace/deep_learning/art-tuning/similitud-embeddings/embeddings"
os.makedirs(output_dir, exist_ok=True)

print("🔄 Cargando EfficientNetV2B2...")
model = EfficientNetV2B2(include_top=False, weights="imagenet", pooling='avg')

# Utilidad para cargar y preparar la imagen
def load_image(img_path, target_size):
    try:
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return preprocess_input(img_array)
    except Exception as e:
        print(f"❌ Error cargando {img_path}: {e}")
        return None

# Obtener nombre base de imagen
print(f"📁 Procesando imágenes desde: {input_base_path}")
count = 0

# Procesar con cada modelo
for root, _, files in os.walk(input_base_path):
    for file in files:
        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_path = os.path.join(root, file)
        img_array = load_image(img_path, IMG_SIZE)
        if img_array is None:
            continue

        try:
            embedding = model.predict(img_array, verbose=0)[0]
            # Crear nombre seguro y único
            relative_path = os.path.relpath(img_path, input_base_path)
            flat_name = relative_path.replace("\\", "_").replace("/", "_").replace(" ", "_")
            output_path = os.path.join(output_dir, f"{flat_name}_v2b2.json")

            with open(output_path, "w") as f:
                json.dump(embedding.tolist(), f)

            count += 1
            if count % 100 == 0:
                print(f"✅ {count} imágenes procesadas...")
        except Exception as e:
            print(f"❌ Error al procesar {img_path}: {e}")

print(f"🎉 Proceso completado. Total de embeddings generados: {count}")
