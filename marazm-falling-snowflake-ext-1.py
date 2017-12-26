#!/usr/bin/python3
#
# jip, 25.12.2017, falling into marasmus... :-)
#
import sys

import tkinter
from tkinter import Button
from tkinter import TOP, BOTTOM, LEFT
import time
from random import randint

#from Line import Line
from Point import Point
from SnowflakeExt import Snowflake

def quit(): 
    root.destroy()
    sys.exit(0)

def get_color( r, g, b ):
    c = '#%02x%02x%02x' % (r, g, b)
    return c



# ------------------------------------
root = tkinter.Tk()
root.title("... marasmus was getting stronger ...")

Button(root, text="ой фсё...", command=quit).pack( side = BOTTOM )
W=1200
H=800
canvas = tkinter.Canvas(root, width=W, height=H, background='black')
canvas.pack()

def start():

     h = int( canvas['height'] )
     w = int( canvas['width'] )
     number_w = 6
     between_w = w/number_w

     r = 255
     g = 255
     b = 255

     x = 0
     y = 0

     sfss = []
     distance = 45
     step = distance

     xxxx = 0
     xdirection = 1    
     shift = 0
     kinds = [ 'round', 'symmetrical', 'asymmetrical' ]
     kinds_nr = 0
 
     while True:

         
         xxxx += xdirection
         if xxxx == 18 or xxxx == -80: xdirection *= (-1)
         if xxxx == -8 and step % 5 == 0: xdirection *= (-1) 

         if step % distance == 0:

             if kinds_nr < 3: 
                factor = 1.5
                index = 0
             elif kinds_nr < 6: 
                index = 1
                factor = 1
             else : 
                index = 2
                factor = 0.75

             kinds_nr += 1
             if kinds_nr == 9: kinds_nr = 0
             k =  kinds[ index ]

             sfs = []

             while x < w + 80:
                lw = randint(0, 5)
                direction = randint(0, 1)
                if direction == 0: direction = -1
                if step%5 == 0: direction *= (-1)

                l = randint(20, 30) * factor

                start_angle = randint(-10, 10)
                x_delta = randint(-40, 40)
                y_delta = randint(-80, 0)

                s = Snowflake( Point( x+x_delta, y_delta ), get_color( r, g, b ), l, start_angle, direction, k, lw )
                s.draw( canvas )
                sfs.append( s )
                x += between_w

             sfss.insert( 0, sfs )
             # sfss.append( sfs )
             x = 0
         step += 1

         time.sleep(0.04)
         canvas.update()
         # time.sleep(0.0001)

         for i in range( len( sfss ) ):
             for j in range( len( sfss[ i ] ) ):
               sfss[ i ][ j ].clean( canvas )
               if xxxx < -7: 
                   sfss[ i ][ j ].centr_p.x += xdirection
                   sfss[ i ][ j ].angl += 1 * sfss[ i ][ j ].direction
                   sfss[ i ][ j ].centr_p.y += 3

               else: 
                   sfss[ i ][ j ].centr_p.x += 3*xdirection
                   sfss[ i ][ j ].angl += 3 * sfss[ i ][ j ].direction
                   sfss[ i ][ j ].centr_p.y += 5

               sfss[ i ][ j ].calc()
               sfss[ i ][ j ].draw( canvas ) 

         # print( " ***** len( sfss ) = ", len( sfss ) )
         for i in range( len( sfss ) ):
             j = 0
             length = len( sfss[ i ] )
             # print( "len( sfss[ i ] ) = ", length )
             while( j < length ):
                 if sfss[ i ][ j ].centr_p.y > h - shift: 
                      # print( "sfss[ i ][ j ].centr_p.y = ", sfss[ i ][ j ].centr_p.y )
                      del sfss[ i ][ j ]
                      shift += 0.5
                      length = len( sfss[ i ] )
                      continue
                 j += 1

             if len( sfss[ i ] ) == 0:
                 del sfss[ i ]
                 break
             
root.after(0, start)
root.mainloop()
