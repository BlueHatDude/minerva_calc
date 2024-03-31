from enum import Enum

class SolutionSet:

    def __init__(self) -> None:

        self.total: float = 0.0

        self.variables: dict = {}
        

    def add_variable(symbol: str, value: float) -> None:
        ...


class TokenType(Enum):
    EMPTY = 0
    OP_PLUS = 1
    OP_MINUS = 2
    OP_MULTIPLY = 3
    OP_DIVIDE = 4
    OP_EXPONENT = 5
    LEFT_PAR = 6
    RIGHT_PAR = 7
    SQRT = 8
    SIN = 9
    COS = 10
    TAN = 11
    LOG = 12
    LN = 13
    
    INTEGER = 14
    DECIMAL = 15
    SYMBOL = 16


class Token:
    
    def __init__(self, type: TokenType) -> None:
        self.type = TokenType
        

class Solver:
    
    def __init__(self, equ: str) -> None:
        self.equ = equ.replace(" ", "")     
        self.solutions = SolutionSet()
        self.tokens: list[Token] = []


    def combine_nums(self, inp: list[str]) -> list[str]:
        for index, value in enumerate(inp):
            if value in "0123456789":
                j: int = index + 1
                while inp[j] in "0123456789":
                    inp[index] += inp[j]
                    del inp[j]
                    j += 1


    def _tokenize(self) -> None:
        # 2 + 4 -> INTEGER:2 OP:PLUS INTEGER:4
        str_tokens: list[str] = [char for char in self.equ]
        self.combine_nums(str_tokens)

    
    def evaluate(self) -> None:
        ...
