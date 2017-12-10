#!/usr/bin/python3
#
# jip, 09.12.2017, falling into marasmus... :-)
#
import tkinter
from tkinter import Button
from tkinter import TOP, BOTTOM, LEFT
import time

from Line import Line
from Point import Point


def quit(): root.destroy() 
def draw_line( c, l ): c.create_line(l.p1.x, l.p1.y, l.p2.x, l.p2.y, fill=l.color, smooth=True, width=3)
def get_color( r, g, b ): 
    c = '#%02x%02x%02x' % (r, g, b)
    return c

current = 0
max = 150

r = 200
g = 0
b = 100
length = 1
flag = 0

def draw_fig( c, l, max, current, r, g, b, length, flag):

    # print( '!!!!!!!!!!!!!!!{0}, {1}, {2}'.format( r, g, b ))

    if not flag%50: c.delete("all")
    if r + current <= 255: r += current
    else: r = 0
    
    if g + current <= 255: g += current
    else: g = 0
    
    if b + current <= 255: b += current
    else: b = 0
    

    ll1 =  Line( l.p2, l.ang+45, get_color( r, g, b ), length )
    draw_line( c, ll1 )
    c.update()

    ll2 =  Line( ll1.p2, ll1.ang+45, get_color( r, g, b ), length ) 
    draw_line( c, ll2 )
    c.update()

    ll3 =  Line( ll2.p2, ll2.ang+45, get_color( r, g, b ), length )
    draw_line( c, ll3 )
    c.update()

    ll4 =  Line( ll3.p2, ll3.ang-90, get_color( r, g, b ), length )
    draw_line( c, ll4 )

    flag += 1
    current += 1
    if not flag%50: 
         length += 0.5
         ll4.ang -= 180
    if not flag%1: length += 0.2
    #length += 1
    #time.sleep(0.025)
    c.update()
    time.sleep(0.05)
    #time.sleep(0.25)
    if current < max: draw_fig( c, ll4, max, current, r, g, b, length, flag )
    # if current < max: draw_fig( c, ll1, max, current, r, g, b )

root = tkinter.Tk()
root.title("... marasmus was getting stronger ...")

Button(root, text="ой фсё...", command=quit).pack( side = BOTTOM )
w=1200
h=800
canvas = tkinter.Canvas(root, width=w, height=h)
canvas.pack()

#-----------------------------------------------------------
def start():
    
     #l1 = Line( Point(w/8,h/8), 315 )
     l1 = Line( Point(w/3,h/3), 315 )
     draw_fig( canvas, l1, max, current, r, g, b, length, flag )
# draw_line( canvas, l1 )

# draw_fig( canvas, l1, max, current, r, g, b, length, flag )
    

# l2 = Line( l1.p2, l1.ang+45, c1 )
# l3 = Line( l2.p2, l2.ang+45, c2 )

# draw_line( canvas, l1 )
# draw_line( canvas, l2 )
# draw_line( canvas, l3 )

#-----------------------------------------------------------
# canvas.create_line(50, 0, 50, 400)
# canvas.create_line(20, 20, 200, 200, fill="red")
# canvas.create_line(10, 50, 300, 60, fill="red", dash=(4, 4))
# canvas.create_line(0, 50, 400, 50, fill=c, dash=(1, 4))

root.after(0, start)
root.mainloop()
