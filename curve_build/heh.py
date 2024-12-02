from scipy.interpolate import CubicSpline, splev, splrep
from scipy import interpolate
import numpy
import matplotlib.pyplot as plt
import csv
import sys

# Change the list of target searches
sys.path.insert(0, '/home/imasada/code/custom_curves/')

# Import the Position Vector class
from Point import Point

def load_data(span):
    section_points = [(float(point.strip().split()[0]), float(point.strip().split()[1]), float(point.strip().split()[2])) for point in raw_data[span].splitlines()]
    span_x = int(float(raw_data[span].splitlines()[0].split()[0]))

    suction_side_points = [(float(point.strip().split()[0]), float(point.strip().split()[1]), float(point.strip().split()[2])) for point in raw_data[span].split('TE')[0].splitlines()]
    pressure_side_points = raw_data[span].split('TE')[1].splitlines()
    pressure_side_points.pop(0)
    pressure_side_points = [(float(point.strip().split()[0]), float(point.strip().split()[1]), float(point.strip().split()[2])) for point in pressure_side_points]


    return section_points, span_x, suction_side_points, pressure_side_points

def get_position(chord_position, span_position, pressure_suction_choice):
    section_parameter = chord_position

    match pressure_suction_choice:
        case 'ps':
            initial_point = CubicSpline(section_parameter, pressure_0)
            initial_point = Point(initial_point[0], initial_point[1], initial_point[2])
            final_point = CubicSpline(section_parameter, pressure_1)
            final_point = Point(initial_point[0], initial_point[1], initial_point[2])
        case 'ss':
            initial_point = CubicSpline(section_parameter, suction_0)
            initial_point = Point(initial_point[0], initial_point[1], initial_point[2])
            final_point = CubicSpline(section_parameter, suction_1)
            final_point = Point(initial_point[0], initial_point[1], initial_point[2])

    section_point = initial_point + scalar_mul(span_position, (final_point - initial_point))

    return section_point

# Read in data
with open('data/profiles.txt', 'r') as f:
    raw_data = f.read().split('\n\n')

    span_0, span_0x, suction_0, pressure_0 = load_data(0)
    #span_025, span_025x, suction_025, pressure_025 = load_data(1)
    #span_05, span_05x, suction_05, pressure_05 = load_data(2)
    #span_075, span_075x, suction_075, pressure_075 = load_data(3)
    span_1, span_1x, suction_1, pressure_01 = load_data(4)


# Inputs
span_position = 0.5
chord_position = 0.25
ps_ss = 'ps'

# Obtain Injection Location
injection_location = get_position(chord_position, span_position, ps_ss)
print(injection_location)

'''
# Parameterize the spline; Each parameter corresponds to a point (z, y)
t_s0 = numpy.linspace(0, 1, len(suction_0))
t_p0 = numpy.linspace(0, 1, len(pressure_0))

t_s025 = numpy.linspace(0, 1, len(suction_025))
t_p025 = numpy.linspace(0, 1, len(pressure_025))

t_s05 = numpy.linspace(0, 1, len(suction_05))
t_p05 = numpy.linspace(0, 1, len(pressure_05))

t_s025 = numpy.linspace(0, 1, len(suction_025))
t_p025 = numpy.linspace(0, 1, len(pressure_025))

t_s1 = numpy.linspace(0, 1, len(suction_1))
t_p1 = numpy.linspace(0, 1, len(pressure_1))

suction_0 = CubicSpline(t_s0, suction_0)
z0_s = [point[0] for point in suction_0(t_s0)]
y0_s = [point[1] for point in suction_0(t_s0)]
plt.scatter(z0_s, y0_s)

pressure_0 = CubicSpline(t_p0, pressure_0)
z0_p = [point[0] for point in pressure_0(t_p0)]
y0_p = [point[1] for point in pressure_0(t_p0)]
plt.scatter(z0_p, y0_p)
'''





'''
# Create the airfoils
#airfoil_0 = CubicSpline(parameter, span_0)
airfoil_025 = CubicSpline(parameter, span_025)
airfoil_05 = CubicSpline(parameter, span_05)
airfoil_075 = CubicSpline(parameter, span_075)
airfoil_1 = CubicSpline(parameter, span_1)

# Create the z and y-coordinates
z0 = [point[0] for point in airfoil_0(parameter)]
y0 = [point[1] for point in airfoil_0(parameter)]

z025 = [point[0] for point in airfoil_025(parameter)]
y025 = [point[1] for point in airfoil_025(parameter)]

z05 = [point[0] for point in airfoil_05(parameter)]
y05 = [point[1] for point in airfoil_05(parameter)]

z075 = [point[0] for point in airfoil_075(parameter)]
y075 = [point[1] for point in airfoil_075(parameter)]

z1 = [point[0] for point in airfoil_1(parameter)]
y1 = [point[1] for point in airfoil_1(parameter)]

# Plot the airfoils
plt.scatter(z0, y0)
plt.scatter(z025, y025)
plt.scatter(z05, y05)
plt.scatter(z075, y075)
plt.scatter(z1, y1)

'''
