import hw01_preprocess as pp
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Plot pmf of the same variable from 5 sensors
def pmf_plot(list_data, column_name):
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(20, 20))
    ax1 = fig.add_subplot(111)
    count = [i.value_counts() for i in list_column]
    probability = [count[i] / len(list_column[i]) for i in range(len(list_column))]
    data = [probability[i].sort_index() for i in range(len(probability))]
    bins = np.histogram(list_column[0], bins=pp.rice_rule(data[0]))[1]
    bins_0 = [(bins[i] + bins[i + 1]) / 2 for i in range(len(bins) - 1)]
    total_width, n = 1.8, len(list_data)
    width = total_width / n
    for i in range(len(data)):
        bins_i = [bins_0[elm] + i * width for elm in range(len(bins_0))]
        frequency_i = np.histogram(list_column[i], bins=pp.rice_rule(data[0]))[0]
        frequency_i = [elm / len(list_column[i]) for elm in frequency_i]
        ax1.bar(bins_i, frequency_i, width=width, label=list_data[i],
                color=["burlywood", "salmon", "yellowgreen", "cadetblue", "darkseagreen"][i])
    ax1.legend(loc='upper right', fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)
    plt.show()


# Plot pdf of the same variable from 5 sensors
def pdf_plot(list_data, column_name):
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(20, 20))
    ax1 = fig.add_subplot(111)
    for i in range(len(list_column)):
        sns.distplot(list_column[i], bins=pp.rice_rule(list_column[i]), label=list_data[i], hist=False,
                     color=["burlywood", "salmon", "yellowgreen", "cadetblue", "darkseagreen"][i],)
    ax1.legend(loc='upper right', fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)
    plt.show()


# Plot cdf of the same variable from 5 sensors
def cdf_plot(list_data, column_name):
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(20, 20))
    ax1 = fig.add_subplot(111)
    for i in range(len(list_column)):
        a1 = ax1.hist(x=list_column[i], bins=pp.rice_rule(list_column[i]), density=True,
                      cumulative=True, color='w', alpha=0.7, rwidth=0.85)
        ax1.plot(a1[1][1:] - (a1[1][1:] - a1[1][:-1]) / 2, a1[0], label=list_data[i],
                 color=["burlywood", "salmon", "yellowgreen", "cadetblue", "darkseagreen"][i])
    ax1.legend(loc='lower right', fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)
    plt.show()


sensor_name = ["HEAT - " + i + "_final.csv" for i in "ABCDE"]
pdf_plot(sensor_name, "Temperature")
