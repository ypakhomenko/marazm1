#!/usr/bin/python3
#
# jip, 10.12.2017, falling into marasmus... :-)
#
#
import Point
import math
from Line import Line

class Snowflake:

   def __init__(self, center_p, color = '#000000000', base_length=10): 

      self.l = base_length
      self.centr_p = center_p
      self.color = color
      self.ids = []
      self.lines = []
      self.calculate( center_p, color, base_length )

   def calculate( self, center_p, color, base_length ):

      angl = 0

      lengths = [ base_length*1.5, base_length*2, base_length*1.5, base_length, base_length*1.5, base_length*2 ]
      for i in range(0, 15):
         self.lines.append( Line( center_p, angl, color, lengths[ i%6 ] ) ) 
         angl += 30


   def draw( self, canvas ):

      for l in self.lines:
          id = canvas.create_line(l.p1.x, l.p1.y, l.p2.x, l.p2.y, fill=l.color, smooth=True, width=2)
          self.ids.append( id )

   def clean( self, canvas ):

      for id in self.ids:
          canvas.delete( id )


