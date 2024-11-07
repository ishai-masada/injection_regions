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

# Span 0.75
with open('data/3_4th/span 0.75 rotor lower.txt', 'r') as f:
    lower_075 = f.read().splitlines()

with open('data/3_4th/span 0.75 rotor upper.txt', 'r') as f:
    upper_075 = f.read().splitlines()

# Span 1.0
with open('data/end/span 1.0 rotor lower.txt', 'r') as f:
    lower_1 = f.read().splitlines()

with open('data/end/span 1.0 rotor upper.txt', 'r') as f:
    upper_1 = f.read().splitlines()


# Parameter
resolution = 0.01
t = numpy.arange(0, 1, resolution)

# Convert the data into the Position Vector type
lower_0 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_0]
upper_0 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_0]

lower_025 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_025]
lower_x_025 = [point.x_coord for point in lower_025]
lower_y_025 = [point.y_coord for point in lower_025]

upper_025 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_025]
upper_x_025 = [point.x_coord for point in upper_025]
upper_y_025 = [point.y_coord for point in upper_025]

lower_05 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_05]
upper_05 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_05]

lower_075 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_075]
lower_x_075 = [point.x_coord for point in lower_075]
lower_y_075 = [point.y_coord for point in lower_075]

upper_075 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_075]
upper_x_075 = [point.x_coord for point in upper_075]
upper_y_075 = [point.y_coord for point in upper_075]

lower_1 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in lower_1]
upper_1 = [Point(float(point.split('\t')[0]), float(point.split('\t')[1])) for point in upper_1]

# Pass the data for span 0, 0.5, and 1.0 into a Bezier Curve class instance 
lower_curve_0 = BezierCurve(lower_0, t, 'ps')
upper_curve_0 = BezierCurve(upper_0, t, 'ss')

lower_curve_05 = BezierCurve(lower_05, t, 'ps')
upper_curve_05 = BezierCurve(upper_05, t, 'ss')

lower_curve_1 = BezierCurve(lower_1, t, 'ps')
upper_curve_1 = BezierCurve(upper_1, t, 'ss')

# Pass the data for span 0.25 & 0.75 into a scipy.interpolate BSpline class instance
lower_tck_025 = interpolate.splrep(lower_x_025, lower_y_025, s=0, k=3)
upper_tck_025 = interpolate.splrep(upper_x_025, upper_y_025, s=0, k=3)

lower_x_025 = numpy.linspace(min(lower_x_025), max(lower_x_025), 100)
upper_x_025 = numpy.linspace(min(upper_x_025), max(upper_x_025), 100)

lower_tck_075 = interpolate.splrep(lower_x_075, lower_y_075, s=0, k=3)
upper_tck_075 = interpolate.splrep(upper_x_075, upper_y_075, s=0, k=3)

lower_x_075 = numpy.linspace(min(lower_x_075), max(lower_x_075), 100)
upper_x_075 = numpy.linspace(min(upper_x_075), max(upper_x_075), 100)

# Produce the curves
lower_curve_0.bezier_function()
upper_curve_0.bezier_function()

lower_curve_025 = interpolate.BSpline(*lower_tck_025)(lower_x_025)
upper_curve_025 = interpolate.BSpline(*upper_tck_025)(upper_x_025)

lower_curve_05.bezier_function()
upper_curve_05.bezier_function()

lower_curve_075 = interpolate.BSpline(*lower_tck_075)(lower_x_075)
upper_curve_075 = interpolate.BSpline(*upper_tck_075)(upper_x_075)

lower_curve_1.bezier_function()
upper_curve_1.bezier_function()

# Plot the curves
'''
lower_curve_0.plot_points()
upper_curve_0.plot_points()

plt.plot(lower_x_025, lower_curve_025)
plt.plot(upper_x_025, upper_curve_025)


lower_curve_05.plot_points()
upper_curve_05.plot_points()

plt.plot(lower_x_075, lower_curve_075)
plt.plot(upper_x_075, upper_curve_075)

lower_curve_1.plot_points()
upper_curve_1.plot_points()

plt.show()
'''

splines = [
           [lower_x_025, lower_curve_025], 
           [upper_x_025, upper_curve_025],
           [lower_x_075, lower_curve_075],
           [upper_x_075, upper_curve_075]
          ]

pressure_side_curves = [
                        lower_curve_0,
                        lower_curve_025,
                        lower_curve_05,
                        lower_curve_075,
                        lower_curve_1
                       ]

suction_side_curves = [
                       upper_curve_0, 
                       upper_curve_025, 
                       upper_curve_05, 
                       upper_curve_075,
                       upper_curve_1 
                      ]
chord_position = 0.25
ps_ss = 'ps'
spanwise_points = []

match ps_ss:
    case 'ps':
        for curve in pressure_side_curves:
            if type(curve) == BezierCurve:
                    desired_y = curve.get_position(chord_position).y_coord
                    x_positions = curve.get_x_positions()
                    desired_x = chord_position * (max(x_positions) - min(x_positions)) + min(x_positions)
                    spanwise_points.append(Point(desired_x, desired_y))
                    #plt.plot(desired_x, desired_y, marker='*')

            elif type(curve) == numpy.ndarray:
                for spline in splines:
                    if numpy.array_equal(curve, spline[1]):
                        desired_y = spline[1][int(chord_position*100)]
                        x_positions = spline[0]
                        desired_x = chord_position * (max(x_positions) - min(x_positions)) + min(x_positions)
                        spanwise_points.append(Point(desired_x, desired_y))
                        #plt.plot(chord_position, desired_y, marker='*')

    case 'ss':
        '''
        for curve in suction_side_curves:
            if type(curve) == BezierCurve:
                    desired_y = curve.get_position(chord_position).y_coord
                    spanwise_points.append(Point(chord_position, desired_y))
                    plt.plot(chord_position, desired_y, marker='*')
            elif type(curve) == numpy.ndarray:
                for spline in splines:
                    if numpy.array_equal(curve, spline[1]):
                        desired_y = spline[1][int(chord_position*100)]
                        spanwise_points.append(Point(chord_position, desired_y))
                        plt.plot(chord_position, desired_y, marker='*')
        '''
# sort the spanwise points by ascending x-values
spanwise_points = sorted(spanwise_points, key=lambda point: point.x_coord)
print(spanwise_points)

# Build a spline using the points along the span of the blade
span_x = [point.x_coord for point in spanwise_points]
span_y = [point.y_coord for point in spanwise_points]
span_spline_tck = interpolate.splrep(span_x, span_y, s=0, k=3) 

span_x = numpy.linspace(min(span_x), max(span_x), 100)
span_spline = interpolate.BSpline(*span_spline_tck)(span_x)
plt.plot(span_x, span_spline)

plt.show()
