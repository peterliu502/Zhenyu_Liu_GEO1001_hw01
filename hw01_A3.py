import hw01_preprocess as pp
from scipy import stats
import matplotlib.pyplot as plt


def correlations(list_data, column_name):
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(100, 40))
    n = 1
    for elm1 in range(len(list_column))[:-1]:
        for elm2 in range(len(list_column))[elm1 + 1:]:
            elm1_normed = pp.normalize(list_column[elm1])
            elm2_normed = pp.normalize(list_column[elm2])
            elm1_normed_matched = pp.length_match(elm1_normed, elm2_normed)
            print("Spearmann," + list_data[elm1] +
                  "," + list_data[elm2] +
                  "," + str(stats.spearmanr(elm1_normed_matched, elm2_normed)[0]))
            print("Pearson," + list_data[elm1] +
                  "," + list_data[elm2] +
                  "," + str(stats.pearsonr(elm1_normed_matched, elm2_normed)[0]))
            fig.add_subplot(5, 2, n)
            n += 1
            plt.scatter(elm1_normed_matched, elm2_normed, c='salmon')
            plt.xticks(fontsize=50)
            plt.yticks(fontsize=50)
            plt.xlabel(list_data[elm1][:9], fontsize=50)
            plt.ylabel(list_data[elm2][:9], fontsize=50)
    plt.show()


sensor_name = ["HEAT - " + i + "_final.csv" for i in "ABCDE"]
correlations(sensor_name, "Temperature")
# correlations(sensor_name, "WBGT")
# correlations(sensor_name, "Crosswind Speed")