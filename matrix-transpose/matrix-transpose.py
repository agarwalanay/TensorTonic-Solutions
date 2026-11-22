import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    ROWS,COLS = len(A) , len(A[0]) #2 l 3
    ans = [[0]*ROWS for _ in range(COLS)]
    for i in range(COLS):
        for j in range(ROWS):
            ans[i][j] = A[j][i]
    res = np.array(ans)
    return res
    pass
