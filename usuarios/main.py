from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Servicio de Usuarios")

# Permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos
class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str

# Datos precargados
usuarios_db = [
    {"id": 1, "nombre": "Carlos Pérez", "correo": "carlos@example.com"},
    {"id": 2, "nombre": "Ana López", "correo": "ana@example.com"},
    {"id": 3, "nombre": "Miguel Torres", "correo": "miguel@example.com"},
    {"id": 4, "nombre": "Laura Díaz", "correo": "laura@example.com"},
    {"id": 5, "nombre": "Pedro Ramírez", "correo": "pedro@example.com"},
    {"id": 6, "nombre": "Sofía Gómez", "correo": "sofia@example.com"},
    {"id": 7, "nombre": "Luis Fernández", "correo": "luis@example.com"},
    {"id": 8, "nombre": "Valeria Ruiz", "correo": "valeria@example.com"},
    {"id": 9, "nombre": "Andrés Vargas", "correo": "andres@example.com"},
    {"id": 10, "nombre": "Camila Romero", "correo": "camila@example.com"}
]

@app.get("/")
def home():
    return {"mensaje": "Bienvenido al servicio de usuarios"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios_db

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    usuarios_db.append(usuario.dict())
    return {"mensaje": "Usuario agregado", "usuario": usuario}
