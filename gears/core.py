from PySide import QtGui, QtCore
from gears import draw
import utils

class Application(QtGui.QApplication):
    """A game application.

    Application orchestrates a Window with a QApplication.

    """
    def __init__(self, args):
        """Initialize the application."""
        super(Application, self).__init__(args)
        self.window = draw.window.Window()
        self._render_clock = utils.Clock(16, self.update)

    def run(self):
        """Start the event loop. Blocking."""
        self.window.show()
        self.exec_()

    def update(self, dt):
        """Update the application window."""
        self.window.updateGL()


class StateStack(object):
    """Implement a state stack.

    Note that _contents is a stack implemented as a
    list:  _contents[0] is the bottom element;
    _contents[-1] is the top element.

    """

    def __init__(self):
        """Initialize an empty StateStack."""
        self._contents = []

    def push(self, state):
        """Push the given state onto the stack.

        Also calls the load() method of the new element
        and the pause(state) method of the element
        that was on top prior to this method call

        """

        try:
            self.top().pause(state)
        except IndexError:
            pass
        self._contents.append(state)
        state.load()

    def pop(self):
        """Pop the topmost state onto the stack.

        Also calls the unload() method of the top element
        and the unpause() method of the element below

        """

        state = self._contents.pop()
        state.unload()
        try:
            self.top().unpause()
        except IndexError:
            pass
        return state

    def is_empty(self):
        """Return true if the stack is empty; false otherwise."""
        return len(self._contents) == 0

    def clear(self):
        """Pop every element off the stack.

        Does nothing (but does not fail) if the stack is already
        empty.

        """

        while not self.is_empty():
            self.pop()

    def top(self):
        """Return a reference to the topmost element.

        Does not affect the stack in any way or fire any
        (un)load or (un)pause events

        """

        return self._contents[-1]
    
    def render(self):
        """Render the states in the stack according to
        their scene's render() method."""
        
        for s in self._contents:
            s.scene.render()
