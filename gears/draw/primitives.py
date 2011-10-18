"""PyGears rendering primitives (Rect, Circle, Triangle, etc)."""
from OpenGL import GL
from math import sin, cos, pi


class Node(object):
    def __init__(self, x=0, y=0, theta=0.0, scale=1.0, color=(1,1,1)):
        self.x = x
        self.y = y
        self.theta = theta
        self.scale = scale
        self.color = color

    def pre_render(self):
        GL.glPushMatrix()
        GL.glPushAttrib(GL.GL_CURRENT_BIT)
        GL.glTranslatef(self.x, self.y, 0)
        GL.glRotatef(self.theta*180/pi, 0, 0, 1)
        GL.glScalef(self.scale, self.scale, 1.0)
        GL.glColor3f(*self.color)

    def plot(self):
        pass

    def post_render(self):
        GL.glPopAttrib()
        GL.glPopMatrix()

    def render(self):
        self.pre_render()
        self.plot()
        self.post_render()


class Rect(Node):
    """A simple, solid color rectangle."""
    def __init__(self, width, height, **kwargs):
        """Initialize the Rect with the given width and height.

        :width:, :height: dimension
        """
        super(Rect, self).__init__(**kwargs)
        self._width = width
        self._height = height

    def plot(self):
        """Render the rectangle within the current OpenGL context."""
        GL.glBegin(GL.GL_QUADS)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(self._width, 0, 0)
        GL.glVertex3f(self._width, self._height, 0)
        GL.glVertex3f(0, self._height, 0)
        GL.glEnd()


class Circle(Node):
    """A simple, solid color circle."""
    # number of sides of the approximating polygon
    DEFAULT_POLYGON_SIDES = 96

    """A simple, solid color circle."""
    def __init__(self, radius, polygon_sides = DEFAULT_POLYGON_SIDES,
        **kwargs):
        """Initialize the Circle with the given radius."""
        super(Circle, self).__init__(**kwargs)
        self._radius = radius
        self._polygon_sides = polygon_sides
        phi = [2 * pi * i /self._polygon_sides for i in \
            range(self._polygon_sides)]
        self._vertices = [(self._radius * cos(phi[i]),
            self._radius * sin(phi[i]), 0) for i in \
            range(self._polygon_sides)]
    

    def plot(self):
        """Render the circle within the current OpenGL context."""
        GL.glBegin(GL.GL_TRIANGLE_FAN)
        GL.glVertex3f(0, 0, 0)
        for i in range(self._polygon_sides):
            GL.glVertex3f(*self._vertices[i])
        # make sure we draw the last triangle too
        GL.glVertex3f(*self._vertices[0])
        GL.glEnd()


class Triangle(Node):
    """A simple, solid color triangle."""

    def __init__(self, vertex1, vertex2, **kwargs):
        """Initialize the triangle.

        Constructs a triangle with the origin and the two
        given ordered pairs as the three vertices.
        :vertex1:, :vertex2: the vertices

        """
        super(Triangle, self).__init__(**kwargs)
        self._vertex1 = (vertex1[0], vertex1[1], 0)
        self._vertex2 = (vertex2[0], vertex2[1], 0)
        

    def plot(self):
        GL.glBegin(GL.GL_TRIANGLES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(*self._vertex1)
        GL.glVertex3f(*self._vertex2)
        GL.glEnd()


class CompositeNode(Node):
    def __init__(self, *children, **kwargs):
        super(CompositeNode, self).__init__(**kwargs)
        self._children = list(children)

    def append(self, *nodes):
        """Attach the given nodes to the top of the composite."""
        self._children.extend(list(nodes))

    def render(self):
        """Render each subtree of the composite."""
        for x in self._children:
            x.render()
