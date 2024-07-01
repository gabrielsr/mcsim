import typing



class RenderOptions(typing.TypedDict):
    FPS: typing.Optional[int]




class Config(typing.TypedDict):
    """Options for the Simulation config

        Arguments:
            context: str -- Change the base directory for simulation assets. Default is .
            map: str -- Name of simulation map file. Must be under assets folder. Default is 'map.drawio'
    """
    context: str
    map: typing.Optional[str]
    duration: typing.Optional[int]
    renderOptions: typing.Optional[RenderOptions]


ConfigFormat = typing.Optional[typing.Union[str, Config]]