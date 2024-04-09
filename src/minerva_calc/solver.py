from enum import Enum


def constrain_num(n: int, nmax: int, nmin: int) -> int:
    """ constrains integer value

    Args:
        n (int): input
        nmax (int): maximum number
        nmin (int): minimum number

    Returns:
        if n is greater than max, return max,
        if n is less than min, return min
        else return n    """    
    return max(min(nmax, n), nmin)


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

        new_inp = inp

        for index, char in enumerate(new_inp):
            # ['1', '2', '3', '4', '+', '2', '4']
            # 

            # find first digit
            if char.isdigit():
                j_index: int = constrain_num(index + 1, nmax=len(new_inp) - 1, nmin=0)
                
                # if reached end of list
                if j_index == -1:
                    continue
                
                # find adjacent nums
                while new_inp[j_index].isdigit():
                    new_inp[index] += new_inp[j_index]
                    # marked for deletion
                    new_inp[j_index] = "X"
                    j_index = constrain_num(j_index + 1, nmax=len(new_inp) - 1, nmin=0)

        # delete unecessary indexes
        new_inp = [s for s in new_inp if s != 'X']
        return new_inp


    def _tokenize(self) -> None:
        # 2 + 4 -> INTEGER:2 OP_PLUS INTEGER:4
        str_tokens: list[str] = [char for char in self.equ]
        self.combine_nums(str_tokens)


    def _run_tests(self) -> None:
        str_tokens: list[str] = [char for char in self.equ]
        str_tokens = self.combine_nums(str_tokens)
        print(str_tokens)


    def evaluate(self) -> None:
        ...
