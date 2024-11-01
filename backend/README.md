This README explains how to work with the FastAPI backend project.

# Backend - Satellite Imagery API

This is the backend of the application, built with FastAPI and Google Earth Engine API.

## Requirements

- Python 3.9 or higher
- Google Earth Engine API

## Installation

1. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```
2. Dependencies installation
```bash
pip install -r requirements.txt
```
3. Execute local server
```bash
uvicorn main:app --reload
```

The backend will be available at http://localhost:8000.

#### API Endpoints
GET /get_image/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD - Gets an image from Google Earth Engine in the specified date range.

Used and working
http://127.0.0.1:8000/get_image/?start_date=2023-01-01&end_date=2023-12-31
