import numpy as np
import matplotlib.pyplot as plt
import hw01_preprocess as pp


# Compute mean statistics (mean, variance and standard deviation for specified column of the data)
def mean_statistics(data):
    df = pp.read_source_file(data)
    for column_name in list(df)[1:]:
        data_mean = df[column_name].mean()
        data_var = df[column_name].var()
        data_std = df[column_name].std()
        print("[{0}]-[{1}]-[mean]:{2}".format(data, column_name, data_mean))
        print("[{0}]-[{1}]-[variance]:{2}".format(data, column_name, data_var))
        print("[{0}]-[{1}]-[standard deviation]:{2}".format(data, column_name, data_std))


# Plot the same variable from 5 sensors in a mulit-hist graph
def multi_hist(list_data, column_name, bar_num1):
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(40, 10))
    ax1 = fig.add_subplot(111)
    ax1.hist(list_column, bar_num1, histtype='bar',
             color=["burlywood", "salmon", "yellowgreen", "cadetblue", "darkseagreen"],
             label=list_data)
    ax1.legend(loc='upper right', fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)
    plt.ylabel("frequency", fontsize=50)
    plt.show()


# Plot the same variable from 5 sensors in a frequency polygon
def freq_polygons(list_data, column_name):
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(40, 10))
    ax1 = fig.add_subplot(111)
    for i in range(len(list_column)):
        [frequency, bins] = np.histogram(list_column[i], bins=pp.rice_rule(list_column[i]))
        ax1.plot(bins[1:] - (bins[1:] - bins[:-1]) / 2, frequency, antialiased=True, label=list_data[i],
                 lw=8, ls=':', color=["burlywood", "salmon", "yellowgreen", "cadetblue", "darkseagreen"][i])
    ax1.legend(loc='upper right', fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)
    plt.ylabel("frequency", fontsize=50)
    plt.show()


# Plot the same variable from 5 sensors in a frequency polygon
def boxplot(list_data, column_name):
    list_column = pp.extract_column_name(list_data, column_name)
    list_name = [i[:8] for i in list_data]
    fig = plt.figure(figsize=(20, 20))
    ax1 = fig.add_subplot(111)
    ax1.boxplot(list_column, patch_artist=True, labels=list_name, meanprops={"linewidth": 8},
                boxprops={'color': 'salmon', "linewidth": 8, 'facecolor': 'cadetblue'})
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel("sensor name", fontsize=50)
    plt.ylabel(column_name, fontsize=50)
    plt.show()
