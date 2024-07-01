import logging
import simpy
import typing
import esper
from typing import List
from datetime import datetime

from mcsim.log import getLogger

from .component_types import ConfigFormat
logger = getLogger(__name__)

from .component_types import Component

def empty_config():
    return { "context": "."}

CleanupFunction = typing.Optional[typing.Callable[[], None]]

class Clock:
    def __init__(self, dt=1/120):
        self.time = 0
        self.dt = dt
    
    def tick(self, env: simpy.Environment):
        while True:
            self.time += self.dt
            yield env.timeout(self.dt)


def example(env):
    event = simpy.events.Timeout(env, delay=1, value=42)
    value = yield event
    print('now=%d, value=%d' % (env.now, value))

class Simulation:
    def __init__(self, config: ConfigFormat = empty_config()):
        self.entity_labels = dict()
        self.config = config
        self.DURATION = config.get('duration', -1)
        self.cleanups: typing.List[CleanupFunction] = []
        self.dt = 1/60
        #self.world = esper.World()
        


    def create_entity(components: List[Component]):
        esper.create_entity(components)
        
    def add_system(self, system: esper.Processor):
        """
        Adds an esper system to the simulation environment.
        These events inherit from esper.Processor and are executed at every simulation step.
        An argument kwargs: SystemArgs will be passed to these processors.
        """
        esper.add_processor(system)
    

    def add_entity(self, components: List[Component], label: str=None):
        """
        Adds an entity to the simulation environment.
        An entity is a collection of components.
        """
        id = esper.create_entity(*components)
        if label:
            self.entity_labels[label] = id

    def my_callback(event):
        print('Called back from', event)

    def esper_processor(self, env: simpy.Environment) -> typing.Generator:
        last_time = 0
        while True:
            dt = env.now - last_time
            esper.process(env)
            yield env.timeout(self.dt)
            last_time = env.now

    def process_systems(self, env: simpy.Environment):
        esper.process()
        yield self.dt

    def loop(self):
        
        env = simpy.Environment()
        clock = Clock()
        env.process(clock.tick(env))
        env.process(self.esper_processor(env))

        try:
            env.run(until=100)
        except Exception as e:
            print(e)
        finally:
            print('Done')
    

    def run(self):
        """
        Run the simulation.
        """
        logger.info(f'Starting simulation')
        try:
            self.loop()
        except Exception as e:
            logger.error(f'Error in simulation: {e}')
            self.gracious_exit()
            raise e
        finally:
            self.gracious_exit()
            logger.info(f'Simulation ended')


    def gracious_exit(self):
        logger.info(f'Exiting gracefully')
        while self.cleanups:
            next_function = self.cleanups.pop()
            logger.info(f'Executing clean-up function {next_function}')
            next_function()