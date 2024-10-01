import numpy
import math
from pointclass import PositionVector
import matplotlib.pyplot as plt

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
