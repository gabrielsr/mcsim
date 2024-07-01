from mcsim.simtypes import Component

class RobotRepresentation(Component):
    def __init__(self, robot_id: str):
        self.robot_id = robot_id
