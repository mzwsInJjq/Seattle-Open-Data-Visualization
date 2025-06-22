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

# 2020 Census Block Groups - Seattle
# https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::2020-census-block-groups-seattle-1

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

data1 = pd.read_csv(r'D:\Misc\bdc_53_FibertothePremises_fixed_broadband_D24_19jun2025.csv')
data2 = pd.read_csv(r'D:\Misc\bdc_53_Cable_fixed_broadband_D24_19jun2025.csv')
data = pd.concat([data1, data2])
census_block_groups = gpd.read_file(r"C:\Users\Chen\Downloads\2020_Census_Block_Groups_-_Seattle.geojson")

print(f"data.columns: {data.columns}")
print(f"census_block_groups.columns: {census_block_groups.columns}")
census_block_groups_list = census_block_groups['GEOID20'].unique().tolist()

# Truncate the 'block_geoid' column to only keep the first 12 characters
data['block_geoid'] = data['block_geoid'].astype(str).str[:12]
# Filter data to only keep rows where 'block_geoid' starts with any elements in the census_block_groups_list
data = data[data['block_geoid'].astype(str).isin(census_block_groups_list)]

# Calculate the max download speed in each tract
max_download_speed_in_block_group = data.groupby('block_geoid')['max_advertised_download_speed'].max().reset_index()
max_download_speed_in_block_group.columns = ['GEOID20', 'max_download_speed_in_tract']

# Merge the max download speed in each tract with the census tracts
census_block_groups = census_block_groups.merge(max_download_speed_in_block_group, on='GEOID20', how='left')

# Print the census tracts with the max download speed in each tract
print(census_block_groups[['GEOID20', 'max_download_speed_in_tract']])
print(census_block_groups['max_download_speed_in_tract'].unique())

# Color the census tracts based on the max download speed in each tract 
census_block_groups['color'] = census_block_groups['max_download_speed_in_tract'].apply(
    lambda x: 'gray' if pd.isnull(x) else plt.cm.Blues(LogNorm(vmin=1200, vmax=400000)(x))
)

census_block_groups.plot(ax=ax, color=census_block_groups['color'], label='Census Block Groups', linewidth=0.4, edgecolor='k')

plt.savefig('seattle-fcc-broadband-bg.pdf', format='pdf', bbox_inches='tight')
plt.show()