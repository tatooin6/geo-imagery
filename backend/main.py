from fastapi import FastAPI, HTTPException
import ee
import google.auth

app = FastAPI()

# Autenticación de Google Earth Engine
credentials, project = google.auth.default()
ee.Initialize(credentials)

@app.get("/get_image/")
async def get_image(start_date: str, end_date: str):
    try:
        # Obtener una colección de imágenes de GEE
        collection = ee.ImageCollection("MODIS/006/MOD13A2").filterDate(start_date, end_date)
        image = collection.first()  # Seleccionar la primera imagen como ejemplo

        # Exportar la imagen en un formato visualizable
        url = image.getThumbURL({'min': 0, 'max': 3000, 'dimensions': 512})
        return {"image_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
