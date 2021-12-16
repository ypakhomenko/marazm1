#!/usr/bin/python3
#
# jip, 09.12.2017, falling into marasmus... :-)
# Ham ek pariwar hai
# pariwar chota nahi hai

from Point import Point
import Line

p1 = Point(3,4)
p2 = Point(13,14)
p3 = Point(30,40)

print( 'p1: {0}, {1}'.format(p1.x, p1.y))
print( 'p2: {0}, {1}'.format(p2.x, p2.y))
print( 'p3: {0}, {1}'.format(p3.x, p3.y))

l = Line.Line( p1, 45 )
print( 'p1: {0}, {1}, p2: {2}, {3}'.format( l.p1.x, l.p1.y, l.p2.x, l.p2.y ))
