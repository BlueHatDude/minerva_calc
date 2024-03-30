from minerva_calc.solution_set import SolutionSet


class Solver:
    
    def __init__(self, equ: str) -> None:
        self.equ = equ     
        self.solutions = SolutionSet()


    def _tokenize(self) -> None:
        ...

    
    def evaluate(self) -> None:
        ...
