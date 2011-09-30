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
    """This constant determines how many sides the circle's approximating
    polygon will have when it is rendered"""
    POLYGON_SIDES = 96

    """A simple, solid color circle."""
    def __init__(self, radius):
        """Initialize the Rect with the given width and height.
        
        :radius: radius
        """
        self._radius = radius
    
    def render(self):
        """Render the circle within the current OpenGL context."""
        GL.glBegin(GL.GL_TRIANGLE_FAN)
        GL.glVertex3f(0, 0, 0)
        for i in range(self.POLYGON_SIDES):
            theta = 2 * pi * i / self.POLYGON_SIDES
            GL.glVertex3f(self._radius * cos(theta),
                self._radius * sin(theta), 0)
        GL.glEnd()
