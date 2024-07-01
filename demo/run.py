from mcsim.core import Simulation
#from mcsim.subs.render import RenderSystem, Renderable
from mcsim.subs.position import Velocity, Position
from mcsim.subs.position import MovementProcessor

def run():

    config = {
        "context": "tests/data",
        "FPS": 60,
        "DLW": 10,
        "duration": 10
    }

    sim = Simulation(config)
    
    #sim.add_system(RenderSystem())

    sim.add_system(MovementProcessor(
        minx=0,
        maxx=800,
        miny=0,
        maxy=600
    ))

    sim.add_entity(
        label='test',
        components=[
            #Renderable(color='red'),
            Position(x=0, y=0),
            Velocity(x=1, y=0)
        ]
    )

    sim.run()



run()