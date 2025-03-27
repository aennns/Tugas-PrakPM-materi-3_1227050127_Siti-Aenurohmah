#%%
import pandas as pd

#%%
# Reading the database
data = pd.read_csv("students.csv")

#%%
# Printing the top 10 rows
display(data.head(10))

#%%
# Show the dataset info
data.info()

#%%
# Missing Value Checking
data.isna().sum()

#%%
# Filling Nan Value with mode
data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)

#%%
# Filling Nan Value with mean
data['reading score'].fillna(data['reading score'].mean(), inplace=True)

#%%
# Filling Nan Value with median
data['grade'].fillna(data['grade'].median(), inplace=True)

#%%
# Check the information of the dataset
data.info()

#%%
# Interpolate the Missing Value
data['lunch'].interpolate(method='linear', inplace=True)

#%%
# Backward fill the missing value
data['gender'].fillna(method='bfill', inplace=True)

#%%
# Forward fill the missing value
data['gender'].fillna(method='ffill', inplace=True)

#%%
# Drop NaN Value
data.dropna(subset=['lunch'], inplace=True)

#%%
# Drop feature with more than 50% NaN values
data.drop('lunch', axis=1, inplace=True)
