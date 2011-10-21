import time
from PySide import QtGui, QtCore
from gears import draw


class Clock(object):
    """A clock capable of notifying observers of each tick."""
    def __init__(self, interval, *observers):
        """Initialize a clock ticking at the given millisecond :interval:.

        Ticks of the clock will start approximately every :interval:
        seconds, with some uncontrollable variability.

        :interval: Integer interval in milliseconds
        :observers: Iterable of callables to call every tick

        """
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self._tick)
        self._timer.start(interval)
        self._observers = set(observers)
        self._previous_time = time.time()

    def register(self, observer):
        """Register the given :observer: to receive tick notifications."""
        self._observers.add(observer)

    def unregister(self, observer):
        """Unregister the given :observer: from tick notifications."""
        self._observers.discard(observer)

    def _tick(self):
        """Notify observers of the number of seconds since the last tick."""
        current_time = time.time()
        dt = current_time - self._previous_time
        self._previous_time = current_time
        for observer in self._observers:
            observer(dt)


class Application(QtGui.QApplication):
    """A game application.

    Application orchestrates a Window with a QApplication.

    """
    def __init__(self, args):
        """Initialize the application."""
        super(Application, self).__init__(args)
        self.window = draw.window.Window()
        self._render_clock = Clock(16, self.update)

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

        self.top().pause(state)
        self._contents.append(state)
        state.load()

    def pop(self):
        """Pop the topmost state onto the stack.

        Also calls the unload() method of the top element
        and the unpause() method of the element below

        """

        state = self._contents.pop()
        state.unload()
        self.top().unpause()
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
