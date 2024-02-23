import math
from point import Point
from line import Line

#from line import Line

class Triangle:
    '''Triangle of three point objects'''
    def __init__(self, a:Point, b:Point, c:Point):
        # Create tuple for points
        self.points = [a, b, c]
        try:
            self.circle = self.circumcircle()
        except ZeroDivisionError:
            self.circle = [0,0,0]
        self.lines = self.createlines()

    def __str__(self):
        return str(self.points[0]) + str(self.points[1]) + str(self.points[2])
    
    def __eq__(self, comp):
        return ((self.points[0] == comp.getpoints()[0]) or (self.points[1] == comp.getpoints()[0]) or (self.points[1] == comp.getpoints()[0]) and
                (self.points[0] == comp.getpoints()[1]) or (self.points[1] == comp.getpoints()[1]) or (self.points[2] == comp.getpoints()[1]) and 
                (self.points[0] == comp.getpoints()[2]) or (self.points[1] == comp.getpoints()[2]) or (self.points[2] == comp.getpoints()[2]))

    def createlines(self):
        return ([Line(self.points[0],self.points[1]), Line(self.points[1],self.points[2]),
                  Line(self.points[2],self.points[0])])

    def getlines(self):
        return self.lines

    def getpoints(self):
        '''Return points of triangle'''
        return self.points

    def circumcircle(self):
        '''Calculate centerpoint and radius for triangle's circumcircle'''
        A = self.points[0].getcoords()
        B = self.points[1].getcoords()
        C = self.points[2].getcoords()
        # Calculate circumcircle
        D = (A[0]-C[0])*(B[1]-C[1]) - (B[0]-C[0])*(A[1]-C[1])
        p0 = ((((A[0]-C[0])*(A[0]+C[0])+(A[1]-C[1])*(A[1]+C[1]))/2 
               *(B[1]-C[1])-((B[0]-C[0])*(B[0]+C[0])+(B[1]-C[1])*(B[1]+C[1]))/2*(A[1]-C[1]))/D)
        p1 = ((((B[0]-C[0])*(B[0]+C[0])+(B[1]-C[1])*(B[1]+C[1]))/2
               *(A[0]-C[0])-((A[0]-C[0])*(A[0]+C[0])+(A[1]-C[1])*(A[1]+C[1]))/2*(B[0]-C[0]))/D)
        r = math.sqrt((C[0]-p0)**2+(C[1]-p1)**2)
        return [p0, p1, r]

    def incircle(self, point:Point):
        '''Check if given point is within circumcircle of triangle'''
        p0, p1, r = self.circle
        x, y = point.getcoords()
        return math.sqrt((p0-x)**2+(p1-y)**2) <= r
