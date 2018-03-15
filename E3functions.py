#################################################
######### FUNCTION DEFINITIONS FOR E3 ###########
#################################################
# --- CONTAINS : 
# quadFunc          Quadratic function x'*A*x
#
# --- PROTOTYPES : 
# def quadFunc(sigma) 
#     return 
#
# --- REQUIRES : 
# numpy             as np
#################################################
import numpy as np 

def quadFunc(sigma): 
    # --- IN: 
    # sigma         matrix nxn          st. E(x) = x'*sigma*x, sigma SDP
    # --- OUT: 
    # energy        function handle     energy 
    # grad          function handle     gradient of energy 
    # hess          function handle     hessian of energy
    # ------------------------------------------------
    
    def energy(x): 
        # returns the energy function as specified above 
        return np.dot(x, sigma@x)
    
    def grad(x): 
        # returns the gradient of the energy specified above 
        return 2*(sigma@x)

    def hess(x): 
        #returns the hessian of the energy specified above 
        return sigma

    return energy, grad, hess

def logistic(X, y):
    # --- IN : 
    # X             matrix              features
    # y             vector              observations
    # --- OUT : 
    # energy        function handle     energy 
    # grad          function handle     gradient of energy 
    # hess          function handle     hessian of energy
    # ------------------------------------------------
    
    def energy(x): 
        return sum(np.log(1 + np.exp(-y*(X@x))))
    
    def grad(x):
        return sum((-(X@y)*exp(-y*(X@x)))/(1 + exp(-x*(X@x))))

    def hess(x): 
        return -1

    return energy, grad, hess
