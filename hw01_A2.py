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


# Plot pdf and kde of the same variable together from 5 sensors
def pdf_and_kde(list_data, column_name):
    list_order = ["(a) ", "(b) ", "(c) ", "(d) ", "(e) "]
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(60, 40))
    ax0 = fig.add_subplot(231)
    sns.distplot(list_column[0], bins=pp.rice_rule(list_column[0]), kde=True, kde_kws={"linewidth": 5, "label": "KDE"},
                 hist=True, hist_kws={"histtype": "step", "linewidth": 5, "color": "salmon", "label": "PDF"},
                 color="cadetblue")
    ax0.legend(loc='upper right', fontsize=50)
    ax0.set_title(list_order[0]+list_data[0][:9], fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)

    ax1 = fig.add_subplot(232)
    sns.distplot(list_column[1], bins=pp.rice_rule(list_column[1]), kde=True, kde_kws={"linewidth": 5, "label": "KDE"},
                 hist=True, hist_kws={"histtype": "step", "linewidth": 5, "color": "salmon", "label": "PDF"},
                 color="cadetblue")
    ax1.legend(loc='upper right', fontsize=50)
    ax1.set_title(list_order[1]+list_data[1][:9], fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)

    ax2 = fig.add_subplot(233)
    sns.distplot(list_column[2], bins=pp.rice_rule(list_column[2]), kde=True, kde_kws={"linewidth": 5, "label": "KDE"},
                 hist=True, hist_kws={"histtype": "step", "linewidth": 5, "color": "salmon", "label": "PDF"},
                 color="cadetblue")
    ax2.legend(loc='upper right', fontsize=50)
    ax2.set_title(list_order[2] + list_data[2][:9], fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)

    ax3 = fig.add_subplot(234)
    sns.distplot(list_column[3], bins=pp.rice_rule(list_column[3]), kde=True, kde_kws={"linewidth": 5, "label": "KDE"},
                 hist=True, hist_kws={"histtype": "step", "linewidth": 5, "color": "salmon", "label": "PDF"},
                 color="cadetblue")
    ax3.legend(loc='upper right', fontsize=50)
    ax3.set_title(list_order[3] + list_data[3][:9], fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)

    ax4 = fig.add_subplot(235)
    sns.distplot(list_column[4], bins=pp.rice_rule(list_column[4]), kde=True, kde_kws={"linewidth": 5, "label": "KDE"},
                 hist=True, hist_kws={"histtype": "step", "linewidth": 5, "color": "salmon", "label": "PDF"},
                 color="cadetblue")
    ax4.legend(loc='upper right', fontsize=50)
    ax4.set_title(list_order[4] + list_data[4][:9], fontsize=50)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel(column_name, fontsize=50)

    plt.show()
