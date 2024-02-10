'''Module for drawing lines between points'''
from point import Point

class Line:
    '''Line object of two endpoints'''
    def __init__(self, start:Point, end:Point):
        self.points = (start, end)

    def movestart(self, start:Point):
        '''Move the starting point of triangle'''
        self.points = (start, self.points[1])

    def moveend(self, end:Point):
        '''Move the ending point of triangle'''
        self.points = (self.points[1], end)

    def draw(self):
        '''Method for drawing line into UI'''
    
    def getpoints(self):
        return self.points
    