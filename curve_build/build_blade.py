from scipy import interpolate 
import numpy
import matplotlib.pyplot as plt
import sys

# Change the list of target searches
sys.path.insert(0, '/home/imasada/code/custom_curves/')

# Import the Position Vector class
from Point import Point
from BezierCurve import BezierCurve


# Read in the control points from the bladegen files

# Span 0
with open('data/zero/span 0 rotor lower.txt', 'r') as f:
    lower_0 = f.read().splitlines()

with open('data/zero/span 0 rotor upper.txt', 'r') as f:
    upper_0 = f.read().splitlines()

with open('data/zero/span 0 rotor upper trailing.txt', 'r') as f:
    upper_trailing_0 = f.read().splitlines()

# Span 0.25
with open('data/quarter/span 0.25 rotor lower.txt', 'r') as f:
    lower_025 = f.read().splitlines()

with open('data/quarter/span 0.25 rotor upper.txt', 'r') as f:
    upper_025 = f.read().splitlines()

# Span 0.5
with open('data/half/span 0.5 rotor lower.txt', 'r') as f:
    lower_05 = f.read().splitlines()

with open('data/half/span 0.5 rotor upper.txt', 'r') as f:
    upper_05 = f.read().splitlines()

with open('data/half/span 0.5 rotor upper trailing.txt', 'r') as f:
    upper_trailing_05 = f.read().splitlines()

# Span 0.75
'''
with open('data/3_4th/span 0.75 rotor lower.txt', 'r') as f:
    lower_075 = f.read().splitlines()

with open('data/3_4th/span 0.75 rotor upper.txt', 'r') as f:
    upper_075 = f.read().splitlines()
'''

# Span 1.0
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
lower_0 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_0]
upper_0 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_0]
upper_trailing_0 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_trailing_0]

lower_025 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_025]
lower_x_025 = [point.x_coord for point in lower_025]
lower_y_025 = [point.y_coord for point in lower_025]

upper_025 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_025]
upper_x_025 = [point.x_coord for point in upper_025]
upper_y_025 = [point.y_coord for point in upper_025]

lower_05 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_05]
upper_05 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_05]
upper_trailing_05 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_trailing_05]

lower_1 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_1]
upper_1 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_1]
upper_trailing_1 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_trailing_1]

# Pass the data for span 0, 0.5, and 1.0 into a Bezier Curve class instance 
lower_curve_0 = BezierCurve(lower_0, t)
upper_curve_0 = BezierCurve(upper_0, t)
upper_trailing_0 = BezierCurve(upper_trailing_0, t)

lower_curve_05 = BezierCurve(lower_05, t)
upper_curve_05 = BezierCurve(upper_05, t)
upper_trailing_05 = BezierCurve(upper_trailing_05, t)

lower_curve_1 = BezierCurve(lower_1, t)
upper_curve_1 = BezierCurve(upper_1, t)
upper_trailing_1 = BezierCurve(upper_trailing_1, t)

# Pass the data for span 0.25 & 0.75 into a scipy.interpolate BSpline class instance
lower_tck_025 = interpolate.splrep(lower_x_025, lower_y_025, s=0, k=3)
upper_tck_025 = interpolate.splrep(upper_x_025, upper_y_025, s=0, k=3)

lower_x_025 = numpy.linspace(min(lower_x_025), max(lower_x_025), 100)
upper_x_025 = numpy.linspace(min(upper_x_025), max(upper_x_025), 100)
lower_curve_025 = interpolate.BSpline(*lower_tck_025)(lower_x_025)
upper_curve_025 = interpolate.BSpline(*upper_tck_025)(upper_x_025)

# Produce the curves
lower_curve_0.bezier_function()
upper_curve_0.bezier_function()
upper_trailing_0.bezier_function()

lower_curve_05.bezier_function()
upper_curve_05.bezier_function()
upper_trailing_05.bezier_function()

lower_curve_1.bezier_function()
upper_curve_1.bezier_function()
upper_trailing_1.bezier_function()

# Plot the curves
'''
lower_curve_0.plot_points()
upper_curve_0.plot_points()
upper_trailing_0.plot_points()

plt.plot(lower_x_025, lower_curve_025)
plt.plot(upper_x_025, lower_curve_025)

lower_curve_05.plot_points()
upper_curve_05.plot_points()
upper_trailing_05.plot_points()

lower_curve_1.plot_points()
upper_curve_1.plot_points()
upper_trailing_1.plot_points()

'''

plt.plot(lower_x_025, lower_curve_025)
plt.plot(upper_x_025, upper_curve_025)


plt.show()
