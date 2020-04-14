#Abiodun Scott
#Write a program that creates a base class Polygon and prints the
#perimeter, ar4ea, and side lengths of each polygon (subclasses)

import math

#superclass
class Polygon():
    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = []
        self.perimeter = 0.0

    def findPerimeter(self):
        for i in range(self.n):
            self.sides.append(float(input('Enter the length of a side: ')))

        for item in self.sides:
            self.perimeter += item
        print('The perimeter is %.2f' % (self.perimeter))

    def displaySide(self):
        #displays the length for each side
        print('This polygon has %d sides.' % len(self.sides))
        print('This polygon has sides with lengths:', self.sides)
        print()

    #prints the information of the polygon
    def __str__(self):
        displaySide(self)
        print('The perimeter is %.02f' % (self.perimeter))

#subclass for right triangle
class RightTriangle(Polygon):
    #print('Right Triangle')
    def __init__(self, num_of_sides = 3):
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0

    def findPerimeter(self):
        Polygon.findPerimeter(self)

    def displaySide(self):
        print("This triangle has %d sides." % len(self.sides))
        print("This triangle has sides with lengths:", self.sides)

    def findArea(self):
        self.area = self.sides[0] * self.sides[1] * 0.5
        print("The area of the right triangle is %.2f" % self.area)
        print()
        
    #prints properties of the polygon subclass
    def __str__(self):
        Polygon.findPerimeter(self)
#subclass for octagon
class Octagon(Polygon):
    #print('Octagon')
    def __init__(self, num_of_sides = 8):
        #inherits polygon class attributes
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0

    def findPerimeter(self):
        Polygon.findPerimeter(self)

    def displaySide(self):
        print("This octagon has %d sides." % len(self.sides)) #length of the sides list
        print("This octagon has sides with lengths:", self.sides)

    def findArea(self):
        #area of an octagon
        self.area = 2*(1 +math.sqrt(2))*self.sides[0]
        print("The area of the octagon is %.2f" % self.area)
        print()
        
    #prints properties of the polygon subclass
    def __str__(self):
        Polygon.__str__(self)
        
#subclass for square
class Square(Polygon):
   # print('Square')
    def __init__(self, num_of_sides = 4):
        #inherits polygon class attributes
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0

    def findPerimeter(self):
        Polygon.findPerimeter(self)

    def displaySide(self):
        print("This square has %d sides." % len(self.sides)) #length of the sides list
        print("This square has sides with lengths:", self.sides)
       
    def findArea(self):
        #area of a square
        self.area = self.sides[0]*self.sides[1]
        print("The area of the square is %.2f" % self.area)
        print()
        
    #prints properties of the polygon subclass
    def __str__(self):
        Polygon.__str__(self)

if __name__ == '__main__':
    #determines the number of sides of the first polygon
    shape = Polygon(5)
    shape.findPerimeter()
    shape.displaySide()
    
    #instance of right triangle class
    print('Right Triangle')
    tri = RightTriangle()
    tri.findPerimeter()
    tri.displaySide()
    tri.findArea()

    #instance of octagon class
    print('Octagon (sides must be the same length for accurate results)')
    octagon = Octagon()
    octagon.findPerimeter()
    octagon.displaySide()
    octagon.findArea()

    #instance of square class
    print('Square (sides must be the same length for accurate results)')
    square = Square()
    square.findPerimeter()
    square.displaySide()
    square.findArea()

    
