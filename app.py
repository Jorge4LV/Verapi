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

@app.get("/list-blob-files")
def list_blob_files():
    # Obtén la URL base del blob storage desde las variables de entorno
    blob_url = os.getenv("BLOB_READ_WRITE_TOKEN")

    if not blob_url:
        return {"error": "Blob storage URL not configured"}, 500

    # Listado de archivos, podría ser dinámico o estático
    files = [
        "GIF_20240912_192846_755-32SLGRY1PGOUsTrKcvw5LVXmXIq7nz.gif",
        "file2.png",
        "file3.txt"
    ]

    # Construir las URLs completas
    file_urls = [f"{blob_url}/{file}" for file in files]
    return {"files": file_urls}
    
