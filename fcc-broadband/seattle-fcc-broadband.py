# Seattle Neighborhood Map Atlas Neighborhoods
# https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::neighborhood-map-atlas-neighborhoods

# Seattle Street Network Database SND
# https://data-seattlecitygis.opendata.arcgis.com/datasets/street-network-database-snd-1

# Seattle GeoJSON
# https://polygons.openstreetmap.fr/get_geojson.py?id=237385&params=0

# Seattle City Limits
# https://data-seattlecitygis.opendata.arcgis.com/maps/seattle-city-limits-2

# Data Download | FCC National Broadband Map
# https://broadbandmap.fcc.gov/data-download

# broadband-map-data-downloads.pdf
# https://us-fcc.app.box.com/v/bdc-data-downloads-output

# 2020 Census Tracts - Seattle
# https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::2020-census-tracts-seattle/

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

nman = gpd.read_file(r"C:\Users\Chen\Downloads\Neighborhood_Map_Atlas_Neighborhoods.geojson")
snd = gpd.read_file(r"C:\Users\Chen\Downloads\Street_Network_Database_SND_5675931800012836898.geojson")
seattle_geojson = gpd.read_file(r"C:\Users\Chen\Downloads\seattle.geojson")
snd = snd[snd["CITYCODE"] == 1]
snd = gpd.overlay(snd, seattle_geojson, how='intersection')
scl = gpd.read_file(r"C:\Users\Chen\Downloads\Seattle_City_Limits_-2760504394019241448.geojson")

fig, ax = plt.subplots(figsize=(20, 10))
ax.axis('off')
nman.plot(ax=ax, color='gray', label='NMAN', alpha=0.5)
snd.plot(ax=ax, color='black', label='SND', linewidth=0.4, alpha=0.25)
scl.plot(ax=ax, color='red', label='SCL', linewidth=0.6, edgecolor='k')

data1 = pd.read_csv(r'C:\Users\Chen\Downloads\bdc_53_FibertothePremises_fixed_broadband_J24_04mar2025.csv')
data2 = pd.read_csv(r'C:\Users\Chen\Downloads\bdc_53_Cable_fixed_broadband_J24_04mar2025.csv')
data = pd.concat([data1, data2])
census_tracts = gpd.read_file(r"C:\Users\Chen\Downloads\2020_Census_Tracts_Seattle_600198261190227915.geojson")

print(f"data.columns: {data.columns}")
print(f"census_tracts.columns: {census_tracts.columns}")
census_tracts_list = census_tracts['GEOID20'].unique().tolist()

# Truncate the 'block_geoid' column to only keep the first 11 characters
data['block_geoid'] = data['block_geoid'].astype(str).str[:11]
# Filter data to only keep rows where 'block_geoid' starts with any elements in the census_tracts_list
data = data[data['block_geoid'].astype(str).isin(census_tracts_list)]

# Calculate the max download speed in each tract
max_download_speed_in_tract = data.groupby('block_geoid')['max_advertised_download_speed'].max().reset_index()
max_download_speed_in_tract.columns = ['GEOID20', 'max_download_speed_in_tract']

# Merge the max download speed in each tract with the census tracts
census_tracts = census_tracts.merge(max_download_speed_in_tract, on='GEOID20', how='left')

# Print the census tracts with the max download speed in each tract
print(census_tracts[['GEOID20', 'max_download_speed_in_tract']])
print(census_tracts['max_download_speed_in_tract'].unique())

# Color the census tracts based on the max download speed in each tract
census_tracts['color'] = census_tracts['max_download_speed_in_tract'].apply(
    lambda x: 'gray' if pd.isnull(x) else plt.cm.Blues(LogNorm(vmin=940, vmax=400000)(x))
)

census_tracts.plot(ax=ax, color=census_tracts['color'], label='Census Tracts', linewidth=0.5, edgecolor='k')

plt.savefig('seattle-fcc-broadband.pdf', format='pdf', bbox_inches='tight')
plt.show()