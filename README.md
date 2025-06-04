# Chicago Crime Checker 2025

A Python + React web app for visualizing crime data around a user-specified address in the city limits of Chicago. This tool estimates nearby population, calculates a safety score, and displays recent crimes on an interactive map.

## Features

* Search any address in Chicago
* Select search radius in meters (e.g., 250m, 500m, 1000m)
* View recent crime data by type and count
* Display safety score based on estimated population and total crime count
* Interactive Leaflet map with address and crime markers

## Technologies Used

* **Frontend**: React, Axios, Leaflet
* **Backend**: Flask, GeoPandas, Pandas, Geopy
* **Data**: 2020 Census block group shapefiles and population data, 2025 City of Chicago crime dataset

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/CrimeVisualization.git
cd CrimeVisualization
```

### 2. Set up Python virtual environment

```bash
python3 -m venv venv310
source venv310/bin/activate
pip install -r requirements.txt
```

### 3. Set up frontend

```bash
cd frontend
npm install
npm start
```

### 4. Run backend

```bash
cd backend
python app.py
```

## Notes

* Population estimates use block groups whose **centroids** fall within the search radius.
* Safety score is calculated as a function of crime count relative to estimated population.

## Author

Isaac Biggs
CS + GGIS Major, University of Illinois Urbana-Champaign
Data sources: City of Chicago Data Portal, U.S. Census Bureau
