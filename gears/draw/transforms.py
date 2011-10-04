"""Provides rendering transforms."""
from OpenGL import GL


class Translation(object):
    def __init__(self, node, x, y):
        """Initializes a Translation to translate node to (x,y).

        :node: any object with a render() method
        :x: x-axis offset
        :y: y-axis offset

        """
        self._node = node
        self._x = x
        self._y = y

    def render(self):
        """Renders the wrapped node translated to the given offset."""
        GL.glPushMatrix()
        GL.glTranslatef(self._x, self._y, 0)
        self._node.render()
        GL.glPopMatrix()
