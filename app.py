from fastapi import FastAPI
import os
import datetime

app = FastAPI()

@app.get("/example/{parameter}")
def example(parameter: str):
    return {
        "parameter": parameter,
        "datetime": datetime.datetime.now().time()
    }

@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }

@app.get("/random-gif")
def random_gif():
    # Obtén el token del blob desde las variables de entorno
    blob_url = os.getenv("BLOB_STORAGE_URL")  # Base del blob storage
    token = os.getenv("BLOB_READ_WRITE_TOKEN")  # Token seguro para el acceso

    if not blob_url or not token:
        return {"error": "Blob storage URL or token not configured"}, 500

    # Configuración: carpeta y rango de archivos
    folder = "Spanks"
    max_gifs = 1000  # Ajusta según el número máximo estimado de GIFs

    # Selecciona un número aleatorio para el GIF
    gif_number = random.randint(0, max_gifs - 1)
    gif_name = f"spank_{gif_number:03}.gif"  # Formato: spank_000.gif, spank_001.gif, ...

    # Construye la URL del archivo
    gif_url = f"{blob_url}/{folder}/{gif_name}"

    return {"random_gif_url": gif_url}
