import os
from os.path import join
import json
import folium

# map object
m = folium.Map(location=[44.647502, 20.291818], zoom_start=12)

# global tooltip
tooltip1 = "Click for more info! "
tooltip2 = "Click for more info! "
tooltip3 = "Click for more info! "
tooltip4 = "This is my school. More info! "
tooltip5 = "Click for more info! "
tooltip6 = "Click for more info! "
tooltip7 = "Forex Stock Exchange Forum. More info! "
tooltip8 = "Restricted area.More info! "
tooltip9 = "Click for more info! "
tooltip10 = "Kosutnjak Forest! "
# icon marker
Logo1 = folium.features.CustomIcon('forex_tr_19.png', icon_size=(35, 35))

# vega
visData = os.path.join('data', 'vis.json')

# geo data
geoOverlay =os.path.join('data', 'geoOverlay.json')
# markers
folium.Marker([44.818181, 20.294455],
              popup="'Nikola Tesla' International  Airport",
              tooltip=tooltip1,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.823360,20.450313],
              popup="Belgrade Fortress",
              tooltip=tooltip2,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.825597,20.454002],
              popup="Zoo",
              tooltip=tooltip3,
              icon=folium.Icon(color="green", icon="cloud")).add_to(m),
folium.Marker([44.810311,20.460782],
              popup="'Nikola Tesla' High School",
              tooltip=tooltip4,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.796171, 20.437084],
              popup="The Belgrade Fair. ",
              tooltip=tooltip5,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.786568, 20.427067],
              popup="Hippodrome / Racecourse  ",
              tooltip=tooltip6,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.814877, 20.455335],
              popup="Best Trading Community in SouthEast Europe.",
              tooltip=tooltip7,
              icon=Logo1).add_to(m),
folium.CircleMarker(
              location=[44.770493,20.469921],
              radius=30,
              popup="The Military Academy of the University of Defence.",
              tooltip=tooltip8,
              color='#fc5628',
              fill=True,
              fill_color='#fc5628').add_to(m),
# vis marker
folium.Marker(
              location=[44.829768, 20.433458],
              tooltip=tooltip9,
              popup=folium.Popup(max_width=550).add_child(folium.Vega(json.load(open(visData)), width=550, height=250))).add_to(m)

# geo marker
folium.GeoJson(geoOverlay,tooltip=tooltip10, name='Kosutnjak Forest', ).add_to(m)


# generate HTML
m.save("map.html")
