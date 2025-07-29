import os
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.applications import (
    EfficientNetB0, EfficientNetB1, EfficientNetB2,
    EfficientNetV2B0, EfficientNetV2B1, EfficientNetV2B2
)
from io import StringIO

# Carpeta de salida
output_dir = "C:/workspace/deep_learning/art-tuning/generator-from-cnn/model_summaries"
os.makedirs(output_dir, exist_ok=True)

# Lista de modelos con su preprocesamiento
MODELS = [
    ("efficientnetb0", EfficientNetB0),
    ("efficientnetb1", EfficientNetB1),
    ("efficientnetb2", EfficientNetB2),
    ("efficientnetv2b0", EfficientNetV2B0),
    ("efficientnetv2b1", EfficientNetV2B1),
    ("efficientnetv2b2", EfficientNetV2B2),
]

# Procesar con cada modelo
for model_name, model_fn in MODELS:
    print(f"🧠 Generando summary para {model_name}...")

    model = model_fn(include_top=False, weights="imagenet", pooling='avg')

    # Capturar el summary como texto
    stream = StringIO()
    model.summary(print_fn=lambda x: stream.write(x + "\n"))
    summary_str = stream.getvalue()

    # 1. Guardar como archivo de texto
    txt_path = os.path.join(output_dir, f"{model_name}_summary.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(summary_str)
    print(f"📝 Guardado en: {txt_path}")