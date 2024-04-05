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


    def combine_nums(self, inp: list[str]):        
        """ a function that takes a list of strs and combines all adjacent digits into one number


        Args:
            inp (list[str]): example: ['1', '2', '3', '+', '4'] -> ['123', '+', '4']
        """        

        for index, char in enumerate(inp):
            # find first digit
            if char.isdigit():
                j_index: int = index + 1 if (index + 1) < len(inp) else -1
                
                # if reached end of list
                if j_index == -1: continue
                
                # find adjacent nums
                while inp[j_index].isdigit():
                    inp[index] += inp[j_index]
                    # marked for deletion
                    inp[j_index] = "X"
                    j_index += 1
            # delete unecessary indexes
            inp = [char for char in inp if char != 'X']                


    def _tokenize(self) -> None:
        # 2 + 4 -> INTEGER:2 OP_PLUS INTEGER:4
        str_tokens: list[str] = [char for char in self.equ]
        self.combine_nums(str_tokens)


    def _run_tests(self) -> None:
        str_tokens: list[str] = [char for char in self.equ]
        self.combine_nums(str_tokens)
        print(str_tokens)


    def evaluate(self) -> None:
        ...
