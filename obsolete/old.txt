from scipy.interpolate import CubicSpline, splev, splrep
from scipy import interpolate
import numpy
import matplotlib.pyplot as plt
import sys
import csv

# Change the list of target searches
sys.path.insert(0, '/home/imasada/code/custom_curves/')

# Import the Position Vector class
from Point import Point
from BezierCurve import BezierCurve

def write_coords(filename, coordinates):
    '''
    Writes the injection locations to a CSV file
    '''

    # Erase the contents of the file
    open(filename, 'w').close()

    # Open the file to use csv module
    with open(filename, 'w', newline='\n') as csvfile:
        coord_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')

        # File Format Requirements
        csvfile.write('[Name]\nS1 Blade\n\n')
        csvfile.write('[Spatial Fields]\n')
        coord_writer.writerow(['X', 'Y', 'Z'])
        csvfile.write('\n[Data]\n')
        coord_writer.writerow(['X[m]', 'Y[m]', 'Z[m]'])
        csvfile.write('\n')

        # Write each set of coordinates as a row in the file
        for point in coordinates:
            coord_writer.writerow([point[0], point[1], point[2]])

def get_bezier_position(curve, span_x, chord_position):
    desired_y = curve.get_position(chord_position).y_coord
    #z_positions = curve.get_x_positions()
    #desired_z = chord_position * (max(z_positions) - min(z_positions)) + min(z_positions)

    return Point(span_x, desired_y)

def get_spline_position(splines, curve, span_x, chord_position):
    for spline in splines:
        if numpy.array_equal(curve, spline[1]):
            z_positions = spline[0]
            desired_z = chord_position * (max(z_positions) - min(z_positions)) + min(z_positions)
            desired_y = curve(desired_z)
            
            return Point(span_x, desired_y)


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
bezier_resolution = 0.01
t = numpy.arange(0, 1, bezier_resolution)

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

# Produce the curves
lower_curve_0.bezier_function()
upper_curve_0.bezier_function()

lower_curve_025 = CubicSpline(lower_x_025, lower_y_025)
upper_curve_025 = CubicSpline(upper_x_025, upper_y_025)

lower_curve_05.bezier_function()
upper_curve_05.bezier_function()

upper_curve_075 = CubicSpline(upper_x_075, upper_y_075)
lower_curve_075 = CubicSpline(lower_x_075, lower_y_075)

lower_curve_1.bezier_function()
upper_curve_1.bezier_function()

# Use the data for span 0.25 & 0.75 to generate x-values
spline_resolution = 100
lower_x_025 = numpy.linspace(min(lower_x_025), max(lower_x_025), spline_resolution)
upper_x_025 = numpy.linspace(min(upper_x_025), max(upper_x_025), spline_resolution)
lower_x_075 = numpy.linspace(min(lower_x_075), max(lower_x_075), spline_resolution)
upper_x_075 = numpy.linspace(min(upper_x_075), max(upper_x_075), spline_resolution)

# Plot the curves
lower_curve_0.plot_points()
upper_curve_0.plot_points()

'''
plt.plot(lower_x_025, lower_curve_025(lower_x_025))
plt.plot(upper_x_025, upper_curve_025(upper_x_025))

lower_curve_05.plot_points()
upper_curve_05.plot_points()

plt.plot(lower_x_075, lower_curve_075(lower_x_075))
plt.plot(upper_x_075, upper_curve_075(lower_x_075))
'''

lower_curve_1.plot_points()
upper_curve_1.plot_points()

plt.show()

# Build the spline along the span of the blade accoring to the span position input from the user
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
# User Inputs (3)
chord_position = 0.25
span_position = 0.5
ps_ss = 'ps'


spanwise_points = []
span_positions = numpy.arange(0, 1.25, 0.25)

# Get 
match ps_ss:
    case 'ps':
        # Assuming constant airfoil section, blade twist, or blade turning. Take the first bezier curve to find the z-position
        first_curve = pressure_side_curves[0]
        last_curve = pressure_side_curves[-1]

        first_point = get_bezier_position(first_curve, 0, chord_position)
        last_point = get_bezier_position(last_curve, 1, chord_position)

        z_positions = first_curve.get_x_positions()
        desired_z = chord_position * (max(z_positions) - min(z_positions)) + min(z_positions)

        # Slope equation
        slope = (last_point.y_coord - first_point.y_coord) / (last_point.x_coord - first_point.x_coord)

        desired_x = span_position * (last_point.x_coord - first_point.x_coord) + first_point.x_coord
        desired_y = (desired_x * slope) + first_point.y_coord

        injection_location = [[desired_x, desired_y, desired_z]]

        '''
        # Assuming constant airfoil section, blade twist, or blade turning. Take the first bezier curve to find the z-position
        z_position = get_bezier_position(spanwise_points, pressure_side_curves[0], span_positions, chord_position).x_position

        for idx, curve in enumerate(pressure_side_curves):
            if type(curve) == BezierCurve:
                spanwise_points.append(get_bezier_position(spanwise_points, curve, span_positions[idx], chord_position))

            elif type(curve) == interpolate._cubic.CubicSpline:
                spanwise_points.append(get_spline_position(spanwise_points, splines, curve, span_positions[idx], chord_position))
        '''

    case 'ss':
        for idx, curve in enumerate(suction_side_curves):
            if type(curve) == BezierCurve:
                spanwise_points.append(get_bezier_position(spanwise_points, curve, span_positions[idx], chord_position))

            elif type(curve) == interpolate._cubic.CubicSpline:
                spanwise_points.append(get_spline_position(spanwise_points, splines, curve, span_positions[idx], chord_position))


'''
blade_length = 0.2
chord_length = 0.09
hub_radius = 0.3
# sort the spanwise points by ascending x-values
spanwise_points = sorted(spanwise_points, key=lambda point: point.x_coord)
spanwise_x = [(point.x_coord * blade_length) for point in spanwise_points]
spanwise_y = [point.y_coord for point in spanwise_points]

span_spline = splrep(spanwise_x, spanwise_y)

x_values = numpy.arange(0, blade_length, 0.01)
desired_x = span_position * (max(x_values) - min(x_values)) + min(x_values)

'''
'''
span_position = numpy.interp(desired_x, spanwise_x, spanwise_y)
print(span_position)
'''
'''

desired_y = splev(desired_x, span_spline)
desired_z = suction_side_curves[0].get_position(chord_position).x_coord

#injection_locations = []
#injection_locations.append(Point(desired_x, desired_y, chord_position))
injection_locations = [[desired_x + hub_radius, desired_y, desired_z]]
'''
print(injection_location)

filename = "Injection Locations.csv"
write_coords(filename, injection_location)
