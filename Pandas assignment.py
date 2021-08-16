#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as np


# In[93]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# # Question1 Answer
__1. Some values in the the FlightNumber column are missing. These numbers are
meant to increase by 10 with each row so 10055 and 10075 need to be put in
place. Fill in these missing numbers and make the column an integer column
(instead of a float column).__
# In[72]:


df


# In[73]:


#df.at[1,"FlightNumber"] = 10055


# In[74]:


df.loc[1,"FlightNumber"] = 10055


# In[75]:


df


# In[76]:


#df.at[3,"FlightNumber"] = 10075


# In[77]:


df.loc[3,"FlightNumber"] = 10075


# In[78]:


# Atlsat  we did it

df


# In[79]:


df.dtypes


# In[80]:


# Converting float64 dtype to int32
df["FlightNumber"] = df["FlightNumber"].astype(int)


# In[81]:


df.dtypes


# In[82]:


df


# # Question 2
# Question2
2. The From_To column would be better as two separate columns! Split each
string on the underscore delimiter _ to give a new temporary DataFrame with
the correct values. Assign the correct column names to this temporary
DataFrame.
# In[97]:


#Creating temporary Dataframe
df1 = df.copy()


# In[98]:


df1


# In[101]:


# Spliting one column into two columns
df1[["From","To"]] = df1.From_To.str.split("_",expand = True)


# In[102]:


# Temproary dataframe with new splited columns
df1


# In[ ]:




