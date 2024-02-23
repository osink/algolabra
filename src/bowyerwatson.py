'''Module for implementing Bowyer-Watson algorithm'''
from point import Point
from triangle import Triangle
from line import Line

class BowyerWatson:
    '''Separate class for containing current Bowyer-Watson calculation'''
    def __init__(self):
        '''Initialise triangulation list'''
        self.pointlist = []

    def __str__(self):
        text = ""
        for point in self.pointlist:
            text += str(point) +" \n"
        return text

    def addpoint(self, point:Point):
        '''Add point to triangulation list'''
        self.pointlist.append(point)

    def calculate(self):
        '''Do the calculation'''
        triangles = []
        print("Start triangluation: \n")
        # Generate massive supertriangle
        supertriangle = Triangle(Point(0,0),Point(10000,0),Point(0,10000))
        triangles.append(supertriangle)
        #print(len(self.pointlist))
        for point in self.pointlist:
            bads = []
            for triangle in triangles:
                if not (point == triangle.getpoints()[0] or point == triangle.getpoints()[1] or point == triangle.getpoints()[2]):
                    try:
                        if triangle.incircle(point):
                            bads.append(triangle)
                    except ZeroDivisionError:
                        bads.append(triangle)
            polygon = []
            for triangle in bads:
                lines = triangle.getlines()
                bads2 = bads
                bads2.remove(triangle)
                for line in lines:
                    fail = False
                    # If not common with others in bads, add to polygon
                    for tri in bads2:
                        lis = tri.getlines()
                        for li in lis:
                            if li == line:
                                fail = True
                    if not fail:
                        polygon.append(line)
                for line in polygon:
                    trianglepoints = line.getpoints()
                    trianglepoints.append(point)
                    new = Triangle(trianglepoints[0],trianglepoints[1],trianglepoints[2])
                    triangles.append(new)
                triangles.remove(triangle)
        triangles2 = []
        print(len(triangles))
        for triangle in triangles:
            if (triangle.getpoints()[0] == supertriangle.getpoints()[0] or triangle.getpoints()[0] == supertriangle.getpoints()[1] or 
                triangle.getpoints()[0] == supertriangle.getpoints()[2] or triangle.getpoints()[1] == supertriangle.getpoints()[0] or 
                triangle.getpoints()[1] == supertriangle.getpoints()[1] or triangle.getpoints()[1] == supertriangle.getpoints()[2] or 
                triangle.getpoints()[2] == supertriangle.getpoints()[0] or triangle.getpoints()[2] == supertriangle.getpoints()[1] or 
                triangle.getpoints()[2] == supertriangle.getpoints()[2]):
                pass
            else:
                triangles2.append(triangle)
        print(len(triangles2))
        return triangles2
