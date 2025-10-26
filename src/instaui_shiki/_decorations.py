from typing import Union
from typing_extensions import TypedDict


class PositionTypedDict(TypedDict):
    line: int
    character: int


class DecorationTypedDict(TypedDict):
    start: Union[PositionTypedDict, int]
    end: Union[PositionTypedDict, int]
    properties: dict


def decoration(
    start: Union[PositionTypedDict, int],
    end: Union[PositionTypedDict, int],
    properties: dict,
) -> DecorationTypedDict:
    """


    Args:
        start (PositionTypedDict): _description_
        end (PositionTypedDict): _description_
        properties (dict): _description_

    Usage:
    ..
    """
    return {
        "start": start,
        "end": end,
        "properties": properties,
    }


def start(line: int, character: int) -> PositionTypedDict:
    return {"line": line, "character": character}


def end(line: int, character: int) -> PositionTypedDict:
    return {"line": line, "character": character}
