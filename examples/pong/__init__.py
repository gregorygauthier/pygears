from gears import core
from PySide import QtCore
class StartState(object):
    def update(dt, app):
        if(app.key_map.get(QtCore.Qt.Key_Space) & 0b010) != 0:
            app.states.push(GameState())
