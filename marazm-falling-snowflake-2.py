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
     distance = 75
     LIM = 11
     
     while True:

         if distance%75 == 0:
         #if distance <= 45:
             sfs = []
             while x < w + 10:
                direction = randint(-1, 1)
                start_angle = randint(-10, 10)
                l = randint(6, 9)
                x_delta = randint(-30, 30)
                y_delta = randint(-15, 15)

                s = Snowflake( Point( x+x_delta, y_delta ), get_color( r, g, b ), l, start_angle, direction )
                s.draw( canvas )
                sfs.append( s )
                x += between_w

             sfss.insert( 0, sfs )
             # sfss.append( sfs )
             x = 0
         distance += 1
         #l += l

         canvas.update()
         time.sleep(0.0001)

         for sf in sfss: 
            for s in sf: 
               s.mv( canvas, 0, 1 )
               # canvas.update()

         # print( "len(sfss): ", len(sfss) )
         if( distance%1500) == 0: LIM -= 1

         if len(sfss) >= LIM: del sfss[ len(sfss)-1 ]

root.after(0, start)
root.mainloop()

