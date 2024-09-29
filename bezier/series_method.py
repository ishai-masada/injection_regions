import numpy
import math
import matplotlib.pyplot as plt
import sys

# Change the list of target searches
sys.path.insert(0, '/home/imasada/code/custom_curves/')

# Import the Position Vector class
from pointclass import PositionVector

# Class Object for a single Bezier Curve
class BezierCurve():


    def __init__(self, control_points, parameter):
        self.control_points = control_points
        self.parameter = parameter
        self.positions = []


    # Returns a binomial coefficient given the degree of the polynomial and the index of the term
    def binomial_coefficient(self, degree, iterator):
        return math.factorial(degree) / (math.factorial(iterator) * math.factorial(degree - iterator))


    # Returns the bernstein polynomial coefficient
    def basis_polynomial(self, parameter, degree, iterator):
        return self.binomial_coefficient(degree, iterator) * (parameter**iterator) * ((1 - parameter)**(degree - iterator))


    # Returns the coordinate of a single point on the curve
    def bezier_function(self):
        degree = len(self.control_points) - 1

        # Iterate Through Each Parameter Step
        for t in self.parameter:
            position = PositionVector(0, 0)

            # Apply the effects of each control point to the parameter
            for idx, point in enumerate(self.control_points):
                position += point.scalar_mul(self.basis_polynomial(t, degree, idx))

            self.positions.append(position)

    '''
    Places the positions onto a plot displaying anything to the user.

    The function plot.show() should only be called after all curves are placed onto the plot.
    '''
    def plot_points(self):
        for i in range(0, len(self.positions)):
            x = numpy.array([self.positions[i].x_coord])
            y = numpy.array([self.positions[i].y_coord])

            plt.plot(x, y, 'o')

        

# Read in the control points from the bladegen file
with open('data/span 0 rotor lower.txt', 'r') as f:
    lower_points = f.read().splitlines()

with open('data/span 0 rotor upper.txt', 'r') as f:
    upper_points = f.read().splitlines()

with open('data/span 0 rotor upper trailing.txt', 'r') as f:
    upper_trailing_points = f.read().splitlines()

lower_points = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_points]
upper_points = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_points]
upper_trailing_points = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_trailing_points]

# Parameter
resolution = 0.05
t = numpy.arange(0, 1 + resolution, resolution)

upper_curve = BezierCurve(upper_points, t)
upper_trailing_curve = BezierCurve(upper_trailing_points, t)
lower_curve = BezierCurve(lower_points, t)

# Produce the curve
upper_curve.bezier_function()
upper_trailing_curve.bezier_function()
lower_curve.bezier_function()

# Plot the full curves without showing the plot
upper_curve.plot_points()
upper_trailing_curve.plot_points()
lower_curve.plot_points()

#print(upper_curve.positions)

plt.show()
