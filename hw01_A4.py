import hw01_preprocess as pp
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


# Plot cdf and its confidence intervals of the same variable from 5 sensors
# and output the confidence intervals in a csv file
def cdf_ci(list_data, column_name, confidence_rate):
    list_order = ["(a) ", "(b) ", "(c) ", "(d) ", "(e) "]
    # The way the serial Numbers are generated needs to be changed，
    # if more than 5 sets of data are input.
    list_column = pp.extract_column_name(list_data, column_name)
    fig = plt.figure(figsize=(60, 40))
    column_num = 3
    df_column = ["sensor name", "variable name", "lower limit", "upper limit"]
    ci_boundary = pd.DataFrame(columns=df_column)
    if len(list_column) % column_num != 0:
        rows_num = len(list_column) // column_num + 1
    else:
        rows_num = len(list_column) // column_num
    for i in range(len(list_column)):
        fig.add_subplot(rows_num, column_num, i + 1)
        mean = np.mean(list_column[i])
        std = np.std(list_column[i])
        interval = stats.norm.interval(confidence_rate, mean, std)
        a1 = plt.hist(x=list_column[i], bins=pp.rice_rule(list_column[i]), density=True,
                      cumulative=True, color='w', alpha=0.7, rwidth=0.85)
        plt.plot(a1[1][1:] - (a1[1][1:] - a1[1][:-1]) / 2, a1[0], label="CDF",
                 color="darkseagreen", lw=8)
        plt.axvline(interval[0], 0, 1, linewidth=8, color="salmon", linestyle=":",
                    label="{}% CI".format(confidence_rate * 100))
        plt.axvline(interval[1], 1, 0, linewidth=8, color="salmon", linestyle=":")
        plt.legend(loc='lower right', fontsize=30)
        plt.title(list_order[i] + list_data[i][:8], fontsize=50)
        plt.xticks(fontsize=50)
        plt.yticks(fontsize=50)
        plt.ylim(min(a1[0]), 1)
        plt.xlabel(column_name, fontsize=50)
        ci_boundary = ci_boundary.append(pd.DataFrame([[list_data[i][:9], column_name, interval[0], interval[1]]],
                                         columns=df_column), ignore_index=True)
    plt.show()
    return ci_boundary


def multi_pd_2_csv(csv_name, *pd_objects):
    pd_files = pd_objects[0]
    for i in pd_objects[1:]:
        pd_files = pd_files.append(i, ignore_index=True)
    pd_files.to_csv('{}.csv'.format(csv_name))


sensor_name = ["HEAT - " + i + "_final.csv" for i in "ABCDE"]
multi_pd_2_csv("confidence_intervals",
               cdf_ci(sensor_name, "Temperature", 0.95),
               cdf_ci(sensor_name, "Wind Speed", 0.95))