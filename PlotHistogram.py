"""
Plot of a histogram cosidering the column values in the input file

Author: Carla Borja Espinosa
Date: July 2019

"""

import matplotlib.pyplot as plt
from scipy import *
import glob, os
from sys import argv
import numpy as np

"Input parameters"
dataFile = argv[1]    # file with values to represent in a histogram

"Variables"
xmin = 0.001    # minimum x-axis value to plot
xmax = 5.1      # maximum x-axis value to plot
cmin = 0        # minimum number of counts
cmax = 1000     # maximum number of counts
bins = 1000     # number of bins
   

y_cumulative = np.loadtxt(dataFile)
logbins= np.geomspace(xmin, xmax, bins)
fig = plt.figure(figsize=(9,9)) 
ax1, ax2, ax3 = fig.subplots(nrows=3, ncols=1)

"Histogram"
ax1.hist(y_cumulative, bins= bins, range = (xmin, xmax), 
         orientation='vertical', color = 'b', histtype = 'step')
ax1.set_xlim(xmin, xmax)
ax1.set_ylim(cmin, cmax)

"Histogram with logaritmic x-scale" 
ax2.hist(y_cumulative, bins=logbins, range = (xmin, xmax), 
         orientation='vertical', color = 'b', histtype = 'step')
ax2.set_xscale('log')
ax2.set_ylabel('$ Counts $')
ax2.set_xlim(xmin, xmax)
ax2.set_ylim(cmin, cmax)

"Histogram with log-log scale" 
ax3.hist(y_cumulative, bins=logbins, range = (xmin, xmax), 
         orientation='vertical', color = 'b', histtype = 'step')
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.set_xlabel('$G \, [G_{0}]$ ')
ax3.set_xlim(xmin, xmax)
ax3.set_ylim(cmin, cmax)
    
plt.tight_layout()
plt.show()
