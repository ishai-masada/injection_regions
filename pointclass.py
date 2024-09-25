class PositionVector:
    # This is a point, but the truer representation of the object is a position vector. Will manipulate it as such.
    def __repr__(self):
            return f"Point: {round(self.x_coord, 5)}, {round(self.y_coord, 5)}"

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def __add__(self, other_point):
        return PositionVector(self.x_coord + other_point.x_coord, self.y_coord + other_point.y_coord)

    def scalar_mul(self, scalar):
        return PositionVector(self.x_coord * scalar, self.y_coord * scalar)

    def change_x(self, new_x):
        self.x_coord = new_x

    def change_y(self, new_y):
        self.y_coord = new_y
