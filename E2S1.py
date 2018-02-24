import numpy as np 
import numpy.random as nprdm
import math as m
import matplotlib.pyplot as plt 


def GenerateDataset(n, theta0):
    # n scalar number of points 
    # theta0 scalar in [0, 1]

    return nprdm.binomial(1, theta0, n)


def ComputePosterior(dataset, alpha, beta):
    # --- INPUT 
    # dataset vector our dataset
    # alpha scalar param. of dist. 
    # beta scalar param. of dist. 
    # --- OUTPUT 
    # post function for unnormalized posterior
    # C scalar value of normalization constant
    # a, b bounds of the 0.95 credible interval 
    
    alpha_h = alpha + sum(dataset)
    beta_h = beta + sum(1-dataset)

    # normalization constant 
    C = (m.gamma(alpha + beta)*m.gamma(alpha_h)*m.gamma(beta_h))/(m.gamma(alpha)*m.gamma(beta)*m.gamma(alpha_h + beta_h))

    # posterior function 
    def post(theta):
        Cn = m.gamma(alpha + beta)/(m.gamma(alpha)*m.gamma(beta))
        return (1-theta)**(beta_h -1)*theta**(alpha_h -1)*Cn

    # compute bounds of the 0.95 credible 
    e = 1.96*(alpha_h*beta_h/((alpha_h + beta_h)**2*(1+alpha_h + beta_h)))**2
    a = alpha_h/(alpha_h + beta_h) - e
    b = a + 2*e

    return(post, C, a, b)


def plotPosth(post):
    n = 30

    ft = np.zeros(n+1) 
    for i in range(0, n+1):
        ft[i] = post(i/n)

    plt.plot(ft)
    plt.show()
    
    return 0 


def plotPost(post, C, a, b): 
    n = 30
    ft = np.zeros(n+1)
    for i in range(0, n+1): 
        ft[i] = C*post(i/n)

    m = np.max(ft)

    plt.figure(1)
    plt.plot(ft)
    plotCI(a, b, m)
    plt.show()

    return 0

def plotCI(a, b, m):
    n = 20
    
    #CI = (b-a)*np.array(range(0, n+1))/n + a
    li = np.ones(n+1)
    lo = m*np.array(range(0, n+1))/n

    plt.plot(a*li, lo, 'r')
    plt.plot(b*li, lo, 'r')

    return 0


#----------------------------------------------------


theta0 = 0.5
n = 30

dataset = GenerateDataset(n, theta0)

alpha = 1
beta = 2

post, C, a, b = ComputePosterior(dataset, alpha, beta)

plotPost(post, C, a, b)
