#!/usr/bin/env python
# coding: utf-8

# WORLD COVID-19 LIVE DATA ANALYSED BY IKEJIOFOR OKWUCHUKWU.M

# Steps involved;<br>
# 1) data collection<br>
# 2) data cleaning<br>
# 3) data manipulation<br>
# 4) data exploration<br>
# 5) data visualisation<br>

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[41]:


# importing the data
df = pd.read_csv(r"C:\Users\HP\Downloads\archive\Covid Live.csv")
df


# In[3]:


# looking at the data there are alot of missing values,
# but not all columns missing values will be dropped, 
#for instance not every country must have critical cases therefore we can fill  those ones with zero
# i want to work with rate of the entire population since some countries are not upto 1million by population
# therefore the per million populataion columns are not relevant to this analysis
df.drop(columns=["#","Tot Cases1pop","Tests1Mpop","Deaths1Mpop"],inplace=True)
df.dropna(inplace=True)
df
                 


# In[4]:


#data exploration
df.info()


# In[42]:


# removing "," from the numbers and converting the number columns which are present as string to float through casting
df["TotalCases"]  = df["TotalCases"].str.replace(",","",regex=False).astype(str).astype(float)
df["TotalDeaths"] = df["TotalDeaths"].str.replace(",","",regex=False).astype(str).astype(float)
df["TotalRecovered"] = df["TotalRecovered"].str.replace(",","",regex=False).astype(str).astype(float)
df["ActiveCases"] = df["ActiveCases"].str.replace(",","",regex=False).astype(str).astype(float)
df["Critical"] = df["Critical"].str.replace(",","",regex=False).astype(str).astype(float)
df["TotalTests"] = df["TotalTests"].str.replace(",","",regex=False).astype(str).astype(float)
df["Population"] = df["Population"].str.replace(",","",regex=False).astype(str).astype(float)

df.head()


# In[43]:


# getting the rate of each column
df["DeathRate"] = df["TotalDeaths"]/ df["TotalCases"]
df["InfectionRate"] = df["TotalCases"]/ df["Population"]
df["RecoveryRate"] = df["TotalRecovered"]/ df["TotalCases"]
df["CriticalCaseRate"] = df["Critical"]/ df["TotalCases"]
df.tail()


# In[7]:


df.describe()


# indepth exploratory data analysis(EDA) begins

# In[45]:


# ploting a histogram of the infection rate
plt.hist(df["InfectionRate"])
plt.xlabel("InfectionRate")
plt.ylabel("frequency")
plt.title("distribution of infectuion rate");


# In[46]:


# ploting a histogram for the death rate
plt.hist(df["DeathRate"])
plt.xlabel("DeathRate")
plt.ylabel("frequency")
plt.title("distribution of Death Rate");


# In[47]:


# ploting a histogram for the recovery rate
plt.hist(df["RecoveryRate"])
plt.xlabel("Recovery Rate")
plt.ylabel("frequency")
plt.title("distribution of Recovery Rate");


# In[48]:


# PLOTING A HISTOGRAM FOR THE CRITICAL CASES RATE
plt.hist(df["CriticalCaseRate"])
plt.xlabel("CriticalCaseRate")
plt.ylabel("frequency")
plt.title("distribution of Critical Case Rate");


# The above histograms suggests that there is uneven distribution of data(prescence of outliers)
# therefore will be minimal or no correlation between the various parameters(rate parameters), the reason for this is shown in the scatter plot below; 

# In[56]:


plt.scatter(x=df["Population"],y=df["TotalCases"])
plt.xlabel("Population")
plt.ylabel("TotalCases")
plt.title("Population vs TotalCases");
df["Population"].corr(df["TotalCases"])


# In[52]:


df.index = df["Country"]
df.head(2)


# In[53]:


top_10_cases = df["TotalCases"].sort_values(ascending=False).head(10)
top_10_cases


# In[63]:


top_10_deaths = df["TotalDeaths"].sort_values(ascending=False).head(10)
top_10_deaths


# In[18]:


top_10_popu = df["Population"].sort_values(ascending=False).head(10)
top_10_popu


# In[28]:


# IR = infection rate
top_10_IR = df["InfectionRate"].sort_values(ascending=False).head(10)
top_10_IR


# In[29]:


# RR = recovery rate
top_10_RR = df["RecoveryRate"].sort_values(ascending=False).head(10)
top_10_RR


# In[64]:


# DR = death rate
top_10_DR = df["DeathRate"].sort_values(ascending=False).head(10)
top_10_DR


# In[33]:


# scatter plots to show the relationship between total cases and total deaths
plt.scatter(x=df["TotalCases"],y=df["TotalDeaths"])
plt.xlabel("TotalCases")
plt.ylabel("TotalDeaths")
plt.title("TotalCases vs TotalDeaths");


# In[37]:


df["TotalCases"].corr(df["TotalDeaths"])


# In[34]:


# scatter plots to show the relationship between total cases and total recoverred
plt.scatter(x=df["TotalCases"],y=df["TotalRecovered"])
plt.xlabel("TotalCases")
plt.ylabel("TotalRecovered")
plt.title("TotalCases vs TotalRecovered");


# In[36]:


df["TotalCases"].corr(df["TotalRecovered"])


# In[35]:


plt.scatter(x=df["TotalCases"],y=df["Critical"])
plt.xlabel("TotalCases")
plt.ylabel("Critical")
plt.title("Total cases vs Critical cases");


# In[39]:


df["TotalCases"].corr(df["Critical"])

