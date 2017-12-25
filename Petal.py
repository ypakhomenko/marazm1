# jip, 25.12.2017, falling into marasmus... :-)

from Line import Line
from Point import Point
import math

class Petal:

   def __init__(self, p, ang, color = '#000000', length=10):

       self.lines = self.calculate( p, ang, color, length )

   def get_lines( self ): return self.lines

   def calculate( self, p, ang, color, length ):

          lines = []
          
          nr_side_lines = 4
          angl_side_l = 45
          # l_side_lines = length / (nr_side_lines*2)
          l_side_lines = length / nr_side_lines
          distance = (1.0 * length) / (nr_side_lines + 1)
          distance = (1.0 * length) / nr_side_lines

          lines.append( Line( p, ang, color, length ) )
          # lines.append( Line( p, ang, '#FF0000', length ) )
          
          x = p.x
          y = p.y
          xx = math.cos( math.radians( ang ))*distance
          yy = math.sin( math.radians( ang ))*distance

          for i in range( 0, nr_side_lines ):
              
              lines.append( Line( Point( x, y ), ang + angl_side_l, color, l_side_lines ) )
              lines.append( Line( Point( x, y ), ang - angl_side_l, color, l_side_lines ) )
              x += xx
              y += yy

          return lines

