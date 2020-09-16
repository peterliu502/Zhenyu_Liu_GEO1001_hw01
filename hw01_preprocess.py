import pandas as pd
import numpy as np


# read source data from csv file and delete rows contian nan data
def read_source_file(filename):
    filedir = "data/"+filename
    df = pd.read_csv(filedir, skiprows=[4], header=3, parse_dates=['FORMATTED DATE-TIME'])
    df.dropna()
    return df


# match array1's length and array2's length, interpolate data from array1 to the length of array2
def length_match(array1, array2):
    return np.interp(np.linspace(0, len(array2), len(array2)),  # provide an array from 0 to len(array2), step is 1
                            np.linspace(0, len(array1), len(array1)),  # provide an array from 0 to len(array1), step is 1
                            array1)


# Estimate the appropriate number of bars
def rice_rule(array):
    bin_num = int(2 * np.power(len(array), (1 / 3)))
    return bin_num
