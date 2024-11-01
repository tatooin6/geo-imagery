from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import ee
from google.oauth2 import service_account
from datetime import date

app = FastAPI()

# CORS configuracion
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Alcance requerido
scopes = ['https://www.googleapis.com/auth/earthengine.readonly']

# Credenciales de archivo de cuenta de servicio con el alcance adecuado
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
