# CREATES TRAIN AND TEST SETS FROM DATASET 

# --- IMPORTS 
from TransformData import *
import numpy as np
import numpy.random as rdm 

# --- MAIN()
# cut the dataset
dtrain = df.sample(frac=0.8, random_state=32)
dtest = df.drop(dtrain.index)

