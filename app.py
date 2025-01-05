from fastapi import FastAPI, HTTPException, Query
import os
import random

app = FastAPI()

# Configuración global
TOTAL_GIFS = {
    "spanks": 47,
    "sape": 47,
    "rubbing": 50,  # Número total de GIFs para "rubbing"
}
DEFAULT_FOLDER = "spanks"  # Carpeta predeterminada

def get_blob_url(folder: str):
    """Obtiene la URL base del blob y valida las variables de entorno."""
    api_url = os.getenv("API")  # URL base del blob storage
    token = os.getenv("BLOB_READ_WRITE_TOKEN")  # Token seguro para el acceso

    if not api_url:
        raise HTTPException(status_code=500, detail="Blob storage URL not configured")
    if not token:
        raise HTTPException(status_code=500, detail="Blob storage token not configured")

    return f"{api_url}/{folder}?token={token}"

def generate_random_gif_url(folder: str):
    """Genera una URL aleatoria para un GIF de la carpeta especificada."""
    if folder not in TOTAL_GIFS:
        raise HTTPException(status_code=404, detail="Reaction folder not found")
    
    gif_number = random.randint(0, TOTAL_GIFS[folder] - 1)
    gif_name = f"{folder[:-1]}_{gif_number:03}.gif"
    return f"{get_blob_url(folder)}/{gif_name}"

@app.get("/")
def main():
    return {"message": "Welcome to the GIF API!"}

@app.get("/random")
def random_gif(folder: str = Query(DEFAULT_FOLDER, description="Name of the folder")):
    """
    Obtiene un GIF aleatorio de la carpeta especificada.
    Si no se especifica, usa la carpeta predeterminada ("spanks").
    """
    gif_url = generate_random_gif_url(folder.lower())
    return {"random_gif_url": gif_url}

@app.get("/{reaction}")
def get_gif(reaction: str, token: str = Query(None, description="Authentication token")):
    """
    Endpoint para obtener un GIF de una reacción específica.
    
    - reaction: Tipo de reacción (carpeta).
    - token: Token de autenticación.
    """
    # Validar el token
    expected_token = os.getenv("ACCESS_TOKEN")
    if not token or token != expected_token:
        raise HTTPException(status_code=403, detail="Invalid or missing token")

    gif_url = generate_random_gif_url(reaction.lower())
    return {"reaction": reaction, "random_gif_url": gif_url}

@app.get("/rubbing")
def rubbing_gif():
    """
    Endpoint específico para obtener GIFs de 'rubbing'.
    Este es un ejemplo de cómo se puede manejar una reacción directamente.
    """
    folder = "rubbing"
    gif_url = generate_random_gif_url(folder)
    return {"reaction": "rubbing", "random_gif_url": gif_url}
