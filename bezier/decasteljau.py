import numpy

class Point:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def change_x(self, new_x):
        self.x_coord = new_x

    def change_y(self, new_y):
        self.y_coord = new_y
        
control_points = [Point(0, 0), Point(2, 2), Point(3, 5), Point(4, 7)]
