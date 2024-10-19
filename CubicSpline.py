import numpy
import math
from Point import Point
import matplotlib.pyplot as plt
import copy

'''
S_0(x) = ax^3 + bx^2 + cx + d
S_1(x) = ax^3 + bx^2 + cx + d
S_2(x) = ax^3 + bx^2 + cx + d
'''




'''
This class is a complete composite curve (end to end) made from a splice of individual cubic polynomials. These polynomials are generated within the SplineCurve instance given a set of nodes.
'''
class CubicSpline:
    def __init__(self, nodes):
        # Nodes is a list of Points (the class instance)
        self.nodes = nodes
        self.coefficients = []
        self.constants = [node.y_coord for node in nodes]


    def first_derivative(self, node):
        a = 3 * (node.x_coord)**2
        b = 2 * node.x_coord
        c = 1
        d = 0
        coefficients = [a, b, c, d] 

        return coefficients

    def second_derivative(self, node):
        a = 6 * node.x_coord
        b = 2
        c = 0
        d = 0
        coefficients = [a, b, c, d] 

        return coefficients

    def first_derivative_conditions(self, internal_nodes):
        coefficients = []
        constants = []

        for node in internal_nodes:
           coefficients.append(first_derivative(node) - derivative_coefficients(node))
           constant.append(node.y_coord)

        return coefficients, constants

    
    # Apply Boundary Conditions to achieve the last two equations 
    def boundary_conditions(self, external_nodes, boundary_condition):
        coefficients = []
        constants = []
        boundary_condition = "NATURAL"

        match boundary_condition:
            case "NATURAL":
                pass
            case "CLAMPED":
                pass
            case "NOT A KNOT":
                pass
            case "PERIODIC":
                pass
            case "QUADRATIC":
                pass

        return coefficients, constants

    def get_coefficients(self):
        n = len(self.nodes) - 1

        # Find the internal nodes by removing the endpoints from a copy of the instance nodes
        internal_nodes = copy.deepcopy(self.nodes)
        del internal_nodes[0], internal_nodes[-1]

        # Find the external nodes by removing the internal nodes from a copy of the instance nodes
        external_nodes = copy.deepcopy(self.nodes)
        del external_nodes[1:len(external_nodes) - 1]


    def plot_points(self):
        pass


nodes = [Point(1, 2), Point(3, 1), Point(5, 5)]

spline = CubicSpline(nodes)
spline.get_coefficients()
