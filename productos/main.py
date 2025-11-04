from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Servicio de Productos")

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

# Productos de ejemplo
productos_db = [
    {"id": 1, "nombre": "Laptop HP", "precio": 15500},
    {"id": 2, "nombre": "Mouse Logitech", "precio": 350},
    {"id": 3, "nombre": "Teclado Mecánico", "precio": 800},
    {"id": 4, "nombre": "Monitor Samsung 24''", "precio": 2800},
    {"id": 5, "nombre": "Audífonos Sony", "precio": 900},
    {"id": 6, "nombre": "Smartphone Xiaomi", "precio": 6200},
    {"id": 7, "nombre": "SSD 1TB", "precio": 1700},
    {"id": 8, "nombre": "Memoria RAM 16GB", "precio": 950},
    {"id": 9, "nombre": "Silla Gamer", "precio": 3500},
    {"id": 10, "nombre": "Webcam Logitech", "precio": 1200}
]

@app.get("/")
def home():
    return {"mensaje": "Bienvenido al servicio de productos"}

@app.get("/productos")
def listar_productos():
    return productos_db

@app.post("/productos")
def crear_producto(producto: Producto):
    productos_db.append(producto.dict())
    return {"mensaje": "Producto agregado", "producto": producto}
