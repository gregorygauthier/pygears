"""Simple demo primarily for verifying the development environment."""
from gears import core
from gears import draw


def main():
    # node = draw.primitives.Rect(960, 740)
    node = draw.primitives.Circle(500)
    app = core.Application([])
    app.window.attach_node(node)
    app.window.resize(1024, 768)
    app.run()


if __name__ == '__main__':
    main()
