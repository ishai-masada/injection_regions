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
