"""PyGears rendering primitives (Rect, Circle, Triangle, etc)."""
from OpenGL import GL
from math import sin, cos, pi


class Rect(object):
    """A simple, solid color rectangle."""
    def __init__(self, width, height):
        """Initialize the Rect with the given width and height.

        :width:, :height: dimension
        """
        self._width = width
        self._height = height

    def render(self):
        """Render the rectangle within the current OpenGL context."""
        GL.glBegin(GL.GL_QUADS)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(self._width, 0, 0)
        GL.glVertex3f(self._width, self._height, 0)
        GL.glVertex3f(0, self._height, 0)
        GL.glEnd()


class Circle(object):
    """A simple, solid color circle."""
    # number of sides of the approximating polygon
    POLYGON_SIDES = 96

    def __init__(self, radius):
        """Initialize the Circle with the given radius"""
        self._radius = radius
        theta = [2 * pi * i /self.POLYGON_SIDES for i in \
            range(self.POLYGON_SIDES)]
        self._vertices = [(self._radius * cos(theta[i]),
            self._radius * sin(theta[i]), 0) for i in \
            range(self.POLYGON_SIDES)]

    def render(self):
        """Render the circle within the current OpenGL context."""
        GL.glBegin(GL.GL_TRIANGLE_FAN)
        GL.glVertex3f(0, 0, 0)
        for i in range(self.POLYGON_SIDES):
            GL.glVertex3f(*self._vertices[i])
        GL.glEnd()


class Triangle(object):
    """A simple, solid color triangle."""

    def __init__(self, vertex1, vertex2):
        """Initialize a triangle.

        Constructs a triangle with the origin and the two
        given ordered pairs as the three vertices.
        :vertex1:, :vertex2: the vertices

        """
        self._vertex1 = (vertex1[0], vertex1[1], 0)
        self._vertex2 = (vertex2[0], vertex2[1], 0)

    def render(self):
        GL.glBegin(GL.GL_TRIANGLES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(*self._vertex1)
        GL.glVertex3f(*self._vertex2)
        GL.glEnd()
