import csv

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
    x_value = str(float(coord_set[0][:-4]) / 10**(int(coord_set[0][-1:])))
    y_value = str(float(coord_set[1][:-4]) / 10**(int(coord_set[1][-1:])))
    z_value = str(float(coord_set[2][:-4]) / 10**(int(coord_set[2][-1:])))
    
    x_values.append(x_value)
    y_values.append(x_value)
    z_values.append(x_value)
    
# Coordinates as points
unsorted_coordinates = tuple(zip(x_values, y_values, z_values))


tip = max(x_value)
root = min(x_value)
sorted_x = x_values.sort()

# Identify the coordinates around this general location 
approximate_x = '0.598'

# Filter the coordinates by the general location
push_coordinates = [coordinate for coordinate in unsorted_coordinates if coordinate[0].find(approximate_x) != -1]

'''
Write the injection locations to a file

NOTE: Code works. Don't change it.
'''

filename = 'test regions.csv'

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
    for point in push_coordinates:
        coord_writer.writerow([point[0], point[1], point[2]])
