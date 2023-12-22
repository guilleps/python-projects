import pandas as pd
from fancyimpute import IterativeImputer
from sklearn.linear_model import LinearRegression

# Crear el dataset con valores faltantes
df = pd.read_csv("C:/workspace/Python/TAREA10/data/Salary.csv")

# MICE utilizando fancyimpute
imputer = IterativeImputer(max_iter=10, initial_strategy='mean',  estimator=LinearRegression())

# imputer = IterativeImputer(max_iter=10, random_state=0, estimator=LinearRegression())

df_mice = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("Imputación con MICE:")
print(df_mice)


# columna_re = ["x","x"]
# df.loc[df["x"] == 0.0 , "x"] = None