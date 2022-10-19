from interpreter.config import InterpreterConfig


class InterpreterDebugger:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def debug(self, debug: bool):
        if debug and (
            self.interpreter.code_array[self.interpreter.instruction_pointer]
            not in {
                InterpreterConfig().increment_relative_base,
                InterpreterConfig().decrement_relative_base,
            }
        ):
            print("--------")
            print(self.interpreter.array, self.interpreter.pointer)
            print(
                "INSTRUCTION: "
                + str(self.interpreter.instruction_pointer)
                + ": "
                + self.interpreter.code_array[self.interpreter.instruction_pointer]
            )
