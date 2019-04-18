import folium

# map object
m = folium.Map(location=[44.647502, 20.291818], zoom_start=12)

# markers

# generate HTML
m.save("map.html")
