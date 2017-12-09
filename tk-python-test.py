#!/usr/bin/python3
#
# jip, 09.12.2017, falling into marasmus... :-)
#
import tkinter
from tkinter import Button
from tkinter import TOP, BOTTOM, LEFT


def quit(): root.destroy() 

root = tkinter.Tk()
root.title("... marasmus was getting stronger ...")

Button(root, text="ой фсё...", command=quit).pack( side = BOTTOM )
canvas = tkinter.Canvas(root, width=500, height=400)
canvas.pack()

canvas.create_line(50, 0, 50, 400)

c = '#%02x%02x%02x' % (255, 0, 0)
canvas.create_line(20, 20, 200, 200, fill="red")
canvas.create_line(10, 50, 300, 60, fill="red", dash=(4, 4))
canvas.create_line(0, 50, 400, 50, fill=c, dash=(1, 4))

root.mainloop()

