from OpenGL import GL, GLU
from PySide import QtOpenGL
from gears.draw import primitives


class Window(QtOpenGL.QGLWidget):
    """Desktop window filled with an OpenGL framebuffer."""
    def __init__(self, km, *args, **kwargs):
        """Initialize the window."""
        super(Window, self).__init__(*args, **kwargs)
        self._km = km

    def initializeGL(self):
        """Set up OpenGL state for 2D rendering."""
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glDisable(GL.GL_DEPTH_TEST)
        GL.glDisable(GL.GL_COLOR_MATERIAL)
        GL.glEnable(GL.GL_BLEND)
        GL.glEnable(GL.GL_POLYGON_SMOOTH)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        GL.glClearColor(0, 0, 0, 0)

    def paintGL(self):
        """Render the :scene_graph: to the Window."""
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glLoadIdentity()
        self._node.render()

    def resizeGL(self, width, height):
        """Resize the OpenGL viewport to reflect the given window dimensions."""
        GL.glViewport(0, 0, width, height)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluOrtho2D(0, width, 0, height)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
    
    def draw(self, node):
        self._node = node
        self.updateGL()
    
    def keyPressEvent(self, e):
        self._km.press(e.key())
    
    def keyReleaseEvent(self, e):
        self._km.release(e.key())
        

class KeyMap(object):
    def __init__(self):
        self.key_status_map = {}
        self.dirty_keys = set()

    def press(self, key):
        bits = self.key_status_map.get(key, 0)
        bits |= 0b110
        self.key_status_map[key] = bits
        self.dirty_keys.add(key)

    def release(self, key):
        bits = self.key_status_map.get(key, 0)
        bits |= 0b001
        bits &= 0b101
        self.key_status_map[key] = bits
        self.dirty_keys.add(key)

    def reset(self):
        for k in self.dirty_keys:
            key_status_map[k] &= 0b010
        self.dirty_keys.clear()

    def get(self, key):
        return self.key_status_map.get(key, 0)
