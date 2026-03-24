from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime
import os

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI")

print("URI:", MONGO_URI)  # 👈 DEBUG

client = MongoClient(MONGO_URI)
db = client.iot
collection = db.sensores

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

@app.post("/sensor")
def guardar_sensor(data: dict):
    try:
        data["fecha"] = datetime.utcnow()
        resultado = collection.insert_one(data)
        return {"status": "dato guardado"}
    
    except Exception as e:
        return {"error": str(e)}  # 👈 MOSTRAR ERROR REAL

