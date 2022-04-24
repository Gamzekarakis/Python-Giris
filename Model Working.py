#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
ad=pd.read_csv("Advertising.csv")
df=ad.copy()
df.head()


# In[2]:


df=df.iloc[:,1:len(df)]
df.head()


# In[3]:


ad=pd.read_csv("Advertising.csv",usecols=[1,2,3,4])


# In[4]:


df.head()
df.info()


# In[5]:


df.describe().T
df.isnull().values.any()


# In[6]:


df.corr()
import seaborn as sns
sns.pairplot(df,kind="reg");


# In[7]:


sns.jointplot(x="TV",y="sales",data=df,kind="reg")


# In[13]:


X=df[["TV"]]
X[0:5]


# In[14]:


import statsmodels.api as sm

X = sm.add_constant(X)
X[0:5]
y=df["sales"]
y[0:5]


# In[15]:


lm=sm.OLS(y,X)
model=lm.fit()
model.summary()


# In[16]:


import statsmodels.formula.api as smfprint("Sales="+ str("%.2f"%model.params[0]) + "+TV" + "*"  +str("%.2f"% model.params[1]))
lm=smf.ols("sales~TV",df)
model=lm.fit()
model.summary()


# In[17]:


print("Sales="+ str("%.2f"%model.params[0]) + "+TV" + "*"  +str("%.2f"% model.params[1]))


# In[ ]:





# In[ ]:




