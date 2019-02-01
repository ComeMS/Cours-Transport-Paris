def nearbyStation(positionGPSCoordinates):
  """
    finds the station nearest to the given position and the name of the station
    using stations as the dataframe to find the stations
    Parameters:
    -----------

        positionGPSCoordinates: tuple (lat,long)


    Return:
    -------
    list: Coordinates of neareast station
      [name,lat,long,distance in meters]
  """
  FILEPATH = os.path.join('data','stations.csv')
  stations = pd.read_csv(FILEPATH,index_col=0)

  latS, longS = list(stations.loc[0])[1:]
  dist = distance.vincenty([lat1,long1],[latS,longS]).m
  station=list(stations.loc[0])
  index=0
  for i in range(1,stations.shape[0]):
    latS, longS = list(stations.loc[i])[1:]
    distTemp = distance.vincenty(positionGPSCoordinates,[latS,longS]).m
    if distTemp < dist:
        dist=distTemp
        station=list(stations.loc[i])
    station.append(dist)
    return station

def findShortestPath(sourceStations, destStations):
    """
    """
    pass

def getCoordinates(adress):
    """
    find the coordinates (lat,long) of a given adress
    Parameters:
    -----------
        adress: string
    Return:
    -------
        coordinates: tuple (lat,long)

    """
    geolocator = Nominatim()
    coordinates = geolocator.geocode(adress)[1]
    coordinates = np.array(coordinates)
    return coordinates
