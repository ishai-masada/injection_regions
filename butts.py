from matplotlib import pyplot as plt
import numpy as np

# Read in the coordinates from the text file
with open('BG_profile.curve', 'r') as f:
    raw_data = f.read().strip().splitlines()

# Coordinates
x_values = []
y_values = []
z_values = []

# Separate and Scale the Coordinates
for line in raw_data:
    # Separate the coordinates into x, y, and z coordinates
    coord_set = line.split()

    # Add each coordinate to its corresponding list and apply its scientific notation
    x_values.append(str(float(coord_set[0][:-4]) / 10**(int(coord_set[0][-1:]))))
    y_values.append(str(float(coord_set[1][:-4]) / 10**(int(coord_set[1][-1:]))))
    z_values.append(str(float(coord_set[2][:-4]) / 10**(int(coord_set[2][-1:]))))

x_values = np.array(x_values, dtype='float')
y_values = np.array(x_values, dtype='float')
z_values = np.array(x_values, dtype='float')

figure = plt.figure()
axes = figure.add_subplot(projection='3d')
axes.scatter(x_values, y_values, z_values)
plt.show()
