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
    - [2020_Census_Tracts_Seattle_600198261190227915.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::2020-census-tracts-seattle)
    - [2020_Census_Block_Groups_-_Seattle.geojson](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::2020-census-block-groups-seattle-1)

2. Update the file paths in the script to point to the downloaded GeoJSON and CSV files.

3. Run the script:
```bash
python seattle-fcc-broadband.py
```

## Output

- `seattle-snd.py` will generate a `seattle-snd.pdf` file with the visualization of Seattle's street network and neighborhood boundaries.
- `seattle-snd-bo.py` will generate a `seattle-snd-bo.pdf` file with the visualization of Seattle's street network, neighborhood boundaries, and building outlines.
- `seattle-fcc-broadband.py` will generate a `seattle-fcc-broadband.pdf` file with the visualization of Seattle's broadband data. (Census Tracts-Level)
- `seattle-fcc-broadband-bg.py` will generate a `seattle-fcc-broadband-bg.pdf` file with the visualization of Seattle's broadband data. (Census Block Groups-Level)
### Output of `seattle-fcc-broadband.py`
```
data.columns: Index(['frn', 'provider_id', 'brand_name', 'location_id', 'technology',
       'max_advertised_download_speed', 'max_advertised_upload_speed',
       'low_latency', 'business_residential_code', 'state_usps', 'block_geoid',
       'h3_res8_id'],
      dtype='object')
census_tracts.columns: Index(['OBJECTID', 'GEOID20', 'GROSS_ACRES', 'LAND_ACRES', 'WATER_ACRES',
       'NAME', 'TRACT_NUMB', 'BASENAME', 'UVDA_AREA', 'CRA_NO', 'CRA_GRP',
       'GEN_ALIAS', 'DETL_NAMES', 'C_DISTRICT', 'geometry'],
      dtype='object')
         GEOID20  max_download_speed_in_tract
0    53033000402                         2000
1    53033000403                         2000
2    53033000700                         8000
3    53033003302                         8000
4    53033003601                         2000
..           ...                          ...
172  53033008101                        10000
173  53033010401                         2000
174  53033011401                         2000
175  53033011700                         2000
176  53033011901                         2000

[177 rows x 2 columns]
[  2000   8000   1200  10000 100000   6000 400000]
```

### Output of `seattle-fcc-broadband-bg.py`
```
data.columns: Index(['frn', 'provider_id', 'brand_name', 'location_id', 'technology',
       'max_advertised_download_speed', 'max_advertised_upload_speed',
       'low_latency', 'business_residential_code', 'state_usps', 'block_geoid',
       'h3_res8_id'],
      dtype='object')
census_block_groups.columns: Index(['OBJECTID', 'GEOID20', 'GROSS_ACRES', 'ACRES_LAND', 'ACRES_WATER',
       'TRBG', 'NAMELSAD', 'BG', 'TRACT', 'TRACT_LABEL', 'Shape__Area',
       'Shape__Length', 'geometry'],
      dtype='object')
          GEOID20  max_download_speed_in_tract
0    530330002021                       2000.0
1    530330002022                       2000.0
2    530330004022                       2000.0
3    530330013003                       2000.0
4    530330017013                       2000.0
..            ...                          ...
531  530330074042                       2000.0
532  530330080033                       2000.0
533  530330091001                       8000.0
534  530330092002                       8000.0
535  530330104013                       2000.0

[536 rows x 2 columns]
[  2000.   8000.     nan  10000.   6000.   5000. 100000.   1200.   1500.
 400000.]
```
