# Data exploratory with PYTHON and PANDAS.

#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a data frame for the name table
names = pd.read_csv("names.csv")
region = pd.read_csv("regions.csv")

names.head(5)

region.head(5)

#joining the region table to the names tables
df = names.merge(region, on="State", how="left")

df.head(5)

df.dtypes

df.shape

# Checking for any null values in the table
# Region has a lot of null values
df.isnull().sum()

df["Region"].isnull()

# To show which rows (indexes) are the null values
df[df["Region"].isnull()].index

# Understanding about the Region table, if a specific or more States are not listed in the Region table
df.iloc[[275663,  275664,  275665,  275666,  275667,  275668,  275669,  275670,
        275671,  275672]]

# Grouping by to check if the null values are only in the MI state
# They actually are only in the MI state, in the Region table, it was not listed.
df.groupby("State")["Name"].count()
# Created a variable to identify the null values
nullValues = df["Region"].isnull()
# Replacing the NULL values for the text "midwest" within the Region column
# No need to create a new DF, once this code below already applies it in the DF.
df.loc[nullValues, "Region"] = "Midwest"

# Checking for duplicated values within the DF
# No duplicated vales
df.duplicated()
df.duplicated().value_counts()

# Separating the Year that has the max number os Births
df.groupby(["Year"])["Births"].max()

# Grouping by Year, to filter the top names of each year.
# Get the index of the max births for each year
idx = df.groupby("Year")["Births"].idxmax()
# Filter rows where Births match the max for that year
df.loc[idx, ["Year", "Name", "Births"]].reset_index(drop=True

