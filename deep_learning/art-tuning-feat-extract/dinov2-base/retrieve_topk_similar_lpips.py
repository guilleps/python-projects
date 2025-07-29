import os
import torch
import lpips
import numpy as np
from PIL import Image
from torchvision import transforms

# === CONFIG ===
query_image_path = "C:/workspace/data/train_sampled_100/art_nouveau/alphonse-mucha_cycles-perfecta-1902.jpg"
images_folder = "C:/workspace/data/train_sampled_100"
top_k = 3
lpips_net = 'squeeze'  # opciones: 'alex', 'vgg', 'squeeze'

# === LPIPS MODELO ===
loss_fn = lpips.LPIPS(net=lpips_net).cuda() if torch.cuda.is_available() else lpips.LPIPS(net=lpips_net)

# === TRANSFORMACIONES PARA LPIPS ===
transform = transforms.Compose([
    transforms.Resize((256, 256)),  # asegúrate que todas tengan mismo tamaño
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)  # normalización [-1,1]
])

# === FUNCIÓN PARA CARGAR Y TRANSFORMAR ===
def load_image_tensor(path):
    img = Image.open(path).convert("RGB")
    tensor = transform(img).unsqueeze(0)  # shape (1, 3, H, W)
    return tensor.cuda() if torch.cuda.is_available() else tensor

# === IMAGEN DE CONSULTA ===
query_tensor = load_image_tensor(query_image_path)

# === RECORRER Y COMPARAR TODAS LAS IMÁGENES ===
results = []
for root, _, files in os.walk(images_folder):
    for file in files:
        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        path = os.path.join(root, file)
        try:
            img_tensor = load_image_tensor(path)
            dist = loss_fn(query_tensor, img_tensor)
            score = dist.item()
            results.append((path, round(score, 4)))
        except Exception as e:
            print(f"[!] Error con {file}: {e}")

# === ORDENAR Y MOSTRAR TOP-K (LPIPS → menor es mejor) ===
results.sort(key=lambda x: x[1])
print(f"\n🔍 Top-{top_k} imágenes más similares perceptualmente (LPIPS) a:\n{query_image_path}\n")

for i, (path, score) in enumerate(results[:top_k]):
    print(f"{i+1}. {os.path.basename(path)}  |  LPIPS distance: {score}")
