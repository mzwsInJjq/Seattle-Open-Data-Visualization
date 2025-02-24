# Seattle Neighborhood Map Atlas Neighborhoods
# https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::neighborhood-map-atlas-neighborhoods

# Seattle Street Network Database SND
# https://data-seattlecitygis.opendata.arcgis.com/datasets/street-network-database-snd-1

# Seattle GeoJSON
# https://polygons.openstreetmap.fr/get_geojson.py?id=237385&params=0

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

nman = gpd.read_file(r"C:\Users\Chen\Downloads\Neighborhood_Map_Atlas_Neighborhoods.geojson")
snd = gpd.read_file(r"C:\Users\Chen\Downloads\Street_Network_Database_SND_5675931800012836898.geojson")
seattle_geojson = gpd.read_file(r"C:\Users\Chen\Downloads\seattle.geojson")
snd = snd[snd["CITYCODE"] == 1]
snd = gpd.overlay(snd, seattle_geojson, how='intersection')

fig, ax = plt.subplots(figsize=(20, 10))
ax.axis('off')
nman.plot(ax=ax, color='b', label='NMAN', alpha=0.5)
snd.plot(ax=ax, color='k', label='SND', linewidth=0.4)

plt.savefig('seattle-snd.pdf', format='pdf', bbox_inches='tight')