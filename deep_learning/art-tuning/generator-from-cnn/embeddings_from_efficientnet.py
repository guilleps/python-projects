import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import (
    EfficientNetB0, EfficientNetB1, EfficientNetB2,
    EfficientNetV2B0, EfficientNetV2B1, EfficientNetV2B2
)
from tensorflow.keras.applications.efficientnet import preprocess_input as preprocess_v1
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input as preprocess_v2
from tensorflow.keras.preprocessing import image

# CONFIG
IMG_SIZE = (256, 256)  # Tamaño común, cambia según modelo si deseas
EMBEDDING_LAYER = 'avg_pool'  # nombre interno del último pooling

# Ruta de la imagen
input_image_path = "C:/workspace/deep_learning/art-tuning/imgs/last_judgement.jpg"
output_dir = "C:/workspace/deep_learning/art-tuning/output_embeddings/last_judgement"
os.makedirs(output_dir, exist_ok=True)

# Lista de modelos con su preprocesamiento
MODELS = [
    ("efficientnetb0", EfficientNetB0, preprocess_v1, (224, 224)),
    ("efficientnetb1", EfficientNetB1, preprocess_v1, (240, 240)),
    ("efficientnetb2", EfficientNetB2, preprocess_v1, (260, 260)),
    ("efficientnetv2b0", EfficientNetV2B0, preprocess_v2, (224, 224)),
    ("efficientnetv2b1", EfficientNetV2B1, preprocess_v2, (240, 240)),
    ("efficientnetv2b2", EfficientNetV2B2, preprocess_v2, (260, 260)),
]

# Utilidad para cargar y preparar la imagen
def load_image(img_path, target_size):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Obtener nombre base de imagen
image_name = os.path.splitext(os.path.basename(input_image_path))[0]

# Procesar con cada modelo
for model_name, model_fn, preprocess_fn, model_size in MODELS:
    print(f"🔄 Procesando con {model_name}...")

    base_model = model_fn(include_top=False, weights="imagenet", pooling='avg')
    img_array = load_image(input_image_path, model_size)
    img_preprocessed = preprocess_fn(img_array)

    embedding = base_model.predict(img_preprocessed)[0]  # 1D vector
    print(f"📏 {model_name} → embedding shape: {embedding.shape}")

    output_path = os.path.join(output_dir, f"{image_name}_{model_name}.json")
    with open(output_path, "w") as f:
        json.dump(embedding.tolist(), f)

    print(f"✅ Embedding guardado en {output_path}")
