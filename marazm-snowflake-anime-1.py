#!/usr/bin/python3
#
# jip, 10.12.2017, falling into marasmus... :-)
#
import tkinter
from tkinter import Button
from tkinter import TOP, BOTTOM, LEFT
import time
from random import randint

from Line import Line
from Point import Point
from Snowflake import Snowflake

def quit(): root.destroy() 
def get_color( r, g, b ): 
    c = '#%02x%02x%02x' % (r, g, b)
    return c

current = 0
max = 150

r = 255
g = 255
b = 255

def draw_fig( x, y, canvas, max, current, r, g, b):

    w = int( canvas['width'] )
    h = int( canvas['height'] )
    number = 10.0
    between = w/number
    sfs = []

    while x < w + 10:

        l = randint(15, 20)
        sfs.append( Snowflake( Point( x,y ), get_color( r, g, b ), l ) )
        x += between
    
    for j in range(0, h):

       for sf in sfs:
          sf.draw( canvas )
          canvas.update()

       time.sleep(0.005)

       for sf in sfs:
          sf.clean( canvas )
          sf.centr_p.y += 1
          sf.calculate( sf.centr_p, get_color( r, g, b ), l )

    current += 1
    #y += 1
    if current < max: draw_fig( 0,y, canvas, max, current, r, g, b)


root = tkinter.Tk()
root.title("... marasmus was getting stronger ...")

Button(root, text="ой фсё...", command=quit).pack( side = BOTTOM )
w=1200
h=800
canvas = tkinter.Canvas(root, width=w, height=h, background='black')
canvas.pack()

#-----------------------------------------------------------
def start():
    
     draw_fig( 0, 0, canvas, max, current, r, g, b)

root.after(0, start)
root.mainloop()
