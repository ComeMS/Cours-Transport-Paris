"""
Main program

    Parameters:
    -----------
    addressSource: tuple
        (x,y)
    addressDest: tuple
        (x,y)

    Return:
    -------
    tuple
      (itinerary, distance, time)
"""
import sys
import dataImport
import dataOuput
import process

#geopy
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

import os
import pandas as pd


if __name__ == "__main__":
if len(sys.argv) == 4:

        sourcePositionGPSCoordinates = sys.argv[1]
        destPositionGPSCoordinates = sys.argv[2]
        radius = sys.argv[3]
        sourceStations = nearbyStations(radius, sourcePositionGPSCoordinates)
        destStations = nearbyStations(radius, destPositionGPSCoordinates)
        findShortestPath(sourceStations, destStations)

    else:
        print("Usage: python main.py <sourcePostion> <destPostion> <radius>")


adress1 = "55 Rue des Petits Champs, 75001 Paris"
adress2 = "8 Rue Scribe, 75008 Paris"

lat1, long1 = getCoordinates(adress1)
lat2, long2 = getCoordinates(adress2)
