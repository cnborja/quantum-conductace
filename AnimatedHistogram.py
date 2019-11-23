"""
Animated plot of a histogram. It shows each conductance trace and how its values contribute to the histogram.

Author: Carla Borja Espinosa
Date: July 2019

"""

import matplotlib.pyplot as plt
from scipy import *
import glob, os
import time
from sys import argv
import matplotlib.animation as animation
import numpy as np

"Input parameters"
path = argv[1]   # directory path where the traces data files are

"Variables"
line = 0         # line in data files from which start reading the data
xmin = 0.001     # minimum x-axis value to plot
xmax = 5.1       # maximum x-axis value to plot
cmin = 0         # minimum number of counts
cmax = 1000      # maximum number of counts
bins = 1000      # number of bins in x and y

os.chdir(path)
list_dat = [file for file in sorted(glob.glob("*.dat"))]
logbins= np.geomspace(xmin, xmax, bins)
fig = plt.figure(figsize=(16,9)) 
axs = fig.subplots(nrows=1, ncols=3)

def column(array,column):
    """Returns column n from file lines in array"""
    c = [float(i)  
        for i in [(line.split()[column]) 
        for line in array]]
    return c

def animate(i):
    with open(list_dat[i]) as g:
        glines = g.readlines()[line:]
        x = column(glines,0)
        y = column(glines,1)
        for j in y:
            y_cumulative.append(j)

    "Plot the data in the plane x-y"
    axs[0, 0].clear()
    axs[0, 0].plot(x, y, '.r', label = 'y0')
    axs[0, 0].set_ylabel('$ Counts $')
    axs[0, 0].set_xlim(xmin, xmax)
    axs[0, 0].set_ylim(cmin, cmax)

    "Histogram"
    axs[0, 1].clear()
    axs[0, 1].hist(y_cumulative, bins= bins, range = (xmin, xmax), 
                   orientation='vertical', color = 'b')
    axs[0, 1].set_xlabel('$G \, [G_{0}]$ ')
    axs[0, 1].set_xlim(xmin, xmax)
    axs[0, 1].set_ylim(cmin, cmax)

    "Histogram with logaritmic x-scale" 
    axs[0, 2].clear()
    axs[0, 2].hist(y_cumulative, bins=logbins, range = (xmin, xmax), 
                   orientation='vertical', color = 'b')
    axs[0, 2].set_xscale('log')
    axs[0, 2].set_xlim(xmin, xmax)
    axs[0, 2].set_ylim(cmin, cmax)
    
    return axs 

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.tight_layout()
plt.show()

