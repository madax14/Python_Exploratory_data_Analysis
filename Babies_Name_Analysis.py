#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[85]:


# Creating a data frame for the name table
#names = pd.read_csv("names.csv")
region = pd.read_csv("regions.csv")


# In[10]:


names.head(5)


# In[56]:


region.head(5)


# In[86]:


#joining the region table to the names tables
df = names.merge(region, on="State", how="left")


# In[46]:


df.head(5)


# In[47]:


df.dtypes


# In[48]:


df.shape


# In[70]:


# Checking for any null values in the table
# Region has a lot of null values
df.isnull().sum()


# In[50]:


df["Region"].isnull()


# In[72]:


# To show which rows (indexes) are the null values
df[df["Region"].isnull()].index


# In[59]:


# Understanding that in the Region table, a specific or more States are not listed in the Region table
df.iloc[[275663,  275664,  275665,  275666,  275667,  275668,  275669,  275670,
        275671,  275672]]


# In[69]:


# Grouping by to check if the null values are only in the MI state
# They are only in MI 
df.groupby("State")["Name"].count()


# In[88]:


# Created a variable to identify the null values
nullValues = df["Region"].isnull()


# In[97]:


# Replacing the NULL vales for the text "midwest" within the Region column
df.loc[nullValues, "Region"] = "Midwest"


# In[98]:


df.iloc[[275663,  275664,  275665,  275666,  275667,  275668,  275669,  275670,
        275671,  275672]]

