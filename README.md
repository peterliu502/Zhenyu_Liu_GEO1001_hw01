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
  Append multiple Dataframe in one Dataframe.  
  
* [![hw01_A1](https://img.shields.io/badge/Python_file-hw01__A1-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A1.py)  
This file contains functions used to solve questions in `exercise A1`.  

* [![hw01_A2](https://img.shields.io/badge/Python_file-hw01__A2-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A2.py)  
This file contains functions used to solve questions in `exercise A2`.  

* [![hw01_A3](https://img.shields.io/badge/Python_file-hw01__A3-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A3.py)  
This file contains functions used to solve questions in `exercise A3`.  

* [![hw01_A4](https://img.shields.io/badge/Python_file-hw01__A4-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_A4.py)  
This file contains functions used to solve questions in `exercise A4`.  

* [![hw01_BQ](https://img.shields.io/badge/Python_file-hw01__BQ-yellow)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/hw01_BQ.py)  
This file contains functions used to solve `bonus question`.  

## Other Files  
A brief introduction to each non-Python file. 
Click the icons to jump to the corresponding folders, files and code.  

* [![README.md](https://img.shields.io/badge/other_file-READ.md-yellowgreen)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/README.md)  
This file describes the basic information of repository `Zhenyu_Liu_GEO1001_hw01`.

* [![confidence_intervals.csv](https://img.shields.io/badge/other_file-confidence__intervals.csv-yellowgreen)](https://github.com/peterliu502/Zhenyu_Liu_GEO1001_hw01/blob/master/confidence_intervals.csv)  
This file records the confidence intervals information (upper limits and lower limits) of CDF of `Temperature` and `Wind Speed` data from 5 sensors.  

* Analysis report  

* Latex source file  

* Source data  