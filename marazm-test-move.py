#!/usr/bin/python3
#
# jip, 22.12.2017, falling into marasmus... :-)
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
     number_w = 8.0
     number_h = 10.0
     between_w = w/number_w
     between_h = h/number_h

     r = 255
     g = 255
     b = 255

     x = 0
     y = 0

     sfs = []
     sfss = []
     distance = 40
     
     s = Snowflake( Point( 10, 10 ), get_color( r, g, b ), 10, 0 )
     s.draw( canvas )

     while True:


         canvas.update()
         time.sleep(0.001)

         s.mv( canvas, 0, 0.1 )

root.after(0, start)
root.mainloop()

