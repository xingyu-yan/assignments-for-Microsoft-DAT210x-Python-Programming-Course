import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#
# .. your code here ..
df = pd.read_csv('census.csv',sep=',')
df.columns=['education', 'age', 'capital_gain', 'race', 'capital_loss', 
            'hours_per_week', 'sex', 'classification']
#print(df.head(4))
print(df.dtypes)

#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# .. your code here ..
df.dtypes
#Out[55]: 
#education         object
#age                int64
#capital_gain      object
#race              object
#capital_loss       int64
#hours_per_week     int64
#sex               object
#classification    object

df.capital_gain.unique()
#Out[57]: array(['2174', '?', '0', ..., '2387', '6723', '5060'], dtype=object)

#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?
#
# .. your code here ..
df = pd.get_dummies(df,columns=['race'])
df = pd.get_dummies(df,columns=['sex'])


#
# TODO:
# Print out your dataframe
#
# .. your code here ..
print(df)

