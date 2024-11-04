# GEE image viewer

## Satellite Imagery Visualization Project

Currently this is a Proof of Concept composed of three main services in a docker container: a React frontend (JS), a FastAPI backend (python), and a PostgreSQL database. It uses satellite images from Google Earth Engine and deploys them in a web application for analysis and visualization. At this moment there is only a hardcoded image provided by COPERNICUS/S2, also hardcoded dates for the request of this image.

## Project Structure

- [frontend/](./frontend/README.md): Contains the React frontend project.
- [backend/](./backend/README.md): Contains the FastAPI backend project, which connects to Google Earth Engine to retrieve images.
- `db/`: PostgreSQL database service to store user information and other data.

## Deployment with Docker

Make sure you have Docker and Docker Compose installed on your system.

### Deployment Instructions

1. Clone this repository:

```bash
git clone <REPOSITORY_URL>
cd repository-name
```

2. Deploy locally on docker
Once located on the root directory, it is advisable to build without cache, then start the container with a disengaged terminal:
```bash
docker-compose -f docker-compose.yml build --no-cache
docker-compose up -d
```
#### Alternatively it can be started with 

```bash
docker-compose up --build
```
#### To stop the container

```bash
docker-compose down
```

3. Check available services at:

Frontend (React): http://localhost:3000
Backend (FastAPI): http://localhost:8000
PostgreSQL: localhost:5432

### Environment Variables

- `GOOGLE_APPLICATION_CREDENTIALS`: Set this value for the Google credentials file in the backend.
- `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`: Database settings in the `docker-compose.yml` file.

### Project Structure
.
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── credentials.json
├── frontend/
│   ├── public/
│   └── src/
└── docker-compose.yml


## Future Changes and Challenges

In the future, this should become an entire project that projects an architeture that extends multiple services as it is possible.

The idea behind this Proof of Concept is that exists the possibility to create a platform that allows the end user to request a Google Earth engine, in order to work with it. There are other technologies that are about to be added to the project. Those are and should be:

- Send parameters from the user interface in order to change dates, sensors and any other required parameters.
- Leaflet integration.
- Map tools handling.
- Geometry object management.
- User Management.
