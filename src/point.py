class Point:
    '''Point defines a point in 2D space'''
    def __init__(self, x:int, y:int):
        self.coords = (x, y)

    def transfer(self, x:int, y:int):
        '''Move point to new coords'''
        self.coords = (x, y)

    def getcoords(self):
        '''Return coordinates of point'''
        return self.coords
