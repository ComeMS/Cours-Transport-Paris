def nearbyStations(positionGPSCoordinates):
  """
    finds the stations around the given position and the max distance of search
    Parameters:
    -----------

        positionGPSCoordinates: tuple (lat,long)


    Return:
    -------
    list: Coordinates of neareast station
      (lat,long)
  """
    pass

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
    return coordinates
