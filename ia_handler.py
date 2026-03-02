# ia_handler.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Diccionario de respuestas básicas (si quieres redundancia)
respuestas_basicas = {
    "hola": "¡Hola! 😎",
    "adios": "¡Hasta luego! 👋",
    "como estas": "Estoy activo y listo para ayudarte!"
}

# Función para buscar en internet (ejemplo simple)
def buscar_web(pregunta):
    # Esto es un ejemplo; en producción podrías usar Google Custom Search API, Bing API, o scraping
    # Aquí simulamos una búsqueda simple
    return f"No encontré información exacta sobre '{pregunta}', parece ser desconocido 🤔"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje", "").lower()

    # 1️⃣ Revisar respuestas básicas
    for clave, resp in respuestas_basicas.items():
        if clave in mensaje:
            return jsonify({"respuesta": resp})

    # 2️⃣ Si no sabe → usar buscador web
    respuesta_web = buscar_web(mensaje)

    # 3️⃣ Devolver respuesta a Roblox
    return jsonify({"respuesta": respuesta_web})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje", "").lower()
    print("Recibí mensaje de Roblox:", mensaje)  # <<<< Ver en logs de Render
