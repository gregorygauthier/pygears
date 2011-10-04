"""Simple demo primarily for verifying the development environment."""
from gears import core
from gears import draw
from math import pi

def main():
    node = draw.primitives.Rect(300, 200)
    # node = draw.primitives.Circle(500)
    node = draw.transforms.Rotation(node, pi/4)
    node = draw.transforms.Translation(node, 200, 200)
    node2 = draw.primitives.Rect(100, 200)
    app = core.Application([])
    app.window.attach_node(node)
    app.window.attach_node(node2)
    app.window.resize(1024, 768)
    app.run()


if __name__ == '__main__':
    main()
