import pandas as pd
import folium
import re

data_traffic = pd.read_csv('TAREA12_FINAL/data/Chicago_Traffic_Tracker_Congestion_Estimates_by_Regions.csv', delimiter=',')

print(data_traffic.head())
print("\n\n",data_traffic.describe())
print("\n\n",data_traffic.info())
print("\n\n",data_traffic.isnull().sum())
print("\n\n",data_traffic.duplicated().sum())

columnas_eliminar = ['CURRENT_SPEED', 'LAST_UPDATED']
data_traffic = data_traffic.drop(columns=columnas_eliminar)
print("\n\n",data_traffic.head())

data_traffic['REGION'] = data_traffic['REGION'].astype('string')
data_traffic['REGION'] = data_traffic['REGION'].astype('string')


data_traffic = data_traffic.rename(columns={'REGION': 'region', 
                                            'REGION_ID': 'region_id',
                                            'WEST': 'west',
                                            'EAST': 'east',
                                            'SOUTH': 'south',
                                            'NORTH': 'north',
                                            'DESCRIPTION': 'description'})

print("\n\n",data_traffic.info())
print(data_traffic.head())


# ____________________________________GRAFICA DEL MAPA_________________________________________________________________________

# diccionario de colores
colores = {
    'Riverdale-Hegewisch': 'blue',
    'Near North': 'green',
    'Washington Hts-Roseland-Pullman': 'red',
    'Ashburn': 'purple',
    'Chicago Loop': 'orange',
    'Austin': 'pink',
    'Humboldt-Garfield Prk E/W': 'lightblue',
    'South Deering-East Side': 'yellow',
    'Beverly-Mt Greenwood-Morgan Park': 'brown',
    'Bridgeport-McKinley-Lower West': 'gray',
    'Hyde Park-Kenwood-Woodlawn': 'darkgreen',
    'Downtown Lakefront': 'olive',
    'Midway-Garfield Rdg-Clearing': 'cyan',
    'Edge Water-Uptown': 'lightgreen',
    'Irving Park-Avondale-North Ctr': 'darkpurple',
    'Near South-Douglas': 'lightred',
    'South West Side': 'darkorange',
    'Far North West': 'darkblue',
    'West Town-Near West': 'pink',
    'South Shore-S Chicago-Avlon': 'lightgray',
    'Lawndale N/S': 'darkred',
    'Hermosa-Logan Square': 'darkpink',
    'Dunning-Portage-Belmont Cragn': 'darkyellow',
    'Auburn Gresham-Chatham': 'darkbrown',
    'Lincoln Park-Lake View': 'lightbrown',
    'New City-Englewood-W Englewood': 'darkcyan',
    'Rogers Park - West Ridge': 'lightpurple',
    'North Park-Albany-Lincoln Sq': 'darkgreen',
    'Fuller-Grand Blvd-Washington Park': 'darkolivegreen',
}


# coordenadas de la ciudad e chicago
chicago_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11)

# agrega formas/figuras que representan las areas provistas por el dataset
for index, row in data_traffic.iterrows():
    region_name = row['region']
    if region_name in colores:
        region_polygon = folium.Polygon(
            locations=[
                (row['south'], row['west']),
                (row['south'], row['east']),
                (row['north'], row['east']),
                (row['north'], row['west']),
            ],
            color='black',
            fill=True,
            fill_color=colores[region_name],  # agrega color a la region
            fill_opacity=0.5,
            popup=row['region'] # mensaje pop
        )
        region_polygon.add_to(chicago_map)


chicago_map.save("TAREA12_FINAL/data/chicago_regions_colored_map.html")