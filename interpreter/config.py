from typing import Set

from interpreter.defaults import DefaultSymbols
from interpreter.singleton import SingletonMeta


class InterpreterConfig(metaclass=SingletonMeta):
    def __init__(
        self,
        increment_data_pointer: str = None,
        decrement_data_pointer: str = None,
        increment_relative_base: str = None,
        decrement_relative_base: str = None,
        output_value: str = None,
        input_value: str = None,
        jump_forward: str = None,
        jump_backward: str = None,
    ):
        self.increment_data_pointer = (
            increment_data_pointer
            if increment_data_pointer
            else DefaultSymbols.INCREMENT_DATA_POINTER
        )
        self.decrement_data_pointer = (
            decrement_data_pointer
            if decrement_data_pointer
            else DefaultSymbols.DECREMENT_DATA_POINTER
        )
        self.increment_relative_base = (
            increment_relative_base
            if increment_relative_base
            else DefaultSymbols.INCREMENT_RELATIVE_BASE
        )
        self.decrement_relative_base = (
            decrement_relative_base
            if decrement_relative_base
            else DefaultSymbols.DECREMENT_RELATIVE_BASE
        )
        self.output_value = (
            output_value if output_value else DefaultSymbols.OUTPUT_VALUE
        )
        self.input_value = input_value if input_value else DefaultSymbols.INPUT_VALUE
        self.jump_forward = (
            jump_forward if jump_forward else DefaultSymbols.JUMP_FORWARD
        )
        self.jump_backward = (
            jump_backward if jump_backward else DefaultSymbols.JUMP_BACKWARD
        )

    def get_all_symbols(self) -> Set[str]:
        return {
            self.increment_data_pointer,
            self.decrement_data_pointer,
            self.increment_relative_base,
            self.decrement_relative_base,
            self.output_value,
            self.input_value,
            self.jump_forward,
            self.jump_backward,
        }
