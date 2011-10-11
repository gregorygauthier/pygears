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
    DEFAULT_POLYGON_SIDES = 96

    """A simple, solid color circle."""
    def __init__(self, radius, polygon_sides = DEFAULT_POLYGON_SIDES):
        """Initialize the Circle with the given radius
        
        :radius: radius
        """
        self._radius = radius
        self._polygon_sides = polygon_sides
        theta = [2 * pi * i /self._polygon_sides for i in \
            range(self._polygon_sides)]
        self._vertices = [(self._radius * cos(theta[i]),
            self._radius * sin(theta[i]), 0) for i in \
            range(self._polygon_sides)]
    
    def render(self):
        """Render the circle within the current OpenGL context."""
        GL.glBegin(GL.GL_TRIANGLE_FAN)
        GL.glVertex3f(0, 0, 0)
        for i in range(self._polygon_sides):
            GL.glVertex3f(*self._vertices[i])
        GL.glVertex3f(*self._vertices[0]) # make sure we draw the last triangle
                                          # too
        GL.glEnd()

class Triangle(object):
	"""This is a triangle with one vertex at the origin
	   and the other two vertices at specified locations"""
	
	"""Construct the triangle with the origin and the two
	given ordered pairs as the three vertices.
	:vertex1:, :vertex2: the vertices
	"""
	
	def __init__(self, vertex1, vertex2):
		self._vertex1 = (vertex1[0], vertex1[1], 0)
		self._vertex2 = (vertex2[0], vertex2[1], 0)
	
	def render(self):
		GL.glBegin(GL.GL_TRIANGLES)
		GL.glVertex3f(0, 0, 0)
		GL.glVertex3f(*self._vertex1)
		GL.glVertex3f(*self._vertex2)
		GL.glEnd()

class CompositeNode(object):

    def __init__(self, children):
        self._children = children

    def render(self):
        for x in self._children:
            x.render()
