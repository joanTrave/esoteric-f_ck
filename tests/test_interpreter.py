from interpreter.interpreter import Interpreter

HELLO_WORLD_BF: str = (
    "++++++++[>++++[>++>+dfghjk++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---."
    "+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
)

ASCII_A = "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
PRINT = "."


def test_hello_world():
    interpreter = Interpreter()
    interpreter.interpret(
        HELLO_WORLD_BF,
        debug=False,
    )


def test_abcdefgh():
    interpreter = Interpreter()
    interpreter.interpret(
        ">" + ASCII_A + "<++++++++[>.+<-]",
        debug=False,
    )
