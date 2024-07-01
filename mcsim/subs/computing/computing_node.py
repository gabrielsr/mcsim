from esper import Processor
from mcsim.simtypes import Component

class ComputingNode(Component):
    def __init__(self, controller):
        self.controller = controller


class ComputingSystem(Processor):
    def __init__(self):
        pass

    def process(self):
        pass


