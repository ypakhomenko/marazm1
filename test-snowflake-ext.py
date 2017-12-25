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
from Petal import Petal

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


s = Snowflake( Point( w/4, h/4 ), get_color( 255,255,255 ), 50, 0, 1, 'round' )
s.draw( canvas )
s = Snowflake( Point( w/2, h/2 ), get_color( 255,255,255 ), 50, 0, 1, 'symmetrical' )
s.draw( canvas )
s = Snowflake( Point( w/2+w/4, h/2+h/4 ), get_color( 255,255,255 ), 50, 0, 1, 'asymmetrical' )
s.draw( canvas )
'''
pet = Petal( Point( w/2, h/2 ), 0, get_color( 255,255,255 ), 100 )
lines = pet.get_lines()
for l in lines:
    canvas.create_line(l.p1.x, l.p1.y, l.p2.x, l.p2.y, fill=l.color, smooth=True, width=1)

'''
canvas.update()

root.mainloop()

