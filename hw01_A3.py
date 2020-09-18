import hw01_preprocess as pp
from scipy import stats
import matplotlib.pyplot as plt


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


sensor_name = ["HEAT - " + i + "_final.csv" for i in "ABCDE"]
correlations(sensor_name, "Temperature")
