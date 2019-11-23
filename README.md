# Quantum Conductace 
## Atomic-sized metallic contacts

Python scripts to plot traces, histograms and colour density plots of conductance measurements from atomic-sized metallic contacts. The traces of conductance are a graph representation of the quantization of conductance that arises from the radial confinment in atomic-sized metallic contacts. For more information about traces of conductance see section 2.4 in:

*Sabater Piqueres, C. (2013). Theoretical and experimental study of electronic transport and structure in atomic-sized contacts.*

### Prerequisites
For running the scripts, you need Python3 with scipy, numpy and matplotlib.

### Getting started
Our files with the data of each trace of conductance need to be organized in two columns, one for the time, steps or voltage, depending on the experimental measurement, and the other one with the values of conductance. Set the variables in each script according to your measurements, and pass the input parameters when running the code in terminal as:

$ python3 script.py input-parameters

The output file from DataHistogram.py is used as input for PlotHistogram.py and GaussianFit.py scripts.


