"""Simple demo primarily for verifying the development environment."""
from gears import core
from gears import draw
from math import pi

node = draw.primitives.Rect(300, 200, theta=1.5)

def update(dt):
    global node
    node.x = (node.x + 50 * dt) % 1024
    node.y = (node.y + 70 * dt) % 768


def main():
    global node
    app = core.Application([])
    clock = core.Clock(32)
    clock.register(update)
    app.window.attach_node(node)
    app.window.resize(1024, 768)
    app.run()


if __name__ == '__main__':
    main()
