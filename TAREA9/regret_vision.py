import pandas as pd
from sklearn.impute import KNNImputer

df = pd.read_csv("C:/workspace/Python/TAREA9/data/Salary.csv")

# Inicializar el imputador KNN con el número de vecinos deseado
imputer = KNNImputer(n_neighbors=3)

# Aplicar el imputador a los datos
imputed_data = imputer.fit_transform(df)

# Convertir los datos imputados de vuelta a un DataFrame de Pandas
imputed_df = pd.DataFrame(imputed_data, columns=['YearsExperience', 'Salary'])

print(imputed_df)