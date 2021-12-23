import os
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import select

class PlotGraph:
    def __init__(self, filePath):
        self.filePath = filePath

    def plotGraph(self):
        f = open(self.filePath, "r")
        functionName = f.readline()
        print(functionName)
        while(functionName):
            f.readline()
            srcga_fmin = f.readline().split(',')
            srcga_fmin.pop()
            srcga_fmin = np.array(srcga_fmin).astype(np.float)

            f.readline()
            rcga_p_fmin = f.readline().split(',')
            rcga_p_fmin.pop()
            rcga_p_fmin = np.array(rcga_p_fmin).astype(np.float)

            f.readline()
            rcga_ps_fmin = f.readline().split(',')
            rcga_ps_fmin.pop()
            rcga_ps_fmin = np.array(rcga_ps_fmin).astype(np.float)

            f.readline()
            de_fmin = f.readline().split(',')
            de_fmin.pop()
            de_fmin = np.array(de_fmin).astype(np.float)

            f.readline()
            mps_de_fmin = f.readline().split(',')
            mps_de_fmin.pop()
            mps_de_fmin = np.array(mps_de_fmin).astype(np.float)

            plt.boxplot([srcga_fmin, rcga_p_fmin, rcga_ps_fmin, de_fmin, mps_de_fmin])
            plt.title(functionName)
            plt.ylabel('Min fitness score')
            plt.xticks([1, 2, 3, 4, 5], ['SRCGA', 'RCGA-P', 'RCGA-PS', 'DE/BEST/1/Bin', 'MPS-DE'])

            plt.show()
            save_path = 'Experiments/'
            name =  " Experiment Result for " + functionName
            figureName = os.path.join(save_path, name)
            plt.savefig(figureName)

            functionName = f.readline()
        f.close()

    