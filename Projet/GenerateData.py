import numpy as np
import matplotlib.pyplot as plt 
import random as rdm 

def GenerateDataset(n):
    """ 
    GENERATEDATASET generates a sample dataset
    :param n: (scalar) nb of pts. 
    :param f: (function handle) function along which to sample 
    :return: 
    """ 
    data = np.zeros((n, 3))
    # parameters (changable)
    p = 0.5

    # data generation
    for i in range(0, n): 
        t = rdm.binomial(1, p)
        data[i, 0] = t
        data[i, 1] = t*rdm.normal(0,1) * (1-t)*rdm.normal(2, 1)
        data[i, 2] = t*rdm.normal(0,1) * (1-t)*rdm.normal(2, 1)
    return data 

