#!/usr/bin/python3
#
# jip, 25.12.2017, falling into marasmus... :-)
#
#
import Point
import math
from Line import Line
from Petal import Petal

class Snowflake:

   def __init__(self, center_p, color = '#000000000', base_length=10, angl=0, direction=1, form='round'): 

      self.l = base_length
      self.centr_p = center_p
      self.color = color
      self.ids = []
      self.petals = []
      self.angl = angl
      self.direction = direction
      self.calculate( center_p, color, base_length, angl, form )
      self.form = form


   def calc( self ): self.calculate( self.centr_p, self.color, self.l, self.angl, self.form )
   def calculate( self, center_p, color, base_length, start_angl, form ):

      del self.petals[:]

      angl = start_angl

      if form == 'round':
          lengths = [ base_length, base_length, base_length, base_length, base_length, base_length ]
      elif form == 'symmetrical':
          lengths = [ base_length*1.5, base_length*2, base_length*1.5, 2*base_length, base_length*1.5, base_length*2 ]
      elif form == 'asymmetrical':
          lengths = [ base_length*1.5, base_length*2, base_length*1.5, 2.5*base_length, base_length*1.5, base_length*2 ]

      for i in range(0, 15):
         self.petals.append( Petal( center_p, angl, color, lengths[ i%6 ] ) ) 
         #self.petals.append( Petal( center_p, angl, color, base_length ) ) 
         angl += 30


   def draw( self, canvas ):

      del self.ids[:]

      for pet in self.petals:
          lines = pet.get_lines()
          for l in lines:
               id = canvas.create_line(l.p1.x, l.p1.y, l.p2.x, l.p2.y, fill=l.color, smooth=True, width=1)
               self.ids.append( id )
               # print( len( self.ids ) )

   def mv( self, canvas, x, y ):
       
       for id in self.ids: 
           # print( "Moving id: ", id )
           
           canvas.move( id, x, y )

   def clean( self, canvas ):

      for id in self.ids:
          canvas.delete( id )
      del self.ids[:]
      del self.petals[:]

