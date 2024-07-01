from typing import List
from robot.robot_representation import RobotRepresentation
from simulator.components import Battery
from mcsim.core import Simulation

from subs.computing import network

from mcsim.simtypes import Component

from subs.computing.computing_node import ComputingNode

class Skills:
    MOVABLE = ()
    CARRY = "carry"

class RobotBuilder:
    def __init__(self, simulation: Simulation):
        self.simulation = simulation
        self.network = network()


    def movable_skill():
        pass



    def create_base_robot(self, robot_id: str, 
            skill_components: List[Component] = [],
            controller = None):
        # skills

        # battery
        return self.simulation.create_entity(robot_id,
            RobotRepresentation(
                robot_id=robot_id
            ),
            self.network.create_interface(),
            Battery(
                capacity=100, charge=100, discharge_rate=1
            ),
            ComputingNode(
                controller=controller,
            ),
            self.network.create_interface(),
            *skill_components
        )

    def create_node(self, node_id: str):

        # add actor in the world
        world.add_component(Robots.robot_A, node_a)


        # create channels of communication betwen the node and the systems in the world
        node_a.bind(mb_interface)

        
        nodes = nodes_builder.build_nodes(network)
        robot_a = create_node(network)
        ensemble_system = create_ensemble_system(network)