# import csv
import pandas as pd
# import numpy
# import sklearn
# from sklearn import preprocessing

df = pd.read_csv('../data/tracks2020.csv', encoding='windows-1252')
pd.set_option('display.max_columns', None)
print(df)