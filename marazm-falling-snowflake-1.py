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

r = 255
g = 255
b = 255

def draw_fig( x, y, canvas, max, current, r, g, b, angle):

    w = int( canvas['width'] )
    h = int( canvas['height'] )
    number = 10.0
    between = w/number
    sfs = []

    while x < w + 10:

        '''
        l = 20
        x_delta = 0
        y_delta = 0
        direction = randint(-1, 1)
        start_angle = randint(-7, 7)
        ''' 
        direction = randint(-1, 1)
        start_angle = randint(-7, 7)
        l = randint(6, 9)
        x_delta = randint(-5, 5)
        y_delta = randint(-5, 5)

        sfs.append( Snowflake( Point( x+x_delta,y+y_delta ), get_color( r, g, b ), l, start_angle + angle ))
        x += between
        angle += 0.3 * direction
    
    for sf in sfs: sf.draw( canvas )
    canvas.update()
    time.sleep(0.001)

    for sf in sfs: sf.clean( canvas )

    current += 1
    y += 1
    if current < max: draw_fig( 0, y, canvas, max, current, r, g, b, angle)


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
         draw_fig( 0, 0, canvas, max, current, r, g, b, 0)

root.after(0, start)
root.mainloop()
