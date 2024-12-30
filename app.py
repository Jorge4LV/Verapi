
from fastapi import FastAPI
import os
import random

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello my friend"}

@app.get("/random")
def random_gif():
    # Obtén el token y la URL base del blob desde las variables de entorno
    blob_url = os.getenv("BLOB_STORAGE_URL")  # Base del blob storage
    token = os.getenv("BLOB_READ_WRITE_TOKEN")  # Token seguro para el acceso

    if not blob_url:
        return {"error": "Blob storage URL not configured"}, 500

    if not token:
        return {"error": "Blob storage token not configured"}, 500

  # Configuración: carpeta y número total de GIFs
    folder = "Spanks"
    total_gifs = 47  # Número total de GIFs

    # Selecciona un número aleatorio para el GIF (0 a total_gifs - 1)
    gif_number = random.randint(0, total_gifs - 1)
    gif_name = f"spank_{gif_number:03}.gif"  # Formato: spank_000.gif, spank_001.gif, ...

    # Construye la URL del archivo
    gif_url = f"{blob_url}/{folder}/{gif_name}"

    return {"random_gif_url": gif_url}
