from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import ee
from google.oauth2 import service_account
from datetime import date

app = FastAPI()

# CORS configuration
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

# Required scope
# scopes = ['https://www.googleapis.com/auth/earthengine.readonly']
scopes = ['https://www.googleapis.com/auth/earthengine']

# Service account file credentials with appropriate scope
credentials = service_account.Credentials.from_service_account_file(
    './new-credentials.json', scopes=scopes
)

ee.Initialize(credentials)

@app.get("/get_map/")
async def get_map(
    start_date: date = Query(..., description="Fecha de inicio en formato YYYY-MM-DD"),
    end_date: date = Query(..., description="Fecha de fin en formato YYYY-MM-DD")
):
    try:
        # String formatting
        start_date_str = start_date.isoformat()
        end_date_str = end_date.isoformat()

        # Bolivia geometry definition
        bolivia_geometry = ee.Geometry.Polygon(
            [[[-69.5897, -10.9895], [-57.498, -10.9895],
              [-57.498, -22.896], [-69.5897, -22.896],
              [-69.5897, -10.9895]]]
        )

        # Filter the Sentinel-2 collection by date and by region of Bolivia
        collection = (
            ee.ImageCollection("COPERNICUS/S2_HARMONIZED")
            .filterDate(start_date_str, end_date_str)
            .filterBounds(bolivia_geometry)
        )
        
        # Image band selection
        image = collection.first().select(['B4', 'B3', 'B2'])

        # Get the tile URL for Leaflet
        map_id_dict = image.getMapId({
            'min': 0,
            'max': 3000,
            'bands': ['B4', 'B3', 'B2'],
            'region': bolivia_geometry
        })
        
        print("map_id_dict:", map_id_dict)
        
        # Create the tile URL with `mapid` and `token`
        # tile_url = f"https://earthengine.googleapis.com/map/{map_id_dict['mapid']}/{{z}}/{{x}}/{{y}}?token={map_id_dict['token']}"
        tile_url = f"https://earthengine.googleapis.com/map/{map_id_dict['mapid']}/8/123/4567?token={map_id_dict['token']}"
        
        return {"tile_url": tile_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_image/")
async def get_image(
    start_date: date = Query(..., description="Init Date on format YYYY-MM-DD"),
    end_date: date = Query(..., description="End Date on format YYYY-MM-DD")
):
    try:
        start_date_str = start_date.isoformat()
        end_date_str = end_date.isoformat()

        collection = ee.ImageCollection("COPERNICUS/S2_HARMONIZED").filterDate(start_date_str, end_date_str)
        image = collection.first().select(['B4', 'B3', 'B2'])  # Select first image as example only

        # Uncomment for providing Bolivia Geometry
        # bolivia_geometry = ee.Geometry.Polygon(
        #     [[[-69.5897, -10.9895], [-57.498, -10.9895],
        #       [-57.498, -22.896], [-69.5897, -22.896],
        #       [-69.5897, -10.9895]]]
        # )

        # collection = (
        #     ee.ImageCollection("COPERNICUS/S2_HARMONIZED")
        #     .filterDate(start_date_str, end_date_str)
        #     .filterBounds(bolivia_geometry)
        # )
        
        # image = collection.first().select(['B4', 'B3', 'B2'])

        # url = image.getThumbURL({
        #     'min': 0, 
        #     'max': 3000, 
        #     'dimensions': 512,
        #     'region': bolivia_geometry
        # })
        
        url = image.getThumbURL({'min': 0, 'max': 3000, 'dimensions': 512})
        return {"image_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
