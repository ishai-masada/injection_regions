from scipy import interpolate 
import numpy
import matplotlib.pyplot as plt
import sys

# Change the list of target searches
sys.path.insert(0, '/home/imasada/code/custom_curves/')

from Point import Point

# Read in the control points from the bladegen files
with open('data/quarter/span 0.25 rotor lower.txt', 'r') as f:
    lower = f.read().splitlines()

with open('data/quarter/span 0.25 rotor upper.txt', 'r') as f:
    upper = f.read().splitlines()



# Convert the data points into Point class instances
lower_points = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower]
lower_x = [point.x_coord for point in lower_points]
lower_y = [point.y_coord for point in lower_points]

upper_points = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper]
upper_x = [point.x_coord for point in upper_points]
upper_y = [point.y_coord for point in upper_points]


lower_tck = interpolate.splrep(lower_x, lower_y, s=0, k=3)
upper_tck = interpolate.splrep(upper_x, upper_y, s=0, k=3)

# Plotting
lower_x_values = numpy.linspace(min(lower_x), max(lower_x), 100)
upper_x_values = numpy.linspace(min(upper_x), max(upper_x), 100)
lower_curve = interpolate.BSpline(*lower_tck)(lower_x_values)
upper_curve = interpolate.BSpline(*upper_tck)(upper_x_values)
plt.plot(lower_x_values, lower_curve)
plt.plot(upper_x_values, upper_curve)
plt.show()
