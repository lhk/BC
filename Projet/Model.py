# --- IMPORRTS
# ------ EXT. MODULES : 
import numpy as np # check if necessary
# ------ OWN FUNCTIONS : 
from TransformData import *
from Prior import defPrior # function handle for f(a)
from CondDist import defCondDist # function hangle for f(d|a)



# --- HANDLE EXTERNAL INPUTS 



# --- MAIN()
# f(a|d) ~ f(d|a)*f(a) 

# parameters of our model (internal to the program)
priorFlag = 1
condFlag = 1

# redeem prior function 
fprior = defPrior(priorFlag)

#redeem conditional distribution function 
fcond = defCondDist(condlfag)

# Sample to approximate posterior

# Test the model 
