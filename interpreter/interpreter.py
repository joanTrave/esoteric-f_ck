from typing import List, Dict, Callable

from interpreter.config import InterpreterConfig
from interpreter.interpreter_debugger import InterpreterDebugger


class Interpreter:
    def __init__(self):
        self.array: List[int] = [0]
        self.pointer = 0
        self.code_array: str = ""
        self.instruction_pointer = 0
        self.instruction_functions: Dict[str, Callable] = {
            InterpreterConfig().increment_data_pointer: self.interpret_increment_data_pointer,
            InterpreterConfig().decrement_data_pointer: self.interpret_decrement_data_pointer,
            InterpreterConfig().increment_relative_base: self.interpret_increment_value,
            InterpreterConfig().decrement_relative_base: self.interpret_decrement_value,
            InterpreterConfig().output_value: self.interpret_output_value,
            InterpreterConfig().input_value: self.interpret_input_value,
            InterpreterConfig().jump_forward: self.interpret_jump_forward,
            InterpreterConfig().jump_backward: self.interpret_jump_backward,
        }
        self.instruction = ""
        self.debugger: InterpreterDebugger = InterpreterDebugger(self)
        self.brackets_links: Dict[int, int] = {}

    def _preprocess_code_array(self):
        """
        Convert code string to array of ints
        """
        self._clear_comments()
        self._generate_brackets_links()

    def _generate_brackets_links(self):
        """
        Generate links between brackets. It fills self.brackets_links
        with keys - brackets positions, values - links to next brackets
        and links to previous brackets.
        """
        brackets_stack = []
        for i, char in enumerate(self.code_array):
            if char == "[":
                brackets_stack.append(i)
            elif char == "]":
                start_jump_index = brackets_stack.pop()
                self.brackets_links[start_jump_index] = i
                self.brackets_links[i] = start_jump_index

    def _clear_comments(self):
        """
        Remove comments from code string
        """
        self.code_array = "".join(
            [
                char
                for char in self.code_array
                if char in InterpreterConfig().get_all_symbols()
            ]
        )

    def interpret(self, code_array: str, debug=False):
        """
        Given code string, translate it to python and execute instruction by instruction.
        """
        self.code_array: str = code_array
        self._preprocess_code_array()
        self.instruction_pointer: int = 0
        while self.instruction_pointer < len(self.code_array):
            self.instruction: chr = self.code_array[self.instruction_pointer]
            self.debugger.debug(debug)
            self.instruction_functions[self.instruction]()
            self.instruction_pointer += 1

    def interpret_increment_data_pointer(self):
        self.pointer += 1
        if self.pointer >= len(self.array):
            self.array.append(0)

    def interpret_decrement_data_pointer(self):
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = len(self.array) - 1

    def interpret_increment_value(self):
        self.array[self.pointer] = (self.array[self.pointer] + 1) % 256

    def interpret_decrement_value(self):
        self.array[self.pointer] = (self.array[self.pointer] - 1) % 256

    def interpret_output_value(self):
        print(chr(self.array[self.pointer]), end="")

    def interpret_input_value(self):
        self.array[self.pointer] = ord(input())

    def interpret_jump_forward(self):
        """
        Nested loops supported
        """
        if not self.array[self.pointer]:
            try:
                self.instruction_pointer = self.brackets_links[self.instruction_pointer]
            except KeyError:
                raise ValueError("Unbalanced jump forward/backward")

    def interpret_jump_backward(self):
        """
        Nested loops supported
        """
        try:
            self.instruction_pointer = self.brackets_links[self.instruction_pointer] - 1
        except KeyError:
            raise ValueError("Unbalanced jump forward/backward")
