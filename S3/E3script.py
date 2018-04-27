##################################################
############ MAIN SCRIPT OF SERIES 3 #############
##################################################

############### METHOD IMPORTATION ###############
# std stuff
import numpy as np
import matplotlib.pyplot as plt

from E3methods import * # optimization methods
    # PROTOTYPES : 
    # def GD(theta0, energy, grad, lamb, epsi, maxiter): 
    #     return steps, func
    # def LSGD(theta0, energy, grad, lamb, beta, alpha1, alpha2, epsi, maxiter): 
    #     return steps, func
    # def NRM(theta0, energy, grad, hessian, beta, alpha1, alpha2,  epsi, maxiter):
    #     return steps, func
    # def SGD(theta0, energy, grad, lamb, beta, alpha1, alpha2,  epsi, maxiter): 
    #     return steps, func

from E3functions import * # energy function definitions 
    # PROTOTYPES : 
    # def quadFunc(sigma): 
    #     return energy, grad, hess

##################### TO DO ######################
# - hess functions for logistic and student need to be added
# - logistic and student need to be tested

##################### MAIN #######################
print("1 : test run")
print("2 : analysis of lambda choice for quad fnct")
print("3 : ")

choice = int(input("please choose a nb : "))

if choice ==1:
    ### TEST RUNS 
    sigma = np.array([[2, 0], [0, 2]])
    #nrj1, grad1, hess1 = quadFunc(sigma)

    nrj1, grad1, hess1 = logistic()

    theta = [1, 1]
    lamb = 0.35
    epsi = 0.001 
    maxiter = 1000
    beta = 0.5 # decrease by half if step not accepted
    alpha1 = 0.0001 # recommended settings by Wikipedia
    alpha2 = 0.9

    # CG : 
    stepGD, funcGD = GD(theta, nrj1, grad1, lamb, epsi, maxiter) 
    plt.plot(funcGD, label="GD")

    # Line Search GD : 
    stepLSGD, funcLSGD = LSGD(theta, nrj1, grad1, lamb, beta, alpha1, alpha2, epsi, maxiter)
    plt.plot(funcLSGD, label="LSGD")

    # Newton-Raphson :
    stepNR, funcNR = NRM(theta, nrj1, grad1, hess1, beta, alpha1, alpha2, epsi, maxiter)
    plt.plot(funcNR, label="N-R")

    # Stochastic GD :
    stepSGD, funcSGD = SGD(theta, nrj1, grad1, lamb, beta, alpha1, alpha2, epsi, maxiter)
    plt.plot(funcSGD, label="SGD")

    plt.legend()
    plt.show()

if choice == 2: 
    ### analysis of choice of lamba 
    sigma = np.array([[2, 0], [0, 1]])
    nrj1, grad1, hess1 = quadFunc(sigma)

    theta = [1, 1]
    n = 10
    lamb = np.linspace(0.1,0.6, n)
    epsi = 0.001
    maxiter = 1000
    beta = 0.5 
    alpha1 = 0.0001
    alpha2 = 0.9 

    itercount = np.zeros((4, n))

    for i in range(0, n):  
        # CG : 
        stepGD, funcGD = GD(theta, nrj1, grad1, lamb[i], epsi, maxiter) 

        # Line Search GD : 
        stepLSGD, funcLSGD = LSGD(theta, nrj1, grad1, lamb[i], beta, alpha1, alpha2, epsi, maxiter)

        # Newton-Raphson :
        stepNR, funcNR = NRM(theta, nrj1, grad1, hess1, beta, alpha1, alpha2, epsi, maxiter)

        # Stochastic GD :
        stepSGD, funcSGD = SGD(theta, nrj1, grad1, lamb[i], beta, alpha1, alpha2, epsi, maxiter)
        
        itercount[0, i] = len(stepGD)
        itercount[1, i] = len(stepLSGD)
        itercount[2, i] = len(stepNR) 
        itercount[3, i] = len(stepSGD)

    
    plt.plot(lamb, itercount[0, :], label = "CG")
    plt.plot(lamb, itercount[1, :], label = "LSCG") 
    plt.plot(lamb, itercount[2, :], label = "NR") 
    plt.plot(lamb, itercount[3, :], label = "SGD")
        
    plt.legend()
    plt.show()

if choice == 3:
    print('hello')
