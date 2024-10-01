import numpy
import matplotlib.pyplot as plt
import sys

# Change the list of target searches
sys.path.insert(0, '/home/imasada/code/custom_curves/')

# Import the Position Vector class
from pointclass import PositionVector
from BezierCurve import BezierCurve


# Read in the control points from the bladegen files
with open('data/zero/span 0 rotor lower.txt', 'r') as f:
    lower_0 = f.read().splitlines()

with open('data/zero/span 0 rotor upper.txt', 'r') as f:
    upper_0 = f.read().splitlines()

with open('data/zero/span 0 rotor upper trailing.txt', 'r') as f:
    upper_trailing_0 = f.read().splitlines()

with open('data/half/span 0.5 rotor lower.txt', 'r') as f:
    lower_05 = f.read().splitlines()

with open('data/half/span 0.5 rotor upper.txt', 'r') as f:
    upper_05 = f.read().splitlines()

with open('data/half/span 0.5 rotor upper trailing.txt', 'r') as f:
    upper_trailing_05 = f.read().splitlines()

with open('data/end/span 1.0 rotor lower.txt', 'r') as f:
    lower_1 = f.read().splitlines()

with open('data/end/span 1.0 rotor upper.txt', 'r') as f:
    upper_1 = f.read().splitlines()

with open('data/end/span 1.0 rotor upper trailing.txt', 'r') as f:
    upper_trailing_1 = f.read().splitlines()

# Parameter
resolution = 0.05
t = numpy.arange(0, 1 + resolution, resolution)

# Convert the data into the Position Vector type
lower_0 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_0]
upper_0 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_0]
upper_trailing_0 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_trailing_0]

lower_05 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_05]
upper_05 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_05]
upper_trailing_05 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_trailing_05]

lower_1 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_1]
upper_1 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_1]
upper_trailing_1 = [PositionVector(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_trailing_1]

# Pass the data into a Bezier Curve class instance 
lower_curve_0 = BezierCurve(lower_0, t)
upper_curve_0 = BezierCurve(upper_0, t)
upper_trailing_0 = BezierCurve(upper_trailing_0, t)

lower_curve_05 = BezierCurve(lower_05, t)
upper_curve_05 = BezierCurve(upper_05, t)
upper_trailing_05 = BezierCurve(upper_trailing_05, t)

lower_curve_1 = BezierCurve(lower_1, t)
upper_curve_1 = BezierCurve(upper_1, t)
upper_trailing_1 = BezierCurve(upper_trailing_1, t)

# Produce the curve
lower_curve_0.bezier_function()
upper_curve_0.bezier_function()
upper_trailing_0.bezier_function()

lower_curve_05.bezier_function()
upper_curve_05.bezier_function()
upper_trailing_05.bezier_function()

lower_curve_1.bezier_function()
upper_curve_1.bezier_function()
upper_trailing_1.bezier_function()

# Plot the full curves without showing the plot
'''
lower_curve_05.plot_points()
upper_curve_05.plot_points()
upper_trailing_05.plot_points()

lower_curve_1.plot_points()
upper_curve_1.plot_points()
upper_trailing_1.plot_points()
'''

lower_curve_0.plot_points()
upper_curve_0.plot_points()
upper_trailing_0.plot_points()


plt.show()
