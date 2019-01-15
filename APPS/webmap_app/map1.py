''''
ibrary needed folium
pip install folium

the base layer of the map comes from openstreetmaps
'''
import folium
import pandas


def color_prod(elev):
    if elev < 1500:
        return 'green'
    elif 1500 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[80,-100])  # create a Map object. Pass lat and long to the location
# if you want specific coordinates, copy them from maps.google.com - Select a location, right click, and choose "What's here"
map = folium.Map(location=[80,-100], zoom_start=6)  # you can play with the initial zoom as well
map = folium.Map(location=[80,-100], zoom_start=6, tiles="Mapbox Bright")  # you can change the default layer


# add a marker to the map
map.add_child(folium.Marker(location=[80,-100], popup="Hi I am a marker", icon=folium.Icon(color='green')))

# recommended way is to create a feature group to add a marker to your map

fg = folium.FeatureGroup(name="My Map")
# the marker is a feature, so instead of adding it directly to the map, you add it to the group
fg.add_child(folium.Marker(location=[80,-100], popup="Hi I am a marker", icon=folium.Icon(color='green', prefix='fa')))   #1
# and then you pass the FeatureGroup group as a child to the map
map.add_child(fg)

# one way to add multiple markers to the mas is to repeat #1 and change the parameters (loc, text, color etc)
# second way is to use a for loop:
for coordinates in [[81,-100],[81,-101]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='green')))   #1

# 3rd way is from a file
data = pandas.read_csv("Volcanoes_USA.txt")   # generate a data frame with pandas
lat = list(data["LAT"])    # create separate lists for LAT and LON
lon = list(data["LON"])

# for lt, ln in zip(lat, lon):
#     fg.add_child(folium.Marker(location=[lt,ln], popup="Hi I am a marker", icon=folium.Icon(color='green')))


# focus on popup to make info dynamic

elev = list(data["ELEV"])
for lt, ln, el in zip(lat, lon, elev):
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(el), icon=folium.Icon(color='green')))
    # fg.add_child(folium.Marker(location=[lt,ln], popup="Elevation: "+str(el)+" m", icon=folium.Icon(color='green')))    # or we can add even more text

    # in case there are quotes (') in the popup string, we might get a blank webpage. To change this we need to use another parameter for popup
    # popup = folium.Popup(str(el), parse_html=True)
    # fg.add_child(folium.Marker(location=[lt,ln], popup=popup, icon=folium.Icon(color='green')))


# focus on icons
# change their color to signify the elevation range (green = 0-2000m, orange = 2000-3000 m, red = +3000 m)
# we can create a function to do this for us !!! see the function definition up
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(el), icon=folium.Icon(color=color_prod(el))))


# change the marker to a circle
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el),radius=6, fill=True, fill_color=color_prod(el), color='grey', fill_opacity=0.7))



# add another layer to the map - a polygon layer (1st is the map, 2nd is the markers (point layer), and we can have also line layers to signal roads or rivers for example)
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))

# add color-based polygon featuers
# we will show the population of each country by different color (in ranges)
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'yellow'}))  #this will make all polygons filled with yellow
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# x is mapped to features inside the json file by GeoJson, and actually the method will loop through all of them to find the properties-pop2005 values



# adding a layer control panel (turn on and off the layers (except the base map))
map.add_child(folium.LayerControl())   #basic control (controls all layers at once because we added just one child to the map - the feature group, but the group contains 2 layers)
# solution would be to create feature groups for each layer or group of layers that you want to have separate


map.save("Map1.html") # save the map to html
