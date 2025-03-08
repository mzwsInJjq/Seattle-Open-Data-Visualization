# Seattle Open Data Visualization

This repository contains scripts to visualize Seattle's street network data along with neighborhood boundaries using GeoJSON files.

## Dataset Sources

- **Seattle Neighborhood Map Atlas Neighborhoods**
  - [Link to dataset](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::neighborhood-map-atlas-neighborhoods)
- **Seattle Street Network Database (SND)**
  - [Link to dataset](https://data-seattlecitygis.opendata.arcgis.com/datasets/street-network-database-snd-1)
- **Seattle GeoJSON**
  - [Link to dataset](https://polygons.openstreetmap.fr/get_geojson.py?id=237385&params=0)
- **Seattle Building Outlines 2023**
  - [Link to dataset](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::building-outlines-2023/about)
- **Seattle City Limits**
  - [Link to dataset](https://data-seattlecitygis.opendata.arcgis.com/maps/seattle-city-limits-2)
- **FCC National Broadband Map**
  - [Link to dataset](https://broadbandmap.fcc.gov/data-download)
- **2020 Census Tracts - Seattle**
  - [Link to dataset](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::2020-census-tracts-seattle/)

## Requirements

- `pandas`
- `geopandas`
- `matplotlib`

You can install the required libraries using:
```bash
pip install pandas geopandas matplotlib
```

## Usage

### Script 1: Seattle Street Network and Neighborhood Boundaries

1. Download the required GeoJSON files:
    - [Neighborhood_Map_Atlas_Neighborhoods.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::neighborhood-map-atlas-neighborhoods)
    - [Street_Network_Database_SND_5675931800012836898.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/street-network-database-snd-1)
    - [seattle.geojson](https://polygons.openstreetmap.fr/get_geojson.py?id=237385&params=0)

2. Update the file paths in the script to point to the downloaded GeoJSON files.

3. Run the script:
```bash
python seattle-snd.py
```

### Script 2: Seattle Street Network, Neighborhood Boundaries, and Building Outlines

1. Download the required GeoJSON files:
    - [Neighborhood_Map_Atlas_Neighborhoods.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::neighborhood-map-atlas-neighborhoods)
    - [Street_Network_Database_SND_5675931800012836898.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/street-network-database-snd-1)
    - [seattle.geojson](https://polygons.openstreetmap.fr/get_geojson.py?id=237385&params=0)
    - [Building_Outlines_2023_5720112647185159859.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::building-outlines-2023/about)

2. Update the file paths in the script to point to the downloaded GeoJSON files.

3. Run the script:
```bash
python seattle-snd-bo.py
```

### Script 3: Seattle FCC Broadband Data

1. Download the required GeoJSON and CSV files:
    - [Neighborhood_Map_Atlas_Neighborhoods.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::neighborhood-map-atlas-neighborhoods)
    - [Street_Network_Database_SND_5675931800012836898.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/street-network-database-snd-1)
    - [seattle.geojson](https://polygons.openstreetmap.fr/get_geojson.py?id=237385&params=0)
    - [Seattle_City_Limits_-2760504394019241448.geojson](https://data-seattlecitygis.opendata.arcgis.com/maps/seattle-city-limits-2)
    - [bdc_53_FibertothePremises_fixed_broadband_J24_04mar2025.csv](https://broadbandmap.fcc.gov/data-download)
    - [bdc_53_Cable_fixed_broadband_J24_04mar2025.csv](https://broadbandmap.fcc.gov/data-download)
    - [2020_Census_Tracts_Seattle_600198261190227915.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::2020-census-tracts-seattle/)

2. Update the file paths in the script to point to the downloaded GeoJSON and CSV files.

3. Run the script:
```bash
python seattle-fcc-broadband.py
```

## Output

- `seattle-snd.py` will generate a `seattle-snd.pdf` file with the visualization of Seattle's street network and neighborhood boundaries.
- `seattle-snd-bo.py` will generate a `seattle-snd-bo.pdf` file with the visualization of Seattle's street network, neighborhood boundaries, and building outlines.
- `seattle-fcc-broadband.py` will generate a `seattle-fcc-broadband.pdf` file with the visualization of Seattle's broadband data.
