from PySide import QtGui, QtCore
from gears import draw
import utils

class Application(QtGui.QApplication):
    """A game application.

    Application orchestrates a Window with a QApplication.

    """
    
    
    def __init__(self, initial_state, args):
        """Initialize the application."""
        super(Application, self).__init__(args)
        self.states = StateStack()
        self.states.push(initial_state)
        self._km = draw.window.KeyMap()
        self.window = draw.window.Window(self._km)
        self._render_clock = utils.Clock(16, self.update)

    def run(self):
        """Start the event loop. Blocking."""
        self.window.show()
        self.exec_()

    def update(self, dt):
        """Update the application window."""
        self.window.draw(self.states)
        if self.states.is_empty():
            self.quit()
        else:
            self.states.top().update(dt, self)
        self._km.reset()

    def isPressed(self, key):
        if self._km.get(key) & 0b100 == 0:
            return False
        return True
    
    def isHeld(self, key):
        if self._km.get(key) & 0b010 == 0:
            return False
        return True
    
    def isReleased(self, key):
        if self._km.get(key) & 0b001 == 0:
            return False
        return True

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
            t = self.top()
            t.pause(state)
        except IndexError:
            t = None
            pass
        self._contents.append(state)
        state.load(t)

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
            s.render()

"""Generic State class.
This passes whenever its six methods are called; subclasses
should override the methods they need to do.
"""
class State(object):
    """Pause this state on account of otherstate
    being popped over this state in the stack."""
    def pause(self, otherstate):
        pass
    
    """Unpause this state due to this state becoming
    the topmost state of the stack."""
    def unpause(self):
        pass
    
    """Load this state: called when it is pushed onto the stack.
    otherstate is the state that was on top just before this state was
    pushed."""
    def load(self, otherstate):
        pass
    
    """Unload this state: called when it is popped off the stack."""
    def unload(self):
        pass
    
    """Render this state."""
    def render(self):
        pass
    
    """Update this state.  dt is an amount of time that has passed
    since the last update call (in seconds); app is a reference
    to the current application."""
    def update(self, dt, app):
        pass
