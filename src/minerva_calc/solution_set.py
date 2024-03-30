class SolutionSet:
    
    def __init__(self) -> None:
        self.total: float = 0.0
        self.variables: dict = {}
    
    
    def add_variable(symbol: str, value: float) -> None:
        ...
    