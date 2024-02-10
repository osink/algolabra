'''Module for implementing Bowyer-Watson algorithm'''
from point import Point
from triangle import Triangle
from line import Line

class BowyerWatson:
    '''Separate class for containing current Bowyer-Watson calculation'''
    def bowyerwatson(self):
        '''Initialise triangulation list'''
        self.points = []

    def addpoint(self, point:Point):
        '''Add point to triangulation list'''
        self.points.append(point)

    def calculate(self):
        '''Do the calculation'''
        triangles = []
        for point in self.points:
            bads = []
            for triangle in triangles:
                if triangle.incircle(point):
                    bads.append(triangle)
            polygon = []
            for triangle in bads:
                lines = triangle.getlines
                for line in lines:
                    pass
                    # If not common with others in bads, add to polygon
                    # Remove triangle from triangles
            for line in polygon:
                trianglepoints = line.getpoints()
                trianglepoints.append(point)
                new = Triangle(trianglepoints)
                triangles.append(new)
