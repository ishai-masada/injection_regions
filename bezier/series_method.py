import numpy
import math
import matplotlib.pyplot as plt


# Check if this makes sense
class Bezier_Curve():
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
def bezier_function(parameter, control_points):
    position = control_points[0]

    # Degree of 3 yields a cubic curve
    degree = len(control_points) - 1

    for idx, control_point in enumerate(control_points):
        position = position + control_point.scalar_mul(basis_polynomial(parameter, degree, idx))

    return position

# Read in the control points from the bladegen file
with open('span 0 rotor lower.txt', 'r') as f:
    lower_points = f.read().splitlines()

with open('span 0 rotor upper.txt', 'r') as f:
    upper_points = f.read().splitlines()

lower_points = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])).scalar_mul(-1)  for point in lower_points]
upper_points = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])).scalar_mul(-1)  for point in upper_points]

# Parameter
step_size = 0.1
t = numpy.arange(0, 1 + step_size, step_size)

for beh in t:
    upper = bezier_function(beh, upper_points)
    lower = bezier_function(beh, lower_points)
    x = numpy.array([upper.x_coord, lower.x_coord])
    y = numpy.array([upper.y_coord, lower.y_coord])
    plt.plot(x, y, 'o')

plt.show()
