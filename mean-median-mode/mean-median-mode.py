from collections import Counter
import numpy as np
import pandas as pd
from scipy import stats

def mean_median_mode(x: list) -> dict:
    data = np.array(x)

    mean = np.mean(data)
    median = np.median(data)
    mode_res = stats.mode(data,keepdims = True)

    mode = mode_res.mode[0]

    ans = {'mean': float(mean) , 'median':float(median) , 'mode' : float(mode)}
    return ans