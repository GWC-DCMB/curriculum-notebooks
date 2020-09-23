# Reference Sheet

## Day 1

### Lesson02_HelloWorld_Variables

* Use built-in Python functions (`print`).
* Use mathematical operators to perform calculations (`+ - * /`).
* Assign values to variables.
* Use variables in mathematical equations.

### Lesson03_Variables_Types

* The `type` function.
* The basic Python data types: `int`, `float`, `string`, and `bool`.
* How to convert between different data types.

### Lesson04_Lists_Intro

* Make a list (`[]`).
* Find the length of a list (`len`).
* Add lists together (`+`).
* Add things to a list (`.append`).

### Lesson05_Indexing

* Get an element from a list or string.
* Get multiple elements from a list or string.

### Lesson06_2D_Lists

* How to make 2D lists.

### Lesson07_2D_Lists_Indexing

* How to index 2D lists.

## Day 2

### Lesson08_Functions_and_Methods

* What functions and methods do.
* The difference between functions and methods.
* How to learn more about a certain function or method (using the `help` function).
* New functions: `max`, `min`, `sum`, `abs`, `round`.
* Functions can take arguments that modify the output.

### Lesson09_Packages

* How to import new functions in packages in Python, such as `numpy`.
* More functions and methods:
    * `mean` (in `numpy`)
    * `abs` (in `numpy`)
    * `sort`

### Lesson10_Pandas-Intro

* How to import the `pandas` package with the nickname `pd`.
* How to use `DataFrames`.
* How to see the beginning & end of a `DataFrame` with the functions `head` & `tail`.

### Lesson11_Pandas-Reading

* How to read datasets from files into `pandas` `DataFrames`.
* The `index` and `columns` `attributes` of `DataFrames`.
* How to find the number of rows, columns, and number of data points in a `DataFrame`.

### Lesson12_Pandas-Subsetting

* How to use square brackets to subset columns.
* How to use `iloc` to subset rows.
* How to use `iloc` and square brackets at the same time.
* How to use `query` to find rows where the column has a certain value.

## Day 3

### Lesson13_Numpy_Intro

* Create an `array` with `numpy`.
* Perform math with `numpy` arrays.

### Lesson14_Basic_Stats_I

* Calculate the mean of a set of values manually.
* Use functions in `numpy` to calculate both the `mean` and `median`.

### Lesson15_Basic_Stats_II

* Calculate count statistics using `collections.Counter`.
* Calculate percentages from count statistics.

### Lesson16_Basics_Stats_III

* Perform a t-test on a two-class dataset using `ttest_ind` from `scipy.stats`.
* Interpret the results (`pvalue`) from a t-test.
* Compute correlations for multiple variables using `corrcoef` from `scipy.stats`.

## Day 4

### Lesson17B_LineGraphs

* Use the `seaborn` package with the nickname `sns`.
* Load built-in datasets from `seaborn` with the `load_dataset` function.
* Create a line plot with the `lineplot` function from `seaborn`.
* Change the `hue` and `style` of lines based on categorical variables.

### Lesson18B_Scatterplots

* Create a scatter plot with the `scatterplot` function from `seaborn`.
* Create a scatter plot with a line-of-best-fit with the `lmplot` function from `seaborn`.
* Change the `hue`, `style`, and `palette` of a plot.

### Lesson19B_BarCharts_Histograms

* Create a bar plot with the `barplot` function from `seaborn`.
* Remove missing values from data frames with the `dropna` function.
* Create a histogram for continuous variables with the `distplot` function from `seaborn`.
* Create a count plot for categorical variables with the `countplot` function from `seaborn`.
