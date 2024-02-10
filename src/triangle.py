from point import Point
#from line import Line

class Triangle:
    '''Triangle of three point objects'''
    def __init__(self, a:Point, b:Point, c:Point):
        # Create tuple for points
        self.points = (a, b, c)

    def getpoints(self):
        return self.points
    
        