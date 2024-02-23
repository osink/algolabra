"""Tile is a module for managing individual tiles"""

# Types are 'Unassigned', 'Wall', 'Room' and 'Corridor'
# To be: assign attribute list for different types and enable user generated types

class Tile:
    """Tile class contains information about the tile, on which a map can be constructed."""    
    def __init__(self, coordx: int, coordy: int) -> None:
        # Creates an empty tile at coordx,coordy
        self.x = coordx
        self.y = coordy
        self.type = 'Unassigned'
        self.content = 'None'

    def getcoords(self):
        return [self.x,self.y]

    def changetype(self, typ: str):
        '''Changes type of tile to type'''
        self.type = typ

    def changecontent(self, content: str):
        '''Changes content of tile to content'''
        self.content = content

    def checktype(self):
        '''Return type of tile'''
        return self.type

    def __str__(self):
        # Print symbols for given tiles
        if self.type == 'Unassigned':
            return '?'
        elif self.type == 'Wall':
            return '#'
        elif self.type == 'Room':
            return '$'
        elif self.type == 'Corridor':
            return '£'
        else:
            return 'N'
