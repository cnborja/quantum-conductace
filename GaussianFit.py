"""

Fitting of a histogram using gaussian functions

Author: Carla Borja Espinosa
Date: July 2019


"""

from scipy import *
import glob, os
from sys import argv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import mixture
from progress.bar import Bar
from scipy.stats import norm
import scipy.stats as stats

"Input Arguments"
dataFile = argv[1]    # file with values to represent in a histogram

"Variables"
xmin = 0.3    # minimun value in x-axis
xmax = 1.2    # maximum value in x-axis
bins = 1000   # number of bins to consider for the histogram
ng = 6        # number of gaussians to consider for fitting

x = np.linspace(xmin, xmax, 1300)
y_cumulative = np.array(np.loadtxt(dataFile))
y_cumulative = y_cumulative.reshape(-1,1)
gmm = mixture.GaussianMixture(n_components= ng)
gmm.fit(y_cumulative)
means = gmm.means_
covars = gmm.covariances_
weights = gmm.weights_

"Plot of the Histogram""
fig = plt.figure(figsize=(8,3)) 
ax1 = fig.subplots(nrows=1,ncols=1)
ax1.hist(y_cumulative, bins= bins, range = (xmin, xmax), alpha = 1, orientation='vertical', color = 'b', histtype = 'step', density = 1)

"Plot for each gaussian function"
gauss = np.empty(ng)
for i in range(0, ng):
    gauss[i] = weights[i]*stats.norm.pdf(x,means[i],
               np.sqrt(covars[i])).ravel()
    ax1.plot(x, gauss[i], lw = l2, ls = 'dashed')

"Plot the sum of all fitted gaussian functions"
sum = np.empty(len(gauss[0]))
for i in range(0, len(gauss)):
    sum = sum + gauss[i]

ax1.plot(x, sum, c='black', lw = 3, ls = 'solid')
ax1.set_xlim(xmin, xmax)
ax1.set_xlabel('$G \, [G_{0}]$ ')
plt.tight_layout()
plt.show()

