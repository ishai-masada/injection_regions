from scipy.interpolate import CubicSpline
import numpy
import matplotlib.pyplot as plt
from Point import Point

# Read in the control points from the bladegen files
with open('span 0.25 rotor lower.txt', 'r') as f:
    lower = f.read().splitlines()

with open('span 0.25 rotor upper.txt', 'r') as f:
    upper = f.read().splitlines()



# Convert the data points into Point class instances
lower_points = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower]
lower_x = [point.x_coord for point in lower_points]
lower_y = [point.y_coord for point in lower_points]

upper_points = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper]
upper_x = [point.x_coord for point in upper_points]
upper_y = [point.y_coord for point in upper_points]


lower_cubic = CubicSpline(lower_x, lower_y)
upper_cubic = CubicSpline(upper_x, upper_y)

# Plotting
sample_x_values = numpy.arange(0, 10)
plt.plot(sample_x_values, lower_cubic(sample_x_values))
plt.plot(sample_x_values, upper_cubic(sample_x_values))
plt.show()
