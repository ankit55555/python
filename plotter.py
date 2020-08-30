import numpy as np
import pandas as pd
import folium as fo
%matplotlib inline
map = fo.Map()
map

x = fo.FeatureGroup(name='My Map')
x.add_child(fo.Marker(location=[27.1750,78.0422] , popup='hey' , icon=fo.Icon(color='blue')))
<folium.map.FeatureGroup at 0x1225af9e8>
map.add_child(x)

for lat,lon in ([34,53],[24,-50],[90,-68]):
    x.add_child(fo.Marker(location=[lat,lon] ,
                          popup='hey' , icon=fo.Icon(color='red')))
map.add_child(x)

volcano = pd.read_csv('volcano.csv')
lat_vo = list(volcano['Latitude'])
lon_vo = list(volcano['Longitude'])
name_vo = list(volcano['Name'])
vol = fo.FeatureGroup(name='My Map')
for lat,lon,name in zip(lat_vo,lon_vo,name_vo):
    vol.add_child(fo.Marker(location=[lat,lon] ,
                          popup=name , icon=fo.Icon(color='red')))
map.add_child(vol)
vol.add_child(fo.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))
<folium.map.FeatureGroup at 0x117af8588>
map.add_child(vol)

popu = pd.read_csv('us cities pop.csv')
popu.head()
name	pop	lat	lon
0	New York	8287238	40.730599	-73.986581
1	Los Angeles	3826423	34.053717	-118.242727
2	Chicago	2705627	41.875555	-87.624421
3	Houston	2129784	29.758938	-95.367697
4	Philadelphia	1539313	39.952335	-75.163789
lat_po = list(popu['lat'])
lon_po = list(popu['lon'])
name_po = list(popu['name'])
pop_po = list(popu['pop'])
po = fo.FeatureGroup(name='My Map')
def mar(popu):
    if(popu>35000):
        return 'red'
    elif(popu>10000 and popu<=35000):
        return 'blue'
    else:
        return 'green'
for lat,lon,name,pop in zip(lat_po,lon_po,name_po,pop_po):
    po.add_child(fo.Marker(location=[lat,lon],popup=[pop,name] ,
                          icon=fo.Icon(color=mar(pop))))
map.add_child(po)import numpy as np
import pandas as pd
import folium as fo
%matplotlib inline
map = fo.Map()
map

x = fo.FeatureGroup(name='My Map')
x.add_child(fo.Marker(location=[27.1750,78.0422] , popup='hey' , icon=fo.Icon(color='blue')))
<folium.map.FeatureGroup at 0x1225af9e8>
map.add_child(x)

for lat,lon in ([34,53],[24,-50],[90,-68]):
    x.add_child(fo.Marker(location=[lat,lon] ,
                          popup='hey' , icon=fo.Icon(color='red')))
map.add_child(x)

volcano = pd.read_csv('volcano.csv')
lat_vo = list(volcano['Latitude'])
lon_vo = list(volcano['Longitude'])
name_vo = list(volcano['Name'])
vol = fo.FeatureGroup(name='My Map')
for lat,lon,name in zip(lat_vo,lon_vo,name_vo):
    vol.add_child(fo.Marker(location=[lat,lon] ,
                          popup=name , icon=fo.Icon(color='red')))
map.add_child(vol)
vol.add_child(fo.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))
<folium.map.FeatureGroup at 0x117af8588>
map.add_child(vol)

popu = pd.read_csv('us cities pop.csv')
popu.head()
name	pop	lat	lon
0	New York	8287238	40.730599	-73.986581
1	Los Angeles	3826423	34.053717	-118.242727
2	Chicago	2705627	41.875555	-87.624421
3	Houston	2129784	29.758938	-95.367697
4	Philadelphia	1539313	39.952335	-75.163789
lat_po = list(popu['lat'])
lon_po = list(popu['lon'])
name_po = list(popu['name'])
pop_po = list(popu['pop'])
po = fo.FeatureGroup(name='My Map')
def mar(popu):
    if(popu>35000):
        return 'red'
    elif(popu>10000 and popu<=35000):
        return 'blue'
    else:
        return 'green'
for lat,lon,name,pop in zip(lat_po,lon_po,name_po,pop_po):
    po.add_child(fo.Marker(location=[lat,lon],popup=[pop,name] ,
                          icon=fo.Icon(color=mar(pop))))
map.add_child(po)