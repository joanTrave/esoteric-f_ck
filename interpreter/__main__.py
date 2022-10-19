import sys

from interpreter.exceptions import UnbalancedBracketsException, SyntaxException
from interpreter.interpreter import Interpreter


def main():
    if len(sys.argv) != 2:
        print("Usage: ./interpreter.py <file>")
        exit(1)

    try:
        with open(sys.argv[1]) as f:
            code = f.read()
            Interpreter().interpret(code)
    except FileNotFoundError:
        print(f"FileNotFoundError: {sys.argv[1]}")
    except UnbalancedBracketsException:
        print("UnbalancedBracketsException")
    except SyntaxException as err:
        print(f"SyntaxException: {str(err)}")


if __name__ == "__main__":
    main()
