#!/usr/bin/python3
#
# jip, 09.12.2017, falling into marasmus... :-)
#
# Independently of the used graphical toolkit, a line may be defined through its begining point, angle, length and color
#

# pull test
#
import Point
import math

class Line:

   def __init__(self, p, ang, color = '#000000000', length=10):

      self.length = length
      self.p1 = p
      self.ang = ang
      self.color = color
      self.p2 = self.calculate()

   def calculate( self ): 
      
      #x = math.ceil( math.cos( math.radians( ang ))*self.length + self.p1.x )
      #y = math.ceil( math.sin( math.radians( ang ))*self.length + self.p1.y )
      x = math.cos( math.radians( self.ang ))*self.length + self.p1.x
      y = math.sin( math.radians( self.ang ))*self.length + self.p1.y

      return( Point.Point(x,y) )
