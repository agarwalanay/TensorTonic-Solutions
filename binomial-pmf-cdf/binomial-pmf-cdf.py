import math
from scipy.stats import binom

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    return {'pmf' : float(binom.pmf(n=n,k=k,p=p)) , 'cdf' : float(binom.cdf(n=n,k=k,p=p)) }
    
    
    
    pass