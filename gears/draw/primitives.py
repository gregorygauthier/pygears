"""PyGears rendering primitives (Rect, Circle, Triangle, etc)."""
from OpenGL import GL


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
