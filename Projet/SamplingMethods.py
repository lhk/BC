#######################################################
############ SAMPLING METHODS FOR PROJECT #############
#######################################################

# --- Metropolis Hastings -----------------------------
from Methods2 import MHRW # metropolis-hastings 
"""
def MHRW(theta0, maxiter, lamb, f, rando, display): 
    MHRW is the implementation of the Metropolis-Hastings sampling with random walk
    :param theta0: (scalar) initial step 
    :param maxiter: (scalar) maximum number of iterations 
    :param lamb: (scalar) one step size parameter
    :param f: (function handle) our distribution 
    :param rando: (0, 1) 0-unif error, 1-normal error
    :param display: (bool) if to display covariance and mean

    :return:
"""
from Methods2 import MHRWp # metropolis-hastings with burn-in
"""
def MHRWp(theta0, maxiter, lamb0, f, rando, display):
    MHRWp is the implementation of the Metropolis-Hastings sampling with random walk
    :param theta0: (scalar) initial step 
    :param maxiter: (scalar) maximum number of iterations 
    :param lamb0: (scalar) one step size parameter
    :param f: (function handle) our distribution 
    :param rando: (0, 1) 0-unif error, 1-normal error

    :return:
"""
# -----------------------------------------------------

# TODO : 
# - GVA (Laplace) 
# - IS/AR 

