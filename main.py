from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import random

app = FastAPI(title="Servicio de Pedidos")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pedido(BaseModel):
    id: int
    usuario_id: int
    producto_id: int

pedidos_db = []

@app.get("/")
def home():
    return {"mensaje": "Bienvenido al servicio de pedidos"}

@app.get("/pedidos")
def listar_pedidos():
    # Si no hay pedidos, genera 10 aleatorios basados en usuarios y productos
    if not pedidos_db:
        try:
            usuarios = requests.get("http://localhost:5004/usuarios").json()
            productos = requests.get("http://localhost:5003/productos").json()

            for i in range(1, 11):
                usuario_id = random.choice(usuarios)["id"]
                producto_id = random.choice(productos)["id"]
                pedidos_db.append({
                    "id": i,
                    "usuario_id": usuario_id,
                    "producto_id": producto_id
                })
        except Exception:
            return {"error": "No se pudo conectar a los otros microservicios"}
    return pedidos_db
