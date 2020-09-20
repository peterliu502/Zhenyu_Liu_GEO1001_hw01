import pandas as pd
import hw01_preprocess as pp


sensor_name = ["HEAT - " + i + "_final.csv" for i in "ABCDE"]

# Extract the "date" field from the "FORMATTED DATE-TIME" field, and output in a list.
def list_of_date(list_time):
    list_date = []
    for i in range(len(list_time)):
        for row in range(len(list_time[i])):
            new_date = ""
            n = 0
            while list_time[i][row][n] != " ":
                new_date += list_time[i][row][n]
                n += 1
            list_date.append(new_date)
    return list_date


# Output the date which the variable has an extreme value
def date_of_extremum(list_data, column_name):
    list_time = pp.extract_column_name(list_data, "FORMATTED DATE-TIME")
    list_variable_appended = pp.append_multi_pd(*pp.extract_column_name(list_data, column_name))
    data_temp = pd.DataFrame(columns=["date", column_name])
    data_temp_mean = pd.DataFrame(columns=["date", "Mean " + column_name])
    list_of_date_sum = list_of_date(list_time)
    data_temp["date"] = list_of_date_sum
    data_temp[column_name] = list_variable_appended
    list_of_date_uni_sorted = sorted(set(list_of_date_sum), key=list_of_date_sum.index)
    for new_date in list_of_date_uni_sorted:
        data_temp_1day = data_temp[data_temp["date"] == new_date]
        data_temp_mean = data_temp_mean.append(pd.DataFrame([[new_date, data_temp_1day[column_name].mean()]],
                                               columns=["date", "Mean " + column_name]), ignore_index=True)
    # print(data_temp_mean)
    temp_max = data_temp_mean["Mean " + column_name].max()
    temp_max_date = data_temp_mean[data_temp_mean["Mean " + column_name] == temp_max]["date"]
    temp_min = data_temp_mean["Mean " + column_name].min()
    temp_min_date = data_temp_mean[data_temp_mean["Mean " + column_name] == temp_min]["date"]
    print("The hottest day is {0}, its mean temperature is {1}°C.".format(temp_max_date.values[0], temp_max))
    print("The coldest day is {0}, its mean temperature is {1}°C.".format(temp_min_date.values[0], temp_min))




