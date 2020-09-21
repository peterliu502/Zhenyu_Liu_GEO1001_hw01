# Zhenyu_Liu_GEO1001_hw01
***
[![hw01 repository](https://img.shields.io/badge/repository-Zhenyu__Liu__GEO1001__hw01-orange)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01)  


This is Zhenyu Liu's file repository for `GEO1001-hw01`.  
  
  
## Table of Contents  

- [Author](#author)  
- [Abstract](#abstract)  
- [Runtime Environment](#runtime-environment)
- [Python Files](#python-files)  
- [Other Files](#other-files)  

## Auther

[<img src="https://avatars3.githubusercontent.com/u/59593272?s=400&u=ba1618be6d5e354f0bd7685ff405bdec6d18c101&v=4" width = "50" height = "50" />](https://github.com/peterliu502)

[@ Zhenyu Liu(5386586)](https://github.com/peterliu502)
 
## Abstract  

This repository contains:  

1. The Python files used to solve the problems in [hw01](https://3d.bk.tudelft.nl/courses/geo1001/hw/01/).  
2. The output file of `exercise A4`.
3. The source data used for this assignment.  
4. Analysis report of this assignment and its Latex source files.  
5. The `README.md` files of this repository.  

## Runtime Environment  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1920px-Windows_logo_-_2012_derivative.svg.png" width = "50" height = "50" />  

Operating System: Windows10 64 - bit.  

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/PyCharm_Logo.svg/1200px-PyCharm_Logo.svg.png" width = "50" height = "50" />  
  
IDE：[Pycharm](https://www.jetbrains.com/pycharm/).   
  
<img src="https://camo.githubusercontent.com/91de473fa3f2f749a56effc3e64f1049d108251f/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f632f63332f507974686f6e2d6c6f676f2d6e6f746578742e7376672f37363870782d507974686f6e2d6c6f676f2d6e6f746578742e7376672e706e67" width = "50" height = "50" />  

[Python](https://www.python.org/downloads/release/python-385/) version: 3.8.  

## Python Files  
A brief introduction to each Python file. Click the icons to jump to the corresponding files and code.

* [![geo1001_hw01](https://img.shields.io/badge/Python_file-geo1001__hw01-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/geo1001_hw01.py)  
This file contains the `author's name`, `student number`, and the final `answer code` for `assignment 1`.  
Tip: Computer need enough memory to run the entire code.If you're running on a computer with less memory, 
comment out some of the code and run it in batches.  

* [![hw01_preprocess](https://img.shields.io/badge/Python_file-hw01__preprocess-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_preprocess.py)  
This file contains functions used to preprocess data.
  
  * [![read_source_file()](https://img.shields.io/badge/function-read__source__file()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_preprocess.py#L5)  
  Read source data from csv file and delete rows contian nan data.  
  
  * [![length_match()](https://img.shields.io/badge/function-length__match()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_preprocess.py#L13)  
  Match array1's length and array2's length, interpolate data from array1 to the length of array2.  
  
  * [![rice_rule()](https://img.shields.io/badge/function-rice__rule()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_preprocess.py#L20)  
  Estimate the appropriate number of bars.
  
  * [![extract_column_name()](https://img.shields.io/badge/function-extract__column__name()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_preprocess.py#L26)  
  Export the columns with the same name from the dataset.  
  
  * [![normalize()](https://img.shields.io/badge/function-normalize()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_preprocess.py#L33)  
  Normalize data.  
  
  * [![append_multi_pd()](https://img.shields.io/badge/function-append__multi__pd()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_preprocess.py#L40)  
  Append multiple Dataframe in one Dataframe.  
  
  * [![list_sensor_name()](https://img.shields.io/badge/function-list__sensor__name()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_preprocess.py#L48)  
  Create a list contains sensors' name.  
  
* [![hw01_A1](https://img.shields.io/badge/Python_file-hw01__A1-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A1.py)  
This file contains functions used to solve questions in `exercise A1`.  

  * [![mean_statistics()](https://img.shields.io/badge/function-mean__statistics()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A1.py#L6)  
  Compute mean statistics (mean, variance and standard deviation for specified column of the data).
    
  * [![multi_hist()](https://img.shields.io/badge/function-multi__hist()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A1.py#L18)  
  Plot the same variable from 5 sensors in a mulit-hist graph.  

  * [![freq_polygons()](https://img.shields.io/badge/function-freq__polygons()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A1.py#L34)  
  Plot the same variable from 5 sensors in a frequency polygon.  
  
  * [![boxplot()](https://img.shields.io/badge/function-boxplot()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A1.py#L51)  
  Plot the same variable from 5 sensors in a box plot.  

* [![hw01_A2](https://img.shields.io/badge/Python_file-hw01__A2-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A2.py)  
This file contains functions used to solve questions in `exercise A2`.    
  
  * [![pmf_plot()](https://img.shields.io/badge/function-pmf__plot()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A2.py#L7)  
  Plot pmf of the same variable from 5 sensors.  
  
  * [![pdf_plot()](https://img.shields.io/badge/function-pdf__plot()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A2.py#L32)  
  Plot pdf of the same variable from 5 sensors.  

  * [![cdf_plot()](https://img.shields.io/badge/function-cdf__plot()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A2.py#L49)  
  Plot cdf of the same variable from 5 sensors.  

  * [![pdf_and_kde()](https://img.shields.io/badge/function-pdf__and__kde()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A2.py#L66)  
  Plot pdf and kde of the same variable together from 5 sensors.  

* [![hw01_A3](https://img.shields.io/badge/Python_file-hw01__A3-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A3.py)  
This file contains functions used to solve questions in `exercise A3`.  
  
  * [![correlations()](https://img.shields.io/badge/function-correlations()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A3.py#L6)  
  Calculate the Pearson and Spearmann correlation coefficients of the same variable of each 2 sensors.  
  
  * [![mean_correlations()](https://img.shields.io/badge/function-mean__correlations()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A3.py#L40)  
  Calculate the mean Spearmann correlation coefficients of Temperature and Wet Bulb Globe Temperature (WBGT) of each 2 sensors.  
  
* [![hw01_A4](https://img.shields.io/badge/Python_file-hw01__A4-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A4.py)  
This file contains functions used to solve questions in `exercise A4`.  

  * [![cdf_ci()](https://img.shields.io/badge/function-cdf__ci()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A4.py#L8)  
  Plot cdf and its confidence intervals of the same variable from 5 sensors and output the confidence intervals in a csv file.  

  * [![multi_pd_2_csv()](https://img.shields.io/badge/function-multi__pd__2__csv()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A4.py#L55)  
  Transfer multi-pandas Dataframe files to one csv file.  

  * [![sensors_t_test()](https://img.shields.io/badge/function-sensors__t__test()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A4.py#L63)  
  Compute the T-Test for a variable between 2 sensors.  

* [![hw01_BQ](https://img.shields.io/badge/Python_file-hw01__BQ-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_BQ.py)  
This file contains functions used to solve `bonus question`.  

  * [![list_of_date()](https://img.shields.io/badge/function-list__of__date()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_BQ.py#L5)  
  Extract the "date" field from the "FORMATTED DATE-TIME" field, and output in a list.  
  
  * [![date_of_extremum()](https://img.shields.io/badge/function-date__of__extremum()-green)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_BQ.py#L19)  
  Extract the "date" field from the "FORMATTED DATE-TIME" field, and output in a list.  
  
## Other Files  
A brief introduction to each non-Python file. 
Click the icons to jump to the corresponding folders, files and code.  

* [![README.md](https://img.shields.io/badge/other_file-READ.md-yellowgreen)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/README.md)  
This file describes the basic information of repository `Zhenyu_Liu_GEO1001_hw01`.

* [![confidence_intervals.csv](https://img.shields.io/badge/other_file-confidence__intervals.csv-yellowgreen)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/confidence_intervals.csv)  
This file records the confidence intervals information (upper limits and lower limits) of CDF of Temperature and Wind Speed data from 5 sensors.  

* [![Analysis_report](https://img.shields.io/badge/other_file-Analysis_report-yellowgreen)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/%5BZhenyu%20Liu%5DTUDelft_GEO1001_hw01.pdf)    
This PDF file is the analysis report of the `assignment1`.

* [![Latex source file](https://img.shields.io/badge/other_file-Latex_source_file-yellowgreen)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/tree/master/%5BZhenyu%20Liu%5DTUDelft_GEO1001_hw01)   
This folder contains source code and raw materials of the analysis report.  
The Latex code can run and generates PDF file successfully on Overleaf.  

* [![Source data](https://img.shields.io/badge/other_file-Source_data-yellowgreen)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/tree/master/data)  
The source data of this assignment，[Source link](https://data.4tu.nl/articles/dataset/Measured_Climate_Data_in_Rijsenhout/12833918/1)   
