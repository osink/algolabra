from map import Map
from tile import Tile


def main():
    # Create empty map
    newMap = Map(50,50)
    # Generate content for map !!FUNCTION ITSELF WORK IN PROGRESS!!
    newMap.generate()
    # Print map
    print(newMap)

if __name__ == '__main__':
    main()