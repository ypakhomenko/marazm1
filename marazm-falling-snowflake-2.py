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
     number = 10.0
     between_w = w/number
     between_h = h/number

     r = 255
     g = 255
     b = 255

     x = 0
     y = 0

     sfss = []

     while True:

         sfs = []
         while x < w + 10:
            direction = randint(-1, 1)
            start_angle = randint(-7, 7)
            l = randint(6, 9)
            x_delta = randint(-4, 4)
            y_delta = randint(-4, 4)
            sfs.append( Snowflake( Point( x+x_delta,y_delta ), get_color( r, g, b ), l, start_angle ))
            x += between_w
	         
         sfss.insert( 0, sfs )
         for sf in sfss: 
            # print( "Drawing line..." )
            for s in sf: 
               # print( "    Drawing a snowflake........" )
               s.draw( canvas )

         canvas.update()
         time.sleep(4)
         for sf in sfss: 
            for s in sf: 
               s.clean( canvas )

         canvas.update()

         sfss[0][0].print()
         for sf in sfss: 
            for s in sf: 
               s.centr_p.y += 50
               s.calc()

         sfss[0][0].print()

         x = 0
         if len(sfss) >= 25:
             print( len(sfss) )
             del sfss[ len(sfss)-1 ]

root.after(0, start)
root.mainloop()

