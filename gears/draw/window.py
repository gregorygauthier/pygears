from OpenGL import GL, GLU
from PySide import QtOpenGL
from gears.draw import primitives


class Window(QtOpenGL.QGLWidget):
    """Desktop window filled with an OpenGL framebuffer."""
    def __init__(self, *args, **kwargs):
        """Initialize the window."""
        super(Window, self).__init__(*args, **kwargs)
        self._scene = primitives.CompositeNode()

    def attach_node(self, node):
        """Add the given node to the nodes to render every frame."""
        self._scene.append(node)

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
        self._scene.render()

    def resizeGL(self, width, height):
        """Resize the OpenGL viewport to reflect the given window dimensions."""
        GL.glViewport(0, 0, width, height)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluOrtho2D(0, width, 0, height)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
