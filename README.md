# Minerva Calc Python Library
A Python library for evaluating expressions from strings.

# Overview
The basis of all minerva_calc operations is the `Solver` object. You must pass a string into the constructor and then call the appropriate method depending on how you want to evaluate the expression/equation. 

`Solver.evaluate()`: returns a double with the total value of the inputted equation, including all variables being substituted in. 
`Solver.get_vars()`: returns a dictionary with all of the variables and their corresponding values

Syntax
```
from minerva_calc.solver import Solver

result_one = Solver("2 + 4").evaluate()
print(result_one) # 6.0

equ_one = Solver("2x + 5 = 10")
print(equ_one.get_var()) # {'x': 2.5}
print(equ_one.evalute()) # 10.0

```
