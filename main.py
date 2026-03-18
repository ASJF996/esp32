from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

# conexión MongoDB Atlas
MONGO_URI = "mongodb+srv://esp32:esp32pass@cluster0.rixvkch.mongodb.net/iot"

#“mongodb+srv://<credentials>@cluster0.rixvkch.mongodb.net/?appName=Cluster0”

client = MongoClient(MONGO_URI)
db = client.iot
collection = db.sensores

@app.get("/")
def root():
    return {
 "temperatura": 24,
 "humedad": 60
}


@app.post("/sensor")
def guardar_sensor(data: dict):

    data["fecha"] = datetime.now()

    collection.insert_one(data)

    return {"status":"dato guardado"}

