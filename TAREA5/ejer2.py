import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

# Crear el mapa de calor de valores nulos
sns.heatmap(df.isna(), cbar=False, cmap='magma')
plt.show()