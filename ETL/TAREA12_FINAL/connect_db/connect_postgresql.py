from sqlalchemy import create_engine
import pandas as pd
import psycopg2

# Leer datos desde diferentes fuentes
df_carga = pd.read_csv('TAREA12_FINAL/data/final/kapoo.csv')

# Establecer la conexión a PostgreSQL 
engine = create_engine('postgresql://postgres:129837465lg@localhost:5432/chicago_city_db')

# Escribe el DataFrame en la tabla 'data_poblacion' en PostgreSQL
df_carga.to_sql('chicago_data', engine, index=False, if_exists='replace')

# Cerrar la conexión
engine.dispose()

print('Creacion de BD exitosa...')
 
# ________________________________________________

# def get_connection():
#     try:
#         return psycopg2.connect(
#             database="chicago_city_db",
#             user="postgres",
#             password="129837465lg",
#             host="localhost",
#             port=5432,
#         )
#     except:
#         return False
 
# conn = get_connection()

# conn = get_connection()

# curr = conn.cursor() # type: ignore

# curr.execute("SELECT * FROM chicago_data")

# data = curr.fetchall()

# for row in data:
# 	# print(row)

# conn.close() # type: ignore
