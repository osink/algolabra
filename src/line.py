'''Module for drawing lines between points'''
from point import Point

class Line:
    '''Line object of two endpoints'''
    def __init__(self, start:Point, end:Point):
        self.points = [start, end]

    def __eq__(self, comp: Point):
        return ((self.points[0] == comp.getpoints()[0] and self.points[1] == comp.getpoints()[1]) or 
                (self.points[0] == comp.getpoints()[1] and self.points[1] == comp.getpoints()[0]))

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
    