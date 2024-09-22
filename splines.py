import numpy
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def change_x(self, new_x):
        self.x_coord = new_x

    def change_y(self, new_y):
        self.y_coord = new_y
        
control_points = [Point(0, 0), Point(2, 2), Point(3, 5), Point(4, 7)]
polynomial_order = 3
dependent_matrix = numpy.zeros((len(control_points), 1))
coefficient_matrix = numpy.zeros((polynomial_order + 1, polynomial_order + 1))

for idx, value in enumerate(dependent_matrix):
    dependent_matrix[idx] = control_points[idx].y_coord

for i, point in enumerate(control_points):
    polynomial_order = 3
    row = coefficient_matrix[i]
    for col_idx, value in enumerate(row):
        row[col_idx] = point.x_coord**polynomial_order
        polynomial_order -= 1

variable_matrix = numpy.linalg.solve(coefficient_matrix, dependent_matrix)
print(variable_matrix)
