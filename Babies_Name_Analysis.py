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

# Understanding that in the Region table, a specific or more States are not listed in the Region table
df.iloc[[275663,  275664,  275665,  275666,  275667,  275668,  275669,  275670,
        275671,  275672]]

# Grouping by to check if the null values are only in the MI state
# They actually are only in MI 
df.groupby("State")["Name"].count()
# Created a variable to identify the null values
nullValues = df["Region"].isnull()
# Replacing the NULL values for the text "midwest" within the Region column
df.loc[nullValues, "Region"] = "Midwest"



