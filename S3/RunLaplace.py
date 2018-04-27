# --- IMPORTS 
from S3methods2 import laplace 
from GenerateData import GenerateDataset
import sys 
import matplotlib.pyplot as plt 

# Import size of dataset from outsize 
n = 50 # default dataset size
if(len(sys.argv)==2): 
        n = int(sys.argv[1])

# Generate a dataset 
data = GenerateDataset(n)

# visualize the data 
plt.scatter(data[:,0], data[:,1])
plt.show()
