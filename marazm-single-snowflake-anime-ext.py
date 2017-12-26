#!/usr/bin/python3
#
# jip, 26.12.2017, falling into marasmus... :-)
#
import tkinter
from tkinter import Button
from tkinter import TOP, BOTTOM, LEFT
import time
from random import randint

from Line import Line
from Point import Point
from SnowflakeExt import Snowflake

def quit(): root.destroy() 
def get_color( r, g, b ): 
    c = '#%02x%02x%02x' % (r, g, b)
    return c

current = 0

r = 255
g = 255
b = 255

def draw_fig( x, y, canvas, max, current, r, g, b, angle, length, delta, direction, kind_nr, width):

    w = int( canvas['width'] )
    h = int( canvas['height'] )

    start = -50
    end = 50

    kinds = [ 'round', 'symmetrical', 'asymmetrical']
    delta += direction
    if delta == start: 
        direction = 1
        width = 1
        kind_nr += 1 
        if kind_nr == 3: kind_nr = 0
        # print( "kind_nr = ", kind_nr )
       

    l = length + delta 
    range_max = 50
    if delta == end: 

        for x in range(0, range_max): 
            sf = Snowflake( Point( w/2.0,h/2.0 ), get_color( r, g, b ), l, angle, direction, kinds[ kind_nr ], width )
            width += 1
            angle += 0.3 * direction
            sf.draw( canvas )
            canvas.update()
            time.sleep(0.04)
            sf.clean( canvas )

        direction = -1
        for x in range(0, range_max): 
            sf = Snowflake( Point( w/2.0,h/2.0 ), get_color( r, g, b ), l, angle, direction, kinds[ kind_nr ], width )
            width -= 1
            angle += 0.3 * direction
            sf.draw( canvas )
            canvas.update()
            time.sleep(0.04)
            sf.clean( canvas )

        direction = -1


    sf = Snowflake( Point( w/2.0,h/2.0 ), get_color( r, g, b ), l, angle, direction, kinds[ kind_nr ], width )
    angle += 0.6 * direction
    
    sf.draw( canvas )
    canvas.update()
    time.sleep(0.04)
    # time.sleep(0.1)

    sf.clean( canvas )

    current += 1
    if current < max: draw_fig( 0, y, canvas, max, current, r, g, b, angle, length, delta, direction, kind_nr, width)


root = tkinter.Tk()
root.title("... marasmus was getting stronger ...")

Button(root, text="ой фсё...", command=quit).pack( side = BOTTOM )
w=1200
h=800
canvas = tkinter.Canvas(root, width=w, height=h, background='black')
canvas.pack()
max = int( canvas['height'] )
#-----------------------------------------------------------
def start():
    
     while True: 
         draw_fig( 0, 0, canvas, max, current, r, g, b, 0, 50, -50, 1, 0, 1)

root.after(0, start)
root.mainloop()
