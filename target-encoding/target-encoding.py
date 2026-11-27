from collections import defaultdict
import numpy as np
def target_encoding(categories: list, targets: list) -> list:
    n = len(categories)
    ans = defaultdict(int)
    count = defaultdict(int)
    for i in range(n):
        ans[categories[i]]+=targets[i]
        count[categories[i]] +=1
    res = []
    for i in categories:
        res.append(ans[i] / count[i])


    

    return res
        
        
        
    pass