import hw01_preprocess as pp
from scipy import stats
import matplotlib.pyplot as plt


# Calculate the Pearson and Spearmann correlation coefficients of the same variable of each 2 sensors.
def correlations(list_data, column_name):
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(60, 25))
    n = 1
    column_num = 5
    subplot_num = 0
    for i in range(len(list_column))[1:]:
        subplot_num += i
    if subplot_num % column_num != 0:
        rows_num = subplot_num // column_num + 1
    else:
        rows_num = subplot_num // column_num
    for elm1 in range(len(list_column))[:-1]:
        for elm2 in range(len(list_column))[elm1 + 1:]:
            elm1_normed = pp.normalize(list_column[elm1])
            elm2_normed = pp.normalize(list_column[elm2])
            elm1_normed_matched = pp.length_match(elm1_normed, elm2_normed)
            print("Spearmann between {0} and {1} in {2}: correlation = {3}, p-value = {4}".format(
                list_data[elm1], list_data[elm2], column_name, str(stats.spearmanr(elm1_normed_matched, elm2_normed)[0]),
            str(stats.spearmanr(elm1_normed_matched, elm2_normed)[1])))
            print("Pearson between {0} and {1} in {2}: correlation = {3}, p-value = {4}".format(
                list_data[elm1], list_data[elm2], column_name, str(stats.pearsonr(elm1_normed_matched, elm2_normed)[0]),
            str(stats.pearsonr(elm1_normed_matched, elm2_normed)[1])))
            fig.add_subplot(rows_num, column_num, n)
            n += 1
            plt.scatter(elm1_normed_matched, elm2_normed, c='salmon')
            plt.xticks(fontsize=50)
            plt.yticks(fontsize=50)
            plt.xlabel(list_data[elm1][:9], fontsize=50)
            plt.ylabel(list_data[elm2][:9], fontsize=50)
    plt.show()


# Calculate the mean Spearmann correlation coefficients of
# Temperature and Wet Bulb Globe Temperature (WBGT) of each 2 sensors.
def mean_correlations():
    list_name = ["A", "B", "C", "D", "E"]
    data_A = [1, 0.989755695, 0.990382012, 0.986459581, 0.960448668]
    data_B = [0.989755695, 1, 0.987651843, 0.986711767, 0.966880043]
    data_C = [0.990382012, 0.987651843, 1, 0.989803762, 0.963344]
    data_D = [0.986459581, 0.986711767, 0.989803762, 1, 0.962275137]
    data_E = [0.960448668, 0.966880043, 0.963344, 0.962275137, 1]

    list_data = [data_A, data_B, data_C, data_D, data_E]
    plt.figure(figsize=(20, 20))
    for elm in range(len(list_data)):
        plt.scatter(list_name, list_data[elm], label=list_name[elm], marker='o', s=300,
                    c=["burlywood", "salmon", "yellowgreen", "cadetblue", "darkseagreen"][elm])
    plt.legend(loc='upper right', fontsize=50)
    plt.ylim(0.96, 1.0005)
    plt.xticks(fontsize=50)
    plt.yticks(fontsize=50)
    plt.xlabel("sensor", fontsize=50)
    plt.ylabel("mean correlation coefficients", fontsize=50)
    plt.show()
