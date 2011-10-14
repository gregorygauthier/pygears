"""Simple demo primarily for verifying the development environment."""
from gears import core
from gears import draw
from math import pi

def main():
    node = draw.primitives.Rect(300, 200)
    node.x = 300
    node.theta = 1.5
    app = core.Application([])
    app.window.attach_node(node)
    app.window.resize(1024, 768)
    app.run()


if __name__ == '__main__':
    main()
