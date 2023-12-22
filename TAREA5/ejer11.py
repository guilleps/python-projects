import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

# Elimina los valores duplicados
df_cleaned = df.drop_duplicates()

# Ahora, 'df_cleaned' contiene el DataFrame original sin los valores duplicados

print(df_cleaned)