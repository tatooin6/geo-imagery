from datetime import date
from fastapi import FastAPI, HTTPException, Query
import ee
from google.oauth2 import service_account

app = FastAPI()

# Define el alcance requerido
scopes = ['https://www.googleapis.com/auth/earthengine.readonly']

# Cargar credenciales desde un archivo de cuenta de servicio con el alcance adecuado
credentials = service_account.Credentials.from_service_account_file(
    './credentials.json', scopes=scopes
)

# Inicializar Google Earth Engine con las credenciales y el proyecto
ee.Initialize(credentials)

@app.get("/get_image/")
async def get_image(
    start_date: date = Query(..., description="Fecha de inicio en formato YYYY-MM-DD"),
    end_date: date = Query(..., description="Fecha de fin en formato YYYY-MM-DD")
):
    try:
        # Convertir fechas a strings para Google Earth Engine
        start_date_str = start_date.isoformat()
        end_date_str = end_date.isoformat()

        # Obtener una colección de imágenes de GEE
        collection = ee.ImageCollection("COPERNICUS/S2").filterDate(start_date_str, end_date_str)
        image = collection.first()  # Seleccionar la primera imagen como ejemplo

        # Exportar la imagen en un formato visualizable
        url = image.getThumbURL({'min': 0, 'max': 3000, 'dimensions': 512})
        return {"image_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
