from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Nombre(BaseModel):
    nombre:str

nombres = ['Juan', 'María', 'Pedro']

@app.get("/nombres")
async def obtener_nombres():
    return nombres

@app.post("/nombres")
async def agregar_nombre(nombre: Nombre):
    nombres.append(nombre.nombre)
    return {"mensaje" : "Nombre agregado de manera correcta"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)