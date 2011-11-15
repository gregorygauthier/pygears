"""Simple demo primarily for verifying the development environment."""
from PySide import QtCore
from gears import core
from gears import draw
from gears import utils
from math import pi

class AnimateState(core.State):
    VELOCITY = 30
    def __init__(self):
        self.node = draw.primitives.Circle(200, x=200, y=300)    
    
    def render(self):
        self.node.render()
    
    def update(self, dt, app):
        if app.isPressed(QtCore.Qt.Key_Q):
            app.states.pop()
        self.node.x += self.VELOCITY * dt
        self.node.x %= 1024
        self.node.y += self.VELOCITY * dt
        self.node.y %= 768

def main():
    app = core.Application(AnimateState(), [])
    app.window.resize(1024, 768)
    app.run()


if __name__ == '__main__':
    main()
