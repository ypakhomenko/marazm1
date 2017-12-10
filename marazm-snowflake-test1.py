#!/usr/bin/python3
#
# jip, 10.12.2017, falling into marasmus... :-)
#
import tkinter
from tkinter import Button
from tkinter import TOP, BOTTOM, LEFT

from Line import Line
from Point import Point
from Snowflake import Snowflake

def quit(): root.destroy() 
def draw_line( c, l ): c.create_line(l.p1.x, l.p1.y, l.p2.x, l.p2.y, fill=l.color, smooth=True, width=3)
def get_color( r, g, b ): 
    c = '#%02x%02x%02x' % (r, g, b)
    return c

current = 0
max = 8

r = 200
g = 0
b = 100
length = 3

root = tkinter.Tk()
root.title("... marasmus was getting stronger ...")

Button(root, text="ой фсё...", command=quit).pack( side = BOTTOM )
w=1000
h=500
canvas = tkinter.Canvas(root, width=w, height=h)
canvas.pack()

#-----------------------------------------------------------
sflake = Snowflake( Point( w/2, h/2 ), get_color( 100, 50, 10 ), 20 )
sflake.draw( canvas )
#-----------------------------------------------------------

root.mainloop()
