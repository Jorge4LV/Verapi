from fastapi import FastAPI, HTTPException
import os
import random

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello my friend"}

def check_token(token: str):
    # Compara el token proporcionado con el valor de la variable de entorno
    expected_token = os.getenv("TOKENDUDUA")
    if token != expected_token:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid token")

@app.get("/random")
def random_gif(token: str):
    check_token(token)  # Verifica el token antes de proceder

    # Obtén el enlace base de la variable de entorno API en Vercel
    api_url = os.getenv("API")
    if not api_url:
        raise HTTPException(status_code=500, detail="API base URL not configured")

    # Configuración: carpeta y número total de GIFs
    folder = "Spanks"
    total_gifs = 47  # Número total de GIFs

    # Selecciona un número aleatorio para el GIF (0 a total_gifs - 1)
    gif_number = random.randint(0, total_gifs - 1)
    gif_name = f"spank_{gif_number:03}.gif"  # Formato: spank_000.gif, spank_001.gif, ...

    # Construye la URL usando la variable API
    gif_url = f"{api_url}/{folder}/{gif_name}"

    return {"random_gif_url": gif_url}

@app.get("/spank")
def spank_gif(token: str):
    check_token(token)  # Verifica el token antes de proceder

    # Obtén el enlace base de la variable de entorno API en Vercel
    api_url = os.getenv("API")
    if not api_url:
        raise HTTPException(status_code=500, detail="API base URL not configured")

    # Configuración: carpeta y número total de GIFs
    folder = "spanks"
    total_gifs = 47  # Número total de GIFs

    # Selecciona un número aleatorio para el GIF (0 a total_gifs - 1)
    gif_number = random.randint(0, total_gifs - 1)
    gif_name = f"spank_{gif_number:03}.gif"  # Formato: spank_000.gif, spank_001.gif, ...

    # Construye la URL usando la variable API
    gif_url = f"{api_url}/{folder}/{gif_name}"

    return {"random_gif_url": gif_url}

@app.get("/sape")
def sape_gif(token: str):
    check_token(token)  # Verifica el token antes de proceder

    # Obtén el enlace base de la variable de entorno API en Vercel
    api_url = os.getenv("API")
    if not api_url:
        raise HTTPException(status_code=500, detail="API base URL not configured")

    # Configuración: carpeta y número total de GIFs
    folder = "sape"
    total_gifs = 47  # Número total de GIFs

    # Selecciona un número aleatorio para el GIF (0 a total_gifs - 1)
    gif_number = random.randint(0, total_gifs - 1)
    gif_name = f"Sape_{gif_number:03}.gif"  # Formato: spank_000.gif, spank_001.gif, ...

    # Construye la URL usando la variable API
    gif_url = f"{api_url}/{folder}/{gif_name}"

    return {"random_gif_url": gif_url}