#!/usr/bin/python3
#
# jip, 20.12.2017, falling into marasmus... :-)
#
import sys

import tkinter
from tkinter import Button
from tkinter import TOP, BOTTOM, LEFT
import time
from random import randint

#from Line import Line
from Point import Point
from Snowflake import Snowflake

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
w=1200
h=800
canvas = tkinter.Canvas(root, width=w, height=h, background='black')
canvas.pack()

def start():

     h = int( canvas['height'] )
     w = int( canvas['width'] )
     number_w = 14.0
     between_w = w/number_w

     r = 255
     g = 255
     b = 255

     x = 0
     y = 0

     sfss = []
     distance = 16

     xxxx = 0
     xdirection = 0.5  
     shift = 0
 
     while True:

         
         xxxx += xdirection
         if xxxx == 8 or xxxx == -18: xdirection *= (-1)
         if xxxx == -8 and distance % 3 == 0: xdirection *= (-1) 

         if distance%16 == 0:
         # if True:
             sfs = []
             while x < 2*w:
                direction = randint(-1, 1)
                start_angle = randint(-10, 10)
                l = randint(6, 9)
                x_delta = randint(-40, 40)
                y_delta = randint(-25, 25)

                s = Snowflake( Point( x+x_delta, y_delta ), get_color( r, g, b ), l, start_angle, direction )
                s.draw( canvas )
                sfs.append( s )
                x += between_w

             sfss.insert( 0, sfs )
             # sfss.append( sfs )
             x = 0
         distance += 1

         canvas.update()
         time.sleep(0.02)

         for i in range( len( sfss ) ):
             for j in range( len( sfss[ i ] ) ):
               # s.mv( canvas, 0, 1 )
               # canvas.update()
               sfss[ i ][ j ].clean( canvas )
               sfss[ i ][ j ].centr_p.x += xxxx
               if xxxx < -10: 
                   sfss[ i ][ j ].angl += 3 * sfss[ i ][ j ].direction
                   sfss[ i ][ j ].centr_p.y += 1

               else: 
                   sfss[ i ][ j ].angl += 6 * sfss[ i ][ j ].direction
                   sfss[ i ][ j ].centr_p.y += 2

               sfss[ i ][ j ].calc()
               sfss[ i ][ j ].draw( canvas ) 

         for i in range( len( sfss ) ):
             j = 0
             length = len( sfss[ i ] )
             while( j < length ):
                 # for j in range( len( sfss[ i ] ) ):
                 # print( i, j )
                 # print( "sfss[ i ][ j ].centr_p.y = ", sfss[ i ][ j ].centr_p.y )
                 if sfss[ i ][ j ].centr_p.y > h - shift: 
                      del sfss[ i ][ j ]
                      shift += 0.05
                      length = len( sfss[ i ] )
                      continue
                 j += 1

             if len( sfss[ i ] ) == 0:
                 del sfss[ i ]
                 break
             
root.after(0, start)
root.mainloop()

