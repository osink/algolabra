class Point:
    '''Point defines a point in 2D space'''
    def __init__(self, x:int, y:int):
        self.coords = [x, y]

    def __str__(self):
        return str(self.coords)
    
    def __eq__(self, comp):
        return self.coords[0] == comp.getcoords()[0] and self.coords[1] == comp.getcoords()[1]

    def transfer(self, x:int, y:int):
        '''Move point to new coords'''
        self.coords[0] = x
        self.coords[1] = y

    def getcoords(self):
        '''Return coordinates of point'''
        return self.coords
