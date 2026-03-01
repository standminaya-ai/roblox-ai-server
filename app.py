from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Servidor funcionando 🔥"}

@app.post("/chat")
async def chat(data: dict):
    mensaje = data.get("mensaje", "")
    respuesta = f"Recibí: {mensaje}"
    return {"respuesta": respuesta}
