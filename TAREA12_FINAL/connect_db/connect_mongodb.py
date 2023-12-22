import pymongo
from pymongo import MongoClient
import pandas as pd

conect_to_local = "mongodb://localhost:27017/" #conexión al localhost mongodb compass

cliente = MongoClient(conect_to_local) # se crea un objeto MongoClient

local_db = cliente.local #identifica la bd 'local' existente

collection = local_db.map_red_light # accede a la coleccion perteneciente a la db

# Obtener todos los documentos en la colección
cursor = collection.find()

dataset = list(cursor)

mongo_data = pd.DataFrame(dataset)

print(mongo_data)































"""

# _____________Obtener un documento específico por su ID:___________--
from bson import ObjectId

# Supongamos que "your_id" es el ID del documento que buscas
document_id = ObjectId("your_id")
document = collection.find_one({"_id": document_id})

# Imprimir el documento encontrado
print(document)


# ________________Realizar una consulta más específica:___________________

# Supongamos que quieres obtener documentos que cumplen con ciertos criterios
query = {"field_name": "value"}

# Realizar la consulta
cursor = collection.find(query)

# Iterar sobre los documentos encontrados e imprimir sus contenidos
for document in cursor:
    print(document)

# ______________________________________
"""