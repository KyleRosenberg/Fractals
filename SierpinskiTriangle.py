import random
from graphics import *

win = GraphWin("Sierpinski Triangle", 800, 400*(3**(1/2)))
win.setBackground("black")

POINT_1 = Circle(Point(win.width/2, 13), 10)
POINT_1.setFill("red")
POINT_1.draw(win)
POINT_2 = Circle(Point(13, win.height-8), 10)
POINT_2.setFill("green")
POINT_2.draw(win)
POINT_3 = Circle(Point(win.width-8, win.height-8), 10)
POINT_3.setFill("blue")
POINT_3.draw(win)

def iterate(point, n):
    for i in range(n):
        if point.y < (win.height/2+8):
            color = "red"
        elif point.x < win.width/2:
            color = "green"
        else:
            color = "blue"
        win.plot(point.x, point.y, color)
        ran = random.randint(1, 3)
        if ran==1:
            nextPoint = POINT_1
        elif ran==2:
            nextPoint = POINT_2
        else:
            nextPoint = POINT_3
        halfx = point.x + ((nextPoint.getCenter().x - point.x)/2)
        halfy = point.y + ((nextPoint.getCenter().y - point.y)/2)
        point = Point(halfx, halfy)

point = Point(13, win.width-8)
iterate(point, 100000)

win.getMouse()