"""
Store in a file all the values whose occurrence frequency is going to 
be represented in a histogram

Author: Carla Borja Espinosa
Date: July 2019

"""

import matplotlib.pyplot as plt
from scipy import *
import glob, os
from sys import argv
import numpy as np
from progress.bar import Bar

"Input parameters"
path = argv[1]       # directory path of the conductance traces files
dataFile = argv[2]   # file name where the values will be stored

"Variables"
line = 0             # line number to start reading the data in traces 
                     # files

os.chdir(path)
list_dat = [file for file in sorted(glob.glob("*.dat"))]

def column(array, n):
    """Returns column n from file lines in array"""
    c = [float(i)  
        for i in [(line.split()[n]) 
        for line in array]]
    return c

bar = Bar('Completado:', max=len(list_dat))

for i in range(len(list_dat)):
    with open(list_dat[i]) as g:
        glines = g.readlines()[line:]
        y = column(glines,1)
        for j in y:
            y_cumulative.append(j)

    bar.next()
bar.finish()

np.savetxt(dataFile, y_cumulative)
