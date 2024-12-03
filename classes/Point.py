class Point:
    # This is a point, but the truer representation of the object is a position vector. Will manipulate it as such.
    def __repr__(self):
            #return f"Point: {round(float(self.x_coord), 5)}, {round(float(self.y_coord), 5)}, {round(float(self.z_coord), 5)}"

            return f"Point: {round(float(self.x_coord), 5)}, {round(float(self.y_coord), 5)}"

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        #self.z_coord = z

    def __add__(self, other_point):
        return Point(self.x_coord + other_point.x_coord, self.y_coord + other_point.y_coord)#, self.z_coord + other_point.z_coord)

    def __sub__(self, other_point):
        return Point(self.x_coord - other_point.x_coord, self.y_coord - other_point.y_coord)#, self.z_coord - other_point.z_coord)

    def scalar_mul(self, scalar):
        #return Point(self.x_coord * scalar, self.y_coord * scalar, self.z_coord * scalar)

        return Point(self.x_coord * scalar, self.y_coord * scalar)

    def set_x(self, new_x):
        self.x_coord = new_x

    def set_y(self, new_y):
        self.y_coord = new_y

    '''
    def set_z(self, new_z):
        self.z_coord = new_z
    '''
