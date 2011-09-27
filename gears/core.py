from PySide import QtGui, QtCore
from gears import draw


class Application(QtGui.QApplication):
    """A game application.

    Application orchestrates a Window with a QApplication.

    """
    def __init__(self, args):
        """Initialize the application."""
        super(Application, self).__init__(args)
        self.window = draw.window.Window()

    def run(self):
        """Start the event loop. Blocking."""
        self.timer = QtCore.QTimer(self)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update)
        self.timer.start(16)
        self.window.show()
        self.exec_()

    def update(self):
        """Update the application window."""
        self.window.updateGL()
