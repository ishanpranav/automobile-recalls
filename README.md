# Automobile recalls

This is a demonstration of Python features (classes, magic methods, iterators,
list comprehensions, and lambda functions) for the NYU CSCI 479 Data Management
and Analysis course.

## Highest and lowest potentially affected vehicles

This is a simple Jupyter Notebook that illustrates comprehensions and
manipulation of tabular data relating to automobile recalls.

## `nelta`

This is a data table data structures library that includes `LabeledList` and
`Table` implementations with support for `numpy`-style indexing.

## Recalls potentially affecting at least 500,000 vehicles

This section of the Jupyter notebook leverages `nelta` and composes its features
to flexibly and easily manipulate tabular data.

## Constraints

The following constraints are imposed on the implementation:

* must use at least four list comprehensions:
  * [nelta.py:64](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L64)
  * [nelta.py:82](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L82)
  * [nelta.py:86](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L86)
  * [nelta.py:90](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L90)
  * [nelta.py:94](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L94)
  * [nelta.py:97](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L97)
  * [nelta.py:119](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L119)
  * [nelta.py:170](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L170)
  * [nelta.py:192](https://github.com/nyu-csci-ua-0479-001-spring-2025/homework02-ishanpranav/blob/ab5bfb6272ca8642c8d08640d7d97b458b5106e0/nelta.py#L192)
* must use at least two lambda expressions: see [recall.ipynb](recall.ipynb)

## License

This repository is licensed with the [MIT](LICENSE.txt) license.

## Attribution

The data for this project come from
[Michael Bryant's automobile recalls dataset](https://www.kaggle.com/datasets/michaelbryantds/automobile-recalls-dataset). We use a modified dataset:

* some columns have been removed,
* some column names have been changed,
* some rows have been removed due to non numeric values in numeric columns, and
* some rows have been removed to consider only subset of the data.
