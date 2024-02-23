"""Map is a module for handling the map"""

import random
import math
import tkinter as tk
from bowyerwatson import BowyerWatson
from tile import Tile
from point import Point

class Map:
    """Map class consists of a grid of tile objects, and manages the map"""

    def __init__(self, sizex: int, sizey: int):
        # Initialise an empty grid of tiles of desired size
        self.grid = [[0 for i in range(sizex)] for j in range(sizey)]
        for x in range(sizex):
            for y in range(sizey):
                self.grid[x][y] = Tile(x,y)
        # Currently implementation only for square maps, but initialisation
        # already possible for any rectangular
                
        # Set up info variables
        self.roomcount = 0
        self.corridors = 0
        self.maxrooms = 5
        self.size = sizex
        self.rooms = []
        self.mindist = 4
        self.bw = BowyerWatson()
        self.trianglelist = []

    def __str__(self):
        # Basic print function
        text = ''
        for row in self.grid:
            for tile in row:
                text += str(tile)
            text += '\n'
        return text
    
    def draw(self, canvas: tk.Canvas):
        # Draw map into window
        scale = 10
        for row in self.grid:
            for tile in row:
                xy = tile.getcoords()
                xy = [x * scale for x in xy]
                if tile.checktype() == 'Room':
                    canvas.create_rectangle(xy[0], xy[1], xy[0]+scale, xy[1]+scale, outline="black", fill="red")
                elif tile.checktype() == 'Wall':
                    canvas.create_rectangle(xy[0], xy[1], xy[0]+scale, xy[1]+scale, outline="black", fill="black")
                elif tile.checktype() == 'Corridor':
                    canvas.create_rectangle(xy[0], xy[1], xy[0]+scale, xy[1]+scale, outline="black", fill="blue")
                elif tile.checktype() == 'Unassigned':
                    canvas.create_rectangle(xy[0], xy[1], xy[0]+scale, xy[1]+scale, outline="black", fill="yellow")
        #print(len(self.trianglelist))
        for triangle in self.trianglelist:
           for line in triangle.getlines():
                canvas.create_line(line.getpoints()[0].getcoords()[0]*scale,line.getpoints()[0].getcoords()[1]*scale,
                                line.getpoints()[1].getcoords()[0]*scale,line.getpoints()[1].getcoords()[1]*scale, fill="blue", width="2")
        
    def changetile(self, x: int, y: int, type: str):
        '''Edit tile in x,y for given type'''
        # Editing existing tiles
        self.grid[x][y].changeType(type)

    def generate(self):
        '''Populate given map with random content'''
        # Generate more rooms if max not reached
        while self.roomcount < self.maxrooms:
            self.createroom()

    def triangulate(self):
        '''Calculate Delaunay triangulation for map'''
        self.trianglelist = self.bw.calculate()

    def createroom(self):
        '''Create rooms for given map object'''
        while True:
            # Initialise fail condition
            fail = False
            # Generate random nucleation site
            coordx = random.randrange(self.size)
            coordy = random.randrange(self.size)
            # Check if rooms already within mindist distance of nucleation site
            for room in self.rooms:
                if math.sqrt((room[0] - coordx)**2 + (room[1] - coordy)**2) < self.mindist:
                    fail = True
            if not fail:
                # Add room to roomlist and change according tile's type
                self.rooms.append((coordx,coordy))
                self.bw.addpoint(Point(coordx,coordy))
                self.grid[coordx][coordy].changetype('Room')
                self.roomcount += 1
                break
        # To be here: grow rooms to desired size, check for collisions

    def createcorridors(self):
        '''Create corridors for given map object'''
        # After creating rooms, ensure their connections
        pass
