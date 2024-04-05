import csv


def write_coords(sorted_coordinates, filename):
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
        for point in sorted_coordinates:
            coord_writer.writerow([point[0], point[1], point[2]])


def cross_section(desired_point, precisions):
    desired_location = []

    # Identify the general locations for the data set
    approximate_x = str(sorted_x[int(len(sorted_x) * desired_point[0])])[0:precisions[0]]
    approximate_y = str(sorted_y[int(len(sorted_y) * desired_point[1])])[0:precisions[1]]
    approximate_z = str(sorted_z[int(len(sorted_z) * desired_point[2])])[0:precisions[2]]
    desired_location.append(tuple([approximate_x, approximate_y, approximate_z]))

    # Coordinates as points
    coordinates = list(zip(x_values, y_values, z_values))

    # Filter the coordinates by the common x-value
    sorted_coordinates = tuple([coordinate for idx, coordinate in enumerate(coordinates) if all([approximate_x in coordinate[0], approximate_y in coordinate[1], approximate_z in coordinate[2]])])

    return sorted_coordinates


# Read in the coordinates from the text file
with open('s1 blade.txt', 'r') as f:
    raw_data = f.read().strip().splitlines()

# Individual coordinates
x_values = []
y_values = []
z_values = []

# Separate and Scale the Coordinates
for line in raw_data:
    # Separate the coordinates into x, y, and z coordinates
    coord_set = line.split(',')

    # Add each coordinate to its corresponding list and apply its scientific notation
    x_values.append(str(float(coord_set[0][:-4]) / 10**(int(coord_set[0][-1:]))))
    y_values.append(str(float(coord_set[1][:-4]) / 10**(int(coord_set[1][-1:]))))
    z_values.append(str(float(coord_set[2][:-4]) / 10**(int(coord_set[2][-1:]))))

sorted_x = x_values.copy()
sorted_y = y_values.copy()
sorted_z = z_values.copy()
sorted_x.sort()
sorted_y.sort()
sorted_z.sort()

#x_location = 0.5 # Spanwise location of the blade
desired_point = [0.5, 0.5, 0.5]
precisions = [3, 5, 5] # How many digits to include from each coordinate

# Get the coordintes for a user-defined spanwise location
sorted_coordinates = cross_section(desired_point, precisions)

filename = 'test regions.csv'
write_coords(sorted_coordinates, filename)
