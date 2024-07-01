import enum
import typing

EVENT = typing.NamedTuple('Event', [('type', str), ('payload', typing.NamedTuple)])
ERROR = typing.NamedTuple('ErrorEvent', [('type', str), ('ent', int), ('payload', typing.NamedTuple)])

class Component:
    pass


class LogLevel(enum.Enum):
    DEBUG = 10
    INFO  = 20
    SEER  = 25
    WARN  = 30
    ERROR = 40

    def __lt__(self, other):
        if isinstance(other, LogLevel):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            raise TypeError(f"'<' not supported between instances of 'LogLevel' and {type(other)}")

    def __ge__(self, other):
        if isinstance(other, LogLevel):
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other
        else:
            raise TypeError(f"'>=' not supported between instances of 'LogLevel' and {type(other)}")


class Config(typing.TypedDict):
    """Options for the Simulation config

        Arguments:
            context: str -- Change the base directory for simulation assets. Default is .
            map: str -- Name of simulation map file. Must be under assets folder. Default is 'map.drawio'
    """
    context: str
    map: typing.Optional[str]
    FPS: typing.Optional[int]
    DLW: typing.Optional[int]
    duration: typing.Optional[int]
    verbose: typing.Optional[typing.Union[LogLevel, int]]
    simulationComponents: typing.Optional[typing.Dict[str, list]]


ConfigFormat = typing.Optional[typing.Union[str, Config]]