#!/usr/bin/python3
#
# jip, 09.12.2017, falling into marasmus... :-)
#
import tkinter
from tkinter import Button
from tkinter import TOP, BOTTOM, LEFT

from Line import Line
from Point import Point


def quit(): root.destroy() 

root = tkinter.Tk()
root.title("... marasmus was getting stronger ...")

Button(root, text="ой фсё...", command=quit).pack( side = BOTTOM )
canvas = tkinter.Canvas(root, width=500, height=400)
canvas.pack()
c1 = '#%02x%02x%02x' % (255, 0, 0)
c2 = '#%02x%02x%02x' % (0, 255, 0)

#-----------------------------------------------------------
l1 = Line( Point(10,10), 0 )
l2 = Line( l1.p2, l1.ang+45, c1 )
l3 = Line( l2.p2, l2.ang+45, c2 )


canvas.create_line(l1.p1.x, l1.p1.y, l1.p2.x, l1.p2.y, fill=l1.color)
canvas.create_line(l2.p1.x, l2.p1.y, l2.p2.x, l2.p2.y, fill=l2.color)
canvas.create_line(l3.p1.x, l3.p1.y, l3.p2.x, l3.p2.y, fill=l3.color)

#-----------------------------------------------------------
# canvas.create_line(50, 0, 50, 400)
# canvas.create_line(20, 20, 200, 200, fill="red")
# canvas.create_line(10, 50, 300, 60, fill="red", dash=(4, 4))
# canvas.create_line(0, 50, 400, 50, fill=c, dash=(1, 4))

root.mainloop()
