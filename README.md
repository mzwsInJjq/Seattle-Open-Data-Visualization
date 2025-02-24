# Seattle Open Data Visualization

This repository contains a script to visualize Seattle's street network data along with neighborhood boundaries using GeoJSON files.

## Dataset Sources

- **Seattle Neighborhood Map Atlas Neighborhoods**
  - [Link to dataset](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::neighborhood-map-atlas-neighborhoods)
- **Seattle Street Network Database (SND)**
  - [Link to dataset](https://data-seattlecitygis.opendata.arcgis.com/datasets/street-network-database-snd-1)
- **Seattle GeoJSON**
  - [Link to dataset](https://polygons.openstreetmap.fr/get_geojson.py?id=237385&params=0)

## Requirements

- `pandas`
- `geopandas`
- `matplotlib`

You can install the required libraries using:
```bash
pip install pandas geopandas matplotlib
```

## Usage

1. Download the required GeoJSON files:
    - [Neighborhood_Map_Atlas_Neighborhoods.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::neighborhood-map-atlas-neighborhoods)
    - [Street_Network_Database_SND_5675931800012836898.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/street-network-database-snd-1)
    - [seattle.geojson](https://polygons.openstreetmap.fr/get_geojson.py?id=237385&params=0)

2. Update the file paths in the script to point to the downloaded GeoJSON files.

3. Run the script:
```bash
python seattle-snd.py
```

## Output

The script will generate a `seattle-snd.pdf` file with the visualization of Seattle's street network and neighborhood boundaries.