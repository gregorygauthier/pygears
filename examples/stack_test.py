"""Simple demo primarily for verifying the development environment."""
from gears import core
from gears import draw


def main():
    node = draw.primitives.Rect(32, 32, 960, 704, (0, 0.3, 0.8))
    app = core.Application([])
    app.window.attach_node(node)
    app.window.resize(1024, 768)
    app.run()


if __name__ == '__main__':
    main()
