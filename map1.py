from inspect import isframe
from unicodedata import name
import folium
import pandas

data = pandas.read_csv('reef.txt')
reefname = list(data['name'])
lat = list(data['lat'])
lon = list(data['lon'])
blk = list(data['blk'])

#to be fleshed out in future, color change based on coordinates or average temperature
def color_prod(lon):
    if lon < 60:
        return 'red'
    elif lon <= 148:
        return 'lightgreen'

html = '''
Reef Name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br> '''

#create the map object
map = folium.Map(location=[-19.259, 146.8], zoom_start=8, tiles="Stamen Terrain")
#adding elements to the map
#using feature group
fg = folium.FeatureGroup(name='My Map')

for lt, ln, name in zip(lat, lon, reefname):
    iframe = folium.IFrame(html=html % (name, name), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_prod(ln))))

map.add_child(fg)


map.save('Map1.html')
