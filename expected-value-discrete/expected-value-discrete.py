import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    res = 0 
    for i in range(len(x)):
        res += x[i] * p[i]

    return float(res)
    pass