import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    res = []
    for i in x :
        if i == 0 :
            res.append(float(1-p))
        else : 
            res.append(float(p))
    arr = np.array(res)
    return {'pmf': arr , 'mean' : float(p) , 'variance' : float(p*(1-p))} 
        
    pass