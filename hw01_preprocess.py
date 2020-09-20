import pandas as pd
import numpy as np


# ead source data from csv file and delete rows contian nan data
def read_source_file(filename):
    filedir = "data/"+filename
    df = pd.read_csv(filedir, skiprows=[4], header=3)
    df.dropna()
    return df


# Match array1's length and array2's length, interpolate data from array1 to the length of array2
def length_match(array1, array2):
    return np.interp(np.linspace(0, len(array2), len(array2)),  # provide an array from 0 to len(array2), step is 1
                            np.linspace(0, len(array1), len(array1)),  # provide an array from 0 to len(array1), step is 1
                            array1)


# Estimate the appropriate number of bars
def rice_rule(array):
    bin_num = int(2 * np.power(len(array), (1 / 3)))
    return bin_num


# Export the columns with the same name from the dataset
def extract_column_name(list_data, column_name):
    list_df = [read_source_file(i) for i in list_data]
    list_column = [i[column_name] for i in list_df]
    return list_column


# Normalize data
def normalize(my_array):
    my_mean = np.mean(my_array)
    my_std = np.std(my_array)
    return (my_array - my_mean) / my_std


# Append multiple Dataframe in one Dataframe
def append_multi_pd(*pd_objects):
    pd_files = pd_objects[0]
    for i in pd_objects[1:]:
        pd_files = pd_files.append(i, ignore_index=True)
    return pd_files


# Create a list contains sensors' name
def list_sensor_name(name):
    return ["HEAT - " + i + "_final.csv" for i in name]