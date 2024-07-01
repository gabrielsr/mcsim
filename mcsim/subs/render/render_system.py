import esper
import pyglet

from mcsim.config.config_type import RenderOptions
from mcsim.config import getConfig


class RenderSystem:
    def __init__(self):
        self.config: RenderOptions = getConfig()
        self.window = pyglet.window.Window()
    
        self.window.set_handler('on_draw', self.on_draw)


    def on_draw(self):
        self.window.clear()
    
    def start(self):
        pass

    def process(self):
        pyglet.clock.tick()

        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_events()
            window.dispatch_event('on_draw')
            window.flip()


    def render_map(self):
        pass




class SimulationScreen:
    def __init__(self):
        pass

    