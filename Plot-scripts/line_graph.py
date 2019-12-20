#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams

#rcParams['figure.figsize'] = 8, 5
#rcParams['figure.figsize'] = 7, 5
rcParams['figure.figsize'] = 12, 12


def splitSerToArr(ser):
    return [ser.index, ser.as_matrix()]


def graph(title, filename): 

    """
    xs = range(2, 5)#range(2, 4)
    series1 = [12.4679, None, None]
    series2 = [4.42318, 14.3225, 15.5052]
    series3 = [2.77863, 3.24947, 3.49185]
    """

    """
    xs = range(2, 17)
    series1 = [12.4679, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    series2 = [4.42318, 14.3225, 15.5052, None, None, None, None, None, None, None, None, None, None, None, None]
    series3 = [2.77863, 3.24947, 3.49185, None, None, None, 3.91183, None, None, None, 3.97833, None, None, None, 4.0425]
    plt.ylabel('Time (ms)')

    """
    """
    xs = range(1, 7)
    series1 = [98.41, 8.38, None, None, None, None]
    series2 = [97.57, 17.14, 8.13, 8.23, None, None]
    series3 = [106.85, 34.02, 30.58, 30.51, 30.46, 30.37]
    plt.ylabel('Bandwidth (GB/s)')
    """
    """
    xs = range(2, 17)
    series1 = [8.8826, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    series2 = [9.6263, 6.9794, 5.4775, None, None, None, None, None, None, None, None, None, None, None, None]
    series3 = [9.4461, None, 5.5789, None, 4.1859, None, 3.3905, None, 2.8812, None, 2.5148, None, 2.2556, None, 1.9353]
    plt.ylabel('Time (s)')
    """
    xs = range(1, 17)
    series1 = [666.7810, 1041.3000, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    # yme - same
    series2 = [618.6470, 960.6280, 924.1910, 1119.1400, None, None, None, None, None, None, None, None, None, None, None, None]
    # yme - diff
    series4 = [618.6470, 973.8870, 924.1910, 1119.1400, None, None, None, None, None, None, None, None, None, None, None, None]
    # dgx - same 
    series3 = [646.5240, 1005.6100, None, 923.6450, None, 902.6660, None, 1176.9600, None, 1438.6300, None, 1635.6200, None, 1938.2200, None, 2230.6100]
    # dgx - diff
    series5 = [646.5240, 1035.0200, None, 950.2330, None, 904.1280, None, 1163.8400, None, 1438.6300, None, 1635.6200, None, 1938.2200, None, 2230.6100]

    plt.ylabel('Performance (GFLOPS)')

    s3 = pd.Series(series3, index=xs)
    s5 = pd.Series(series5, index=xs)

    plt.plot(xs, series1, linestyle='-', marker='o', color='#2f2f91', label='Mini Summit (Power AC922, 2 GPUs)')
    plt.plot(xs, series4, linestyle='--', marker='^', color='#60a9e6', label='Yme (Power AC922, 4 GPUs) - Different NUMA nodes')
    plt.plot(xs, series2, linestyle='-', marker='o', color='#3886c7', label='Yme (Power AC922, 4 GPUs)')
    plt.plot( *splitSerToArr(s5.dropna()), linestyle='--', marker='^', color='#76a887', label='Heid (DGX-2, 16 GPUs) - Different NUMA nodes')
    plt.plot( *splitSerToArr(s3.dropna()), linestyle='-', marker='o', color='#69b87f', label='Heid (DGX-2, 16 GPUs)')


    plt.xlabel('Number of GPUs')

    plt.legend()
    plt.title(title)

    plt.savefig(filename, bbox_inches = 'tight', pad_inches = 0)


    plt.show()

#graph('Multi-GPU systems: NCCL MPI AllReduce', 'nccl-mpi-allreduce.svg')
#graph('Multi-GPU systems: NCCL Broadcast', 'nccl-broadcast.svg')
#graph('Multi-GPU systems: QTC', 'qtc-multi.svg')
graph('Multi-GPU systems: Stencil 2D', 'stencil2d-multi.svg')
