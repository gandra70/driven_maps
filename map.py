import folium



# map object
m = folium.Map(location=[44.647502, 20.291818], zoom_start=12)

# global tooltip
tooltip1 = "Belgrade Airport. Click for more info! "
tooltip2 = "Belgrade Fortress. Click for more info! "
tooltip3 = "Belgrade Zoo. Click for more info! "
tooltip4 = "High School of Electrical Engineering 'Nikola Tesla'. Click for more info! "
tooltip5 = "Belgrade Fair . Click for more info! "
tooltip6 = "Belgrade Racecourse. Click for more info! "
tooltip7 = "Forex Stock Exchange Forum. Click for more info! "

# icon marker
Logo1 = folium.features.CustomIcon('forex_tr_19.png', icon_size=(35, 35))
# markers
folium.Marker([44.818181, 20.294455],
              popup="Belgrade Nikola Tesla Airport is an international airport serving Belgrade. It is the largest airport in Serbia, situated 18 km west of downtown.",
              tooltip=tooltip1,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.823360,20.450313],
              popup="Belgrade Fortress, consists of the old citadel and Kalemegdan Park on the confluence of the River Sava and Danube, in an urban area of modern Belgrade, the capital of Serbia. It is located in Belgrade's municipality of Stari Grad.",
              tooltip=tooltip2,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.825597,20.454002],
              popup="Beo zoo vrt, also known as Vrt dobre nade, is a zoo located in Kalemegdan Park, downtown of Belgrade, Serbia. Considered to be one of the oldest public zoos in southeastern Europe, it was founded in 1936 and is the biggest zoo in the country.",
              tooltip=tooltip3,
              icon=folium.Icon(color="green", icon="cloud")).add_to(m),
folium.Marker([44.810311,20.460782],
              popup="This is my school",
              tooltip=tooltip4,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.796171, 20.437084],
              popup="The Belgrade Fair is a large complex of three large domes and a dozen of smaller halls. It is located in the municipality of Savski Venac, on the right bank of the Sava river. ",
              tooltip=tooltip5,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.786568, 20.427067],
              popup="Racecourse at Careva Cuprija is the oldest sports facility in Belgrade. By the Decree of King Alexander dated 15th November 1920, the Danube Riders’ Circle Knez Mihajlo was alloted the state land free of lease for a period of 75 years, for the purpose of fulfilling the need for the permanent racetrack for public horse games.",
              tooltip=tooltip6,
              icon=folium.Icon(color="blue", icon="cloud")).add_to(m),
folium.Marker([44.814877, 20.455335],
              popup="Best Trading Community in SouthEast Europe.",
              tooltip=tooltip7,
              icon=Logo1).add_to(m),
# generate HTML
m.save("map.html")
