import pandas as pd
import folium
from folium.plugins import MarkerCluster

lat_c = 37.53165351203043
lon_c = 126.9974246490573

m = folium.Map(location=[lat_c, lon_c], zoom_start=11)

csv = pd.read_csv('c:/conv_seoul_jae-seor-ham.csv',
                   encoding='cp949',
                   sep=",",)

marker_cluster = MarkerCluster().add_to(m)

for idx, row in csv.iterrows():

    lat_ = row['lat']
    lon_ = row['lon']

    folium.Marker(location=[lat_, lon_],
                  radius=10
                  ).add_to(marker_cluster)

gungsaro = pd.read_csv('c:/gungsaro.csv',
                   encoding='cp949',
                   sep=",",)

for idx, row in gungsaro.iterrows():

    lat_ = row['lat']
    lon_ = row['lon']

    folium.Marker(location=[lat_, lon_],
                  radius=10,
                  icon= folium.Icon(color='red', icon='star'),
                  ).add_to(m)

m.save('gungsaro.html')