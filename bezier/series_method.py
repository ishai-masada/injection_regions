import numpy
import math
import matplotlib.pyplot as plt

# Check if this makes sense
class BPoly():
    pass

class PositionVector:
    # This is a point, but the truer representation of the object is a position vector. Will manipulate it as such.
    def __repr__(self):
            return f"Point: {round(self.x_coord, 5)}, {round(self.y_coord, 5)}"

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def __add__(self, other_point):
        return PositionVector(self.x_coord + other_point.x_coord, self.y_coord + other_point.y_coord)

    def scalar_mul(self, scalar):
        return PositionVector(self.x_coord * scalar, self.y_coord * scalar)

    def change_x(self, new_x):
        self.x_coord = new_x

    def change_y(self, new_y):
        self.y_coord = new_y
        

# Returns a binomial coefficient given the degree of the polynomial and the index of the term
def binomial_coefficient(degree, iterator):
    return math.factorial(degree) / (math.factorial(iterator) * math.factorial(degree - iterator))


# Returns the bernstein polynomial coefficient
def basis_polynomial(parameter, degree, iterator):
    return binomial_coefficient(degree, iterator) * (parameter**iterator) * ((1 - parameter)**(degree - iterator))


# Returns the coordinate of a point on the curve
def bezier_function(parameter, degree, control_points):
    position = control_points[0]
    for idx, control_point in enumerate(control_points):
        position = position + control_point.scalar_mul(basis_polynomial(parameter, degree, idx))

    return position

# Store the control points in a Numpy array
control_points = numpy.asarray([PositionVector(0, 0), PositionVector(1, 2), PositionVector(2, 3)])

# Degree of 3 yields a cubic curve
degree = len(control_points) - 1

# Parameter
step_size = 0.1
t = numpy.arange(0, 1 + step_size, step_size)

for beh in t:
    point = bezier_function(beh, degree, control_points)
    x = numpy.array([point.x_coord])
    y = numpy.array([point.y_coord])
    plt.plot(x, y)

plt.show()

for beh in t:
    point = bezier_function(beh, degree, control_points)
    print(point)
