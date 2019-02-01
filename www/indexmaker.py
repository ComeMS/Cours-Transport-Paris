import folium
departureLat = 48.862969
departureLon = 2.359903
arrivalLat = 48.863969
arrivalLon = 2.369903

Map = folium.Map(
        location=[48.852969, 2.349903], #target Paris
        zoom_start=12)

departureInfo = 'Hey here u start'
arrivalInfo = 'Hey here u go'

folium.Marker([departureLat, departureLon], popup='<i>Mt. Hood Meadows</i>', tooltip=departureInfo).add_to(Map)
folium.Marker([arrivalLat, arrivalLon], popup='<b>Timberline Lodge</b>', tooltip=arrivalInfo).add_to(Map)

Map

#Map.save('indexbypython.html')