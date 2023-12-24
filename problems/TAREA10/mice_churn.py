# https://www.machinelearningplus.com/machine-learning/mice-imputation/
# https://www.kaggle.com/datasets/aakash50897/churn-modellingcsv

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# es necesario habilitar explícitamente la imputación iterativa, ya que aún es experimental
from fancyimpute import IterativeImputer

df = pd.read_csv("C:/workspace/Python/TAREA10/data/Churn_Modelling.csv")

df = df.drop(["RowNumber","CustomerId","Surname","CreditScore","Geography","Gender","Tenure","NumOfProducts","HasCrCard","IsActiveMember","EstimatedSalary"], axis=1)

# Reemplaza los valores "0" con NaN en todo el DataFrame
df.replace(0, np.nan, inplace=True)

# Selecciona las columnas a imputar
columns_to_impute = ["Balance", "Age", "Exited"]
df_train = df[columns_to_impute]
print(df_train)

# MICE utilizando fancyimpute
imputer = IterativeImputer(max_iter=10, initial_strategy='mean',  estimator=LinearRegression())
df_mice = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("Imputación con MICE:")
print(df_mice.head(16))