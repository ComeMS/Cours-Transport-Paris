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

