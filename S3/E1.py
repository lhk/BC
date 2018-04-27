import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def GD(energy, grad, lamb, init, epsi, maxiter):
    steps = []
    nrjs = []
    theta = init 
    k = 0

    while((energy(theta)>=epsi) & (k<maxiter)):
        theta = theta - lamb*grad(theta) 
        steps.append(theta)
        nrjs.append(energy(theta))
        k = k+1 
    return (steps, nrjs)

def GDLS(energy, grad, lamb, init, epsi, maxiter):
    steps = []
    nrjs = []
    theta = init
    k = 0

    #while(0):
    return (0)

def Newton(energy, grad, hess, init, epsi, maxiter): 
    steps = []
    nrjs = []
    theta = init 
    k = 0
    
    while((la.norm(grad(theta))>epsi) & (k<maxiter )):
        theta = theta - la.inv(hess(theta))@grad(theta)
        steps.append(theta)
        nrjs.append(energy(theta))
        k = k+1
    return (steps, nrjs)

def quadtarget(sigma):
    def energy(x):
        # x is defined as a nx1 array 
        return (np.dot(x ,sigma @ x))
    def grad(x): 
        return(2 * sigma @ x)
    def hess(x): 
        return sigma
    return (energy, grad, hess)

def logreg(x, y): 
    # y nx1 vector 
    # x nxm vector

    n = np.shape(y)[0]
    def energy(theta): 
        return (sum(np.log(1 + np.exp(-y*(x@theta)))))
    def grad(theta):
        s = 0
        for i in range(0, n): 
            inner = np.dot(x[i, :], theta)
            s += (-y[i]*x[i, :]*exp(-y[i]*inner))/(1 + np.exp(-y[i]*inner))
        return s

    return (energy, grad)

def lsStud(x, d): 

    def energy(mu, sigma):
        partial = (d+1)/2*log(1 + (((x - y)/sigma)**2)/d)
        return sum(log(sigma) + partial)
    def grad(mu, sigma): 
        dm = sum(-((d+1)/2)*((x - mu)**2)/(d + ((x-mu)/sigma)**2))
        ds = sum(1/sigma - 0.5*(d+1)*((x-y)**2)*(1/sigma)/(1 + 1/d*((x - mu)/sigma)**2))
        return np.array([dm, ds])

    return (energy, grad)
# -------------------------------------------------

N = 50
lamb = np.linspace(0, 1, N)

sigma = np.array([[2, 0, 0],[0, 2, 0], [0, 0, 2]])
epsi = 0.001; 
maxiter = 100;

init = np.array([0, 1, 2])

stepa = []

energy, grad , hess = quadtarget(sigma)
#energy, grad = logreg(x, y)
#energy, grad = lsStud(x, d)


for i in lamb:
    steps, nrjs = GD(energy, grad, i, init, epsi, maxiter) 
    stepa.append(len(steps))

plt.plot(lamb, stepa)
plt.xlabel("lambda")
plt.show()    


steps, nrjs = Newton(energy, grad, hess, init, epsi, maxiter)

x = np.linspace(-5, 5, 60)
f = []
for i in range(0, 20): 
    f.append(energy(x[3*i: 3*i+3]))
plt.plot(x, f)
plt.show()

print(len(steps))
print(steps[len(steps)])
print(nrjs[len(nrjs)])
