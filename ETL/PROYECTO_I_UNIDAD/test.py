import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lee el archivo CSV y crear DataFrame
df = pd.read_csv('C:/workspace/Python/PROYECTO/datos/AB_NYC_2019.csv', sep=',')


missingValues = df.isna()
num_missing = missingValues.values.sum()

plt.title(f'Número total de datos perdidos: {num_missing}', fontsize=14, pad=20)
sns.heatmap(df.isna(), cbar=False, cmap='magma')
plt.show()