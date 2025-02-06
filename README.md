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

## License

This repository is licensed with the [MIT](LICENSE.txt) license.

## Attribution

The data for this project come from
[Michael Bryant's automobile recalls dataset](https://www.kaggle.com/datasets/michaelbryantds/automobile-recalls-dataset). We use a modified dataset:

* some columns have been removed,
* some column names have been changed,
* some rows have been removed due to non numeric values in numeric columns, and
* some rows have been removed to consider only subset of the data.
