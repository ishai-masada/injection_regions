from scipy.interpolate import CubicSpline
import numpy
import matplotlib.pyplot as plt
import csv
import sys
import math

# Change the list of target searches
sys.path.insert(0, '/home/imasada/code/custom_curves/classes')

# Import the Position Vector class
from Point import Point

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
        csvfile.write('[Name]\nR1 Blade\n\n')
        csvfile.write('[Spatial Fields]\n')
        coord_writer.writerow(['X', 'Y', 'Z'])
        csvfile.write('\n[Data]\n')
        coord_writer.writerow(['X[m]', 'Y[m]', 'Z[m]'])
        csvfile.write('\n')

        theta = 5 * math.pi/180 # assumed angle in radians

        # Write each set of coordinates as a row in the file
        for point in coordinates:
            # Offset
            offset = point[0] * math.tan(theta) # add to y-coordinates

            coord_writer.writerow([point[0], point[1] + offset, point[2]])

def load_data(span):
    # All points within airfoil section
    #section_points = [(float(point.strip().split()[0]), float(point.strip().split()[1]), float(point.strip().split()[2])) for point in raw_data[span].splitlines()]
    section_points = [(float(point.strip().split()[1]), float(point.strip().split()[2])) for point in raw_data[span].splitlines()]

    # Span Position
    span_x = int(float(raw_data[span].splitlines()[0].split()[0]))

    # Suction Side Points
    #suction_side_points = [(float(point.strip().split()[0]), float(point.strip().split()[1]), float(point.strip().split()[2])) for point in raw_data[span].split('TE')[0].splitlines()]
    pressure_side_points = [(float(point.strip().split()[1]), float(point.strip().split()[2])) for point in raw_data[span].split('TE')[0].splitlines()]

    # Pressure Side Points
    suction_side_points = raw_data[span].split('TE')[1].splitlines()
    suction_side_points.pop(0)
    suction_side_points = [(float(point.strip().split()[1]), float(point.strip().split()[2])) for point in suction_side_points]

    return section_points, span_x, suction_side_points, pressure_side_points

def get_position(chord_position, span_position, pressure_suction_choice):
    match pressure_suction_choice:
        case 'ps':
            parameter_0 = numpy.linspace(0, 1, len(pressure_0))
            span0_section = CubicSpline(parameter_0, pressure_0)
            initial_point = span0_section(chord_position)

            parameter_1 = numpy.linspace(0, 1, len(pressure_1))
            span1_section = CubicSpline(parameter_1, pressure_1)
            final_point = span1_section(chord_position)

        case 'ss':
            parameter_0 = numpy.linspace(0, 1, len(suction_0))
            span0_section = CubicSpline(parameter_0, suction_0)
            initial_point = span0_section(chord_position)

            parameter_1 = numpy.linspace(0, 1, len(suction_1))
            span1_section = CubicSpline(parameter_1, suction_1)
            final_point = span1_section(chord_position)

    desired_x = (span_0x + span_position*(span_1x - span_0x))
    initial_point = Point(desired_x, initial_point[0], initial_point[1]).scalar_mul(0.001)
    final_point = Point(desired_x, final_point[0], final_point[1]).scalar_mul(0.001)
    section_point = initial_point + (final_point - initial_point).scalar_mul(span_position)

    return section_point

# Read in data
with open('data/heh.txt', 'r') as f:
    raw_data = f.read().split('\n\n')

    section_0, span_0x, suction_0, pressure_0 = load_data(0)
    section_1, span_1x, suction_1, pressure_1 = load_data(4)

# User Input
span_position = 0.5
chord_position = 0.5
ps_ss = 'ps'

with open('data/input positions.csv', 'r') as f:
    raw_data = f.read().splitlines()
    raw_data.pop(0)

points = []

for group in raw_data:
    elements = group.split(',')

    span_position = float(elements[0])
    chord_position = float(elements[1])
    ps_ss = elements[2]

    injection_location = get_position(chord_position, span_position, ps_ss)
    points.append([injection_location.x_coord, injection_location.y_coord, injection_location.z_coord])


write_coords('Injection Locations.csv', points) 
