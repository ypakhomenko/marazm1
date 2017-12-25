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
W=1500
H=1000
canvas = tkinter.Canvas(root, width=W, height=H, background='black')
canvas.pack()

def start():

     h = int( canvas['height'] )
     w = int( canvas['width'] )
     number_w = 8.0
     between_w = w/number_w

     r = 255
     g = 255
     b = 255

     x = 0
     y = 0

     sfss = []
     distance = 35
     step = distance

     xxxx = 0
     xdirection = 1    
     shift = 120
     kinds = [ 'round', 'symmetrical', 'asymmetrical', 'symmetrical', 'round' ]
 
     while True:

         
         xxxx += xdirection
         if xxxx == 18 or xxxx == -40: xdirection *= (-1)
         # if xxxx == -8 and step % 5 == 0: xdirection *= (-1) 

         if step % distance == 0:
         # if True:
             sfs = []
             while x < 2*w:
                direction = randint(0, 1)
                if direction == 0: direction = -1
                if step%5 == 0: direction *= (-1)

                start_angle = randint(-10, 10)
                l = randint(30, 40)
                x_delta = randint(-40, 40)
                y_delta = randint(-60, 0)

                kinds_nr = randint( 0, len( kinds ) -1 )
                k =  kinds[ kinds_nr ]
                s = Snowflake( Point( x+x_delta, y_delta ), get_color( r, g, b ), l, start_angle, direction, k )
                s.draw( canvas )
                sfs.append( s )
                x += between_w
                kinds_nr += 1

             sfss.insert( 0, sfs )
             # sfss.append( sfs )
             x = 0
         step += 1

         canvas.update()
         time.sleep(0.04)
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

         for i in range( len( sfss ) ):
             j = 0
             length = len( sfss[ i ] )
             while( j < length ):
                 if sfss[ i ][ j ].centr_p.y > h - shift: 
                      print( "sfss[ i ][ j ].centr_p.y = ", sfss[ i ][ j ].centr_p.y )
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
