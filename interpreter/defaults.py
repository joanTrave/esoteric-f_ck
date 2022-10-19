from enum import Enum


class DefaultSymbols(str, Enum):
    """
    Default symbols taken by brainf*ck esoteric programming language.
    """

    INCREMENT_DATA_POINTER = ">"
    DECREMENT_DATA_POINTER = "<"
    INCREMENT_RELATIVE_BASE = "+"
    DECREMENT_RELATIVE_BASE = "-"
    OUTPUT_VALUE = "."
    INPUT_VALUE = ","
    JUMP_FORWARD = "["
    JUMP_BACKWARD = "]"
