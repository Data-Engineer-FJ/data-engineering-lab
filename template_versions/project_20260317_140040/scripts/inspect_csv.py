import pandas as pd
import sys

file = sys.argv[1]

df = pd.read_csv(file)

print("\nPreview:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nNull values:")
print(df.isnull().sum())