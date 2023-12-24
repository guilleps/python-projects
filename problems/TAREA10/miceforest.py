import pandas as pd
import miceforest as mf

df = pd.read_csv("C:/workspace/Python/TAREA10/data/Churn_Modelling.csv")

# Use Numeric Features
df_train = df.loc[:, ["Balance", "Age", "Exited"]]

# Create kernel.
kds = mf.ImputationKernel(
    df_train,
    save_all_iterations=True,
    random_state=100
)

# Run the MICE algorithm for 2 iterations
kds.mice(2)

# Return the completed dataset.
df_imputed = kds.complete_data()

# Muestra el DataFrame con valores imputados después de 2 iteraciones
print(df_imputed.head())

# Reinicia el kernel para una nueva imputación
kds.reset()

# Ejecuta el MICE para 5 iteraciones y 50 estimadores
kds.mice(iterations=5, n_estimators=50)

# Return the completed dataset.
df_imputed2 = kds.complete_data()

# Muestra el DataFrame con valores imputados después de 5 iteraciones
print(df_imputed2.head())
