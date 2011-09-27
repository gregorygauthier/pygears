"""PyGears rendering primitives (Rect, Circle, Triangle, etc)."""
from OpenGL import GL


class Rect(object):
    """A simple, solid color rectangle."""
    def __init__(self, x, y, width, height, color):
        """Initialize the Rect with the given coordinates, size, and color.

        :x:, :y: dimensions
        :width:, :height: size
        :color: 3-tuple representing RGB as fractions of 1

        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color

    def render(self):
        """Render the rectangle within the current OpenGL context."""
        GL.glColor(*self._color)

        GL.glLoadIdentity()
        GL.glTranslate(self._x, self._y, 0)

        GL.glBegin(GL.GL_QUADS)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(self._width, 0, 0)
        GL.glVertex3f(self._width, self._height, 0)
        GL.glVertex3f(0, self._height, 0)
        GL.glEnd()
