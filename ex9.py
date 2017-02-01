import math


class Parallelogram(object):
    '''A parallelogram that has a side, base, an angle'''
    def __init__(self, base, side, theta):
        '''(float, float, float) -> NoneType
        Creates a parallelogram'''

        # initiazing variables
        self._base = base
        self._side = side
        self._theta = theta
        # declaring a shape
        self._shape = 'Parallelogram'

    def __str__(self):
        '''(Parallelogram) -> str
        Returns a string representation of Parallelogram'''
        area = str(Parallelogram.area(self))
        # declaring the shape
        shape = self._shape
        return 'I am a ' + shape + ' with area ' + area

    def area(self):
        '''(Parallelogram) -> float
        Gets the area of a parallelogram object given
        the base length, the side length, and the angle
        REQ: theta > 0
        REQ: side > 0
        REQ: base > 0
        '''
        # getting area using formula base * side * sintheta
        # calls converts theta to radians instead of degrees
        theta_radians = math.radians(self._theta)
        # gets sin theta
        sin_theta = math.sin(theta_radians)
        # solving for area with formula base * side * sin(theta)
        area = self._base * self._side * sin_theta

        self._area = area

        return self._area

    def bst(self):
        '''(Parallelogram) -> list
        Returns a list of all parameters of a Parallelogram'''

        Parameters = [self._base, self._side, self._theta]

        return Parameters


class Rhombus(Parallelogram):
    '''A  class to represent a Rhombus that is a parallelogram'''
    def __init__(self, base, theta):
        '''(float, float, float) -> NoneType
        Creates a parallelogram'''
        # Takes in the same parameters as parallelogram with
        # the two sides being equal
        Parallelogram.__init__(self, base, base, theta)
        # Declaring the shape
        self._shape = 'Rhombus'


class Rectangle(Parallelogram):
    '''A class to represent a rectangle that is a parallelogram'''
    def __init__(self, base, side):
        '''(float, float, float) -> NoneType
        Creates a rectangle'''

        # Takes in the same parameters as a parallelogram
        # in a rectangle, the theta will always be 90
        Parallelogram.__init__(self, base, side, 90)
        # Declares the shape to be a rectangle
        self._shape = 'Rectangle'


class Square(Parallelogram):
    '''A class to represent a square that is a parallelogam'''
    def __init__(self, base):
        '''(float) -> NoneType
        Creates a square'''

        # Takes in the same parameters as a parallelogram
        # theta will always be 90 in a square
        Parallelogram.__init__(self, base, base, 90)
        # Declares self._shape as it is a different shape
        self._shape = 'Square'
