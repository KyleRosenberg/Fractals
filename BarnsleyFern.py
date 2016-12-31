import random
from graphics import *

win = GraphWin("Barnsley Fern", 500, 500)
win.setBackground("black")

class BarnsleyFern(object):
    def __init__(self):
        self.x, self.y = 0, 0

    def transform(self, x, y):
        rand = random.uniform(0, 100)
        if rand < 1:
            return 0, 0.16 * y
        elif 1 <= rand < 86:
            return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif 86 <= rand < 93:
            return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

    def iterate(self, iterations):
        print("Iterating")
        for _ in range(iterations):
            win.plot(win.width/2 + self.x*50, (win.height - self.y*50), "green")
            self.x, self.y = self.transform(self.x, self.y)
        print("Done")


fern = BarnsleyFern()
fern.iterate(1000000)
