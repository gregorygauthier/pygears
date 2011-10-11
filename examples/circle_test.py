"""Simple demo primarily for verifying the development environment."""
from gears import core
from gears import draw
from math import pi

def main():
    node = draw.primitives.Circle(200)
    node2 = draw.primitives.Circle(100, 12) # a dodecagon
    node2 = draw.transforms.Translation(node2, 300, 300)
    app = core.Application([])
    app.window.attach_node(node)
    app.window.attach_node(node2)
    app.window.resize(1024, 768)
    app.run()


if __name__ == '__main__':
    main()
