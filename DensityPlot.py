"""
2D colour density plot of conductance traces which are colapsed to a 
central point. The script recreates a figure similar to Figure 2.11 in:

Sabater Piqueres, C. (2013). Theoretical and experimental study of 
electronic transport and structure in atomic-sized contacts.

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
path = argv[1]        # directory path where the traces data files are

"Variables"
line = 0        # line in data files from which start reading the data 
colapse_point = 1.05  # reference point to center all traces 
plot = 1        # 1 or 2 to choose no or yes logaritmic scale
gmin= 0.03      # minimum conductance value to plot
gmax = 3        # maximum conductance value to plot
xmin = -0.02    # minimum x-axis value to plot
xmax = 0.02     # maximum x-axis value to plot
bins = 50       # number of bins in x and y 
cmax = 1000     # plot the bins with maximum 'cmax' counts


os.chdir(path)
list_r = [file for file in sorted(glob.glob("*.dat"))]
x_cum = np.array([])
y_cum = np.array([])

def column(array, n):
    """Returns column n from file lines in array"""
    x = np.array([float(i)  
        for i in [(line.split()[n]) 
        for line in array]])
    return x


bar = Bar('Completado:', max=len(list_r))    # Progress bar

for i in range(len(list_r)):
    with open(list_r[i]) as r:
        rlines = r.readlines()[line:]
        x = column(rlines, 0) 
        y = coltumn(rlines, 1)
        x1 = np.array([])
        y1 = np.array([])
        for k in range(0,len(y)):
            if gmin<y[k]<gmax:
                y1 = np.append(y1,y[k])
                x1 = np.append(x1,x[k])
           
        "Colapse point"
        j=0
        next = True
        x2 = np.array([])
        y2 = np.array([])
        while next:
            if j!=len(y1) and y1[j]<= colapse_point:
                x2 = x1-x1[j]
                y2 = y1
                next=False
            elif j==len(y1):
                x2=np.array([])
                y2=np.array([])
                next=False
            else: j=j+1

        x_cum = np.append(x_cum, x2)  
        y_cum = np.append(y_cum, y2)

    bar.next()
bar.finish()


if plot == 1:
    """ 2D colour density plot """
    x_bins = np.linspace(xmin, xmax, bins)
    y_bins = np.linspace(gmin, gmax, bins)
    plt.figure(figsize=(4,3)) 
    plt.hist2d(x_cum, y_cum, (x_bins, y_bins), 
               cmap=plt.cm.gist_ncar_r, norm = Normalize(), 
               density = False, cmax = cmax)
    plt.colorbar()
    plt.show()

elif plot == 2:
    """ 2D colour density plot with logaritmic y-scale"""
    x_bins = np.linspace(xmin, xmax, bins)
    y_logbins = np.logspace(np.log10(gmin), np.log10(gmax), bins)
    plt.figure(figsize=(4,3))
    plt.hist2d(x_cum, y_cum, (x_bins, y_logbins), 
               cmap=plt.cm.gist_ncar_r, norm = LogNorm(), 
               density = False, cmax = cmax)
    plt.colorbar()
    plt.yscale('log')
    plt.show()


