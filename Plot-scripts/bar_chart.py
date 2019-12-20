#!/usr/bin/env python

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
from matplotlib.ticker import PercentFormatter

rcParams['figure.figsize'] = 7, 5
plt.rcParams.update({'font.size': 12})

def bar_chart_standard(objects, values, title, unit, filename, object_label=''): 
    
    y_pos = np.arange(len(objects))
    #plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.bar(y_pos, values, alpha=0.8, color='#87a2c7')

    plt.xticks(y_pos, objects)
    plt.ylabel(unit)

    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

    # If label for x-axis is needed
    if object_label != '':
        plt.xlabel(object_label)

    plt.title(title)
    # Save the figure
    plt.savefig(filename, bbox_inches = 'tight', pad_inches = 0)
    # Show the figure
    plt.show()

def bar_chart_double(objects, values1, values2, title, unit, filename, object_label='', interval1=None, interval2=None): 



    if interval1 is not None:
        #axes.set_ylim(interval)
        plt.ylim(interval1, interval2)

    y_pos = np.arange(len(objects))
    bar_width = 0.35
    opacity = 0.8

    
    """
    f, (ax, ax2) = plt.subplots(2, 1, sharex=True)

    ax = plt.bar(y_pos, values1, bar_width,
        alpha=opacity,
        color='#81d4ca',
        label='Tensor Cores disabled')
    ax = plt.bar(y_pos + bar_width, values2, bar_width,
        alpha=opacity,
        color='#87a2c7',
        label='Tensor Cores enabled')
    ax2 = plt.bar(y_pos, values1, bar_width,
        alpha=opacity,
        color='#81d4ca',
        label='Tensor Cores disabled')
    ax2 = plt.bar(y_pos + bar_width, values2, bar_width,
        alpha=opacity,
        color='#87a2c7',
        label='Tensor Cores enabled')


    ax.set_ylim(6000000, 7000000)
    ax2.set_ylim(0, 2500000)

    ax.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax.xaxis.tick_top()
    ax.tick_params(labeltop='off')  # don't put tick labels at the top
    ax2.xaxis.tick_bottom()
    """
    plt.bar(y_pos, values1, bar_width,
        alpha=opacity,
        color='#81d4ca',
        label='Tensor Cores disabled')
    plt.bar(y_pos + bar_width, values2, bar_width,
        alpha=opacity,
        color='#87a2c7',
        label='Tensor Cores enabled')
    plt.xticks((y_pos + bar_width/2), objects)
    plt.ylabel(unit)

    # If label for x-axis is needed
    if object_label != '':
        plt.xlabel(object_label)
    plt.title(title)
    plt.legend()
    
    
    # Save the figure
    plt.savefig(filename, bbox_inches = 'tight', pad_inches = 0)
    # Show the figure
    plt.show()

# GTX, RTX, MS, Yme, DGX-2
objects = ('GeForce\nGTX 980', 'Titan RTX', 'Tesla V100\n-SXM2\n16GB', 'Tesla V100\n-SXM2\n32GB', 'Tesla V100\n-SXM3\n32GB')
values = (4930.92, 18201.8, 15577.05, 15572.4, 16233.625)
#bar_chart_standard(objects, values, 'Single GPU comparison: MaxFlops SP', 'Performance (GFLOPS)', 'single-gpus-maxflops-sp.svg')

values = (157.2295, 550.2165, 7819.33, 7829.61, 8146.35)
#bar_chart_standard(objects, values, 'Single GPU comparison: MaxFlops DP', 'Performance (GFLOPS)', 'single-gpus-maxflops-dp.svg')

valuesTC = (471997, 58032, 37499, 40241, 42775)
valuesNoTC = (471997, 134574, 151428, 152053, 126962)
#bar_chart_double(objects, valuesNoTC, valuesTC, 'GEMM Training, float (7680, 48000, 2560, 0, 0)', 'Time (μs)', 'gemm-train-float-tc1.svg')

valuesTC = (53839, 14454, 16465, 16923, 15526)
valuesNoTC = (53839, 14511, 16661, 17107, 15567)
#bar_chart_double(objects, valuesNoTC, valuesTC, 'GEMM Training, float (7680, 5481, 2560, 0, 1)', 'Time (μs)', 'gemm-train-float-tc2.svg')

#valuesTC = (6900850, 989745, 549132, 571522, 712240)
#valuesNoTC = (6900850, 1962075, 2073169, 2110709, 1838153)
valuesTC = (6.900850, 0.989745, 0.549132, 0.571522, 0.712240)
valuesNoTC = (6.900850, 1.962075, 2.073169, 2.110709, 1.838153)
#bar_chart_double(objects, valuesNoTC, valuesTC, 'GEMM Training, float (average of 75 operations)', 'Time (s)', 'gemm-train-float-avg.svg', '', 0, 3)

valuesTC = (507148, 76187, 43319, 45215, 50535)
valuesNoTC = (507148, 143524, 148805, 153695, 135458)
#bar_chart_double(objects, valuesNoTC, valuesTC, 'GEMM Inference, float (average of 160 operations)', 'Time (μs)', 'gemm-infer-float-avg.svg', '', 0, 250000)

# RTX, MS, Yme, DGX-2
objects = ('Titan RTX', 'Tesla V100\n-SXM2\n16GB', 'Tesla V100\n-SXM2\n32GB', 'Tesla V100\n-SXM3\n32GB')
valuesTC = (5896, 13964, 14083, 13052)
valuesNoTC = (10953, 13950, 14068, 13058)
#bar_chart_double(objects, valuesNoTC, valuesTC, 'Convolutions Inference, INT8 (average of 107 operations)', 'Time (μs)', 'conv-infer-int8-avg.svg', '', 0, 18000)

valuesTC = (52497, 58446, 59389, 57898)
valuesNoTC = (52511, 58451, 59324, 57899)
#bar_chart_double(objects, valuesNoTC, valuesTC, 'GEMM Inference, INT8 (average of 75 operations)', 'Time (μs)', 'gemm-infer-int8-avg.svg', '', 0, 73000)

values = (0.45399411337, 0.26487565654, 0.2707725224, 0.38747590652)
bar_chart_standard(objects, values, 'GEMM Training, float', 'Percentage (%)', 'gemm-percent.svg')

values = (0.38747590652, 1, 1, 1)
bar_chart_standard(objects, values, 'Convolutions Interference, INT8', 'Percentage (%)', 'conv-percent.svg')


# Systems
objects = ('Power AC922\n(Mini Summit)', 'Power AC922\n(Yme)', 'DGX-2\n(Heid)')
values = (57.09825, 55.01705, 11.86665)
#bar_chart_standard(objects, values, 'CPU - 1 GPU: Bus speed download', 'Bandwidth (GB/s)', 'ibm-dgx-busspeeddownload.svg')

values = (54.1087, 53.777925, 13.1497)
#bar_chart_standard(objects, values, 'CPU - 1 GPU: Bus speed readback', 'Bandwidth (GB/s)', 'ibm-dgx-busspeedreadback.svg')

#objects = ('0, 1, 2, 3', '0, 1, 14, 15')
#values = ()
#bar_chart_standard(objects, values, 'CPU - 1 GPU: Bus speed readback', 'Bandwidth (GB/s)', 'ibm-dgx-busspeedreadback.svg', 'GPU IDs')