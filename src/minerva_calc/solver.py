from enum import Enum


def constrain_num(n: int, nmax: int, nmin: int) -> int:
    """constrains integer value

    Args:
        n (int): input
        nmax (int): maximum number
        nmin (int): minimum number

    Returns:
        if n is greater than max, return max,
        if n is less than min, return min
        else return n"""
    return max(min(nmax, n), nmin)


def str_to_num(s: str) -> int | float | None:
    """converts string into appropriate number type (does not handle negatives)

    Args:
        s (str): input

    Returns:
        int | float: if string is valid num
        None: if string is not valid num
    """

    if s.isdigit():
        return int(s)
    else:
        try:
            f = float(s)
            return f
        except ValueError:
            return None


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
    LOG_10 = 12
    LOG_E = 13

    INTEGER = 14
    DECIMAL = 15
    SYMBOL = 16


def type_to_str(inp_type: TokenType) -> str:
    match inp_type:
        case TokenType.EMPTY:
            return "EMPTY"
        case TokenType.OP_PLUS:
            return "OP_PLUS"
        case TokenType.OP_MINUS:
            return "OP_MINUS"
        case TokenType.OP_MULTIPLY:
            return "OP_MULTIPLY"
        case TokenType.OP_DIVIDE:
            return "OP_DIVIDE"
        case TokenType.OP_EXPONENT:
            return "OP_EXPONENT"
        case TokenType.LEFT_PAR:
            return "LEFT_PAR"
        case TokenType.RIGHT_PAR:
            return "RIGHT_PAR"
        case TokenType.SQRT:
            return "SQRT"
        case TokenType.SIN:
            return "SIN"
        case TokenType.COS:
            return "COS"
        case TokenType.TAN:
            return "TAN"
        case TokenType.LOG_10:
            return "LOG_10"
        case TokenType.LOG_E:
            return "LOG_E"
        case TokenType.INTEGER:
            return "INTEGER"
        case TokenType.DECIMAL:
            return "DECIMAL "
        case TokenType.SYMBOL:
            return "SYMBOL"


class Token:
    def __init__(self, type: TokenType, value: int | float = None) -> None:
        self.type = type
        self.value = value

    def __eq__(self, value: object) -> bool:
        if isinstance(value, TokenType):
            return self.type == value
        elif isinstance(value, Token):
            return self.type == value.type
        else:
            raise TypeError(
                "Equality comparison between 'Token' and non 'Token' or 'TokenType'"
            )

    def __str__(self) -> str:
        if self.type not in [TokenType.INTEGER, TokenType.DECIMAL]:
            return f"Type: {type_to_str(self.type)}"
        else:
            return f"Type: {type_to_str(self.type)} | Value: {self.value}"


class Solver:
    def __init__(self, equ: str) -> None:
        self.equ = equ.replace(" ", "")
        self.tokens: list[Token] = []

    def _lower_all(self, inp: list[str]) -> None:
        for index, s in enumerate(inp):
            inp[index] = s.lower()

    def _combine_nums(self, inp: list[str]) -> list[str]:
        """a function that takes a list of strs and combines all adjacent digits into one number


        Args:
            inp (list[str]): example: ['1', '2', '3', '+', '4'] -> ['123', '+', '4']
        """

        new_inp = inp

        for index, char in enumerate(new_inp):
            # find first digit
            if char.isdigit():
                j_index: int = constrain_num(index + 1, nmax=(len(new_inp) - 1), nmin=0)

                # covering edge case where there is a single digit at the end
                if j_index == index:
                    break

                # find adjacent nums
                while new_inp[j_index].isdigit():
                    new_inp[index] += new_inp[j_index]
                    # marked for deletion
                    new_inp[j_index] = "X"
                    j_index = constrain_num(
                        j_index + 1, nmax=(len(new_inp) - 1), nmin=0
                    )

        # delete unecessary indexes
        new_inp = [s for s in new_inp if s != "X"]
        return new_inp

    def _combine_letters(self, inp: list[str]) -> list[str]:
        new_inp = inp

        for index, char in enumerate(new_inp):
            if char.isalpha():
                j_index: int = constrain_num(index + 1, nmax=(len(new_inp) - 1), nmin=0)

                while new_inp[j_index].isalpha():
                    new_inp[index] += new_inp[j_index]
                    new_inp[j_index] = "0"
                    j_index = constrain_num(
                        j_index + 1, nmax=(len(new_inp) - 1), nmin=0
                    )

        new_inp = [s for s in new_inp if s != "0"]
        return new_inp

    def _tokenize(self) -> None:
        # preparing input
        str_tokens: list[str] = list(self.equ)
        str_tokens = self._combine_nums(str_tokens)
        str_tokens = self._combine_letters(str_tokens)

        for value in str_tokens:
            match value:
                case "+":
                    self.tokens.append(Token(TokenType.OP_PLUS))
                case "-":
                    self.tokens.append(Token(TokenType.OP_MINUS))
                case "*":
                    self.tokens.append(Token(TokenType.OP_MULTIPLY))
                case "/":
                    self.tokens.append(Token(TokenType.OP_DIVIDE))
                case "^":
                    self.tokens.append(Token(TokenType.OP_EXPONENT))
                case "(":
                    self.tokens.append(Token(TokenType.LEFT_PAR))
                case ")":
                    self.tokens.append(Token(TokenType.RIGHT_PAR))
                case "sqrt":
                    self.tokens.append(TokenType(TokenType.SQRT))
                case "sin":
                    self.tokens.append(Token(TokenType.SIN))
                case "cos":
                    self.tokens.append(Token(TokenType.COS))
                case "tan":
                    self.tokens.append(Token(TokenType.TAN))
                case "log":
                    self.tokens.append(Token(TokenType.LOG_10))
                case "ln":
                    self.tokens.append(Token(TokenType.LOG_E))
                case _:
                    num_val = str_to_num(value)
                    if num_val is not None:
                        if isinstance(num_val, int):
                            self.tokens.append(Token(TokenType.INTEGER, num_val))
                        elif isinstance(num_val, float):
                            self.tokens.append(Token(TokenType.DECIMAL, num_val))

    def _parse(self) -> None:
        """parses tokens to create numerical ouput, following order of operations"""

        # [ '(', '4', '+', '8', ')', '*', 2 ]
        # [ ['4', '+', '8', ], '*', 2 ]

        left_par_indexes: list[int] = [
            i for i, k in enumerate(self.tokens) if k.type == TokenType.LEFT_PAR
        ]
        left_par_indexes.sort(reverse=True)

        for index in left_par_indexes:
            right_par_index = self.tokens.index(TokenType.RIGHT_PAR)
            self.tokens[index] = self.tokens[(index + 1) : right_par_index]

    def _print_tokens(self) -> None:
        for token in self.tokens:
            print(token)

    def _run_tests(self) -> None:
        self._tokenize()
        self._parse()
        self._print_tokens()

    def evaluate(self) -> None: ...
