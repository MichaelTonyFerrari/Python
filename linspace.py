
# coding: utf-8

# <h1>linspace(), zeros(), ones(), and NumPy data types</h1>

# In[2]:


import numpy as np


# In[3]:


# three elements, ranging from 5 to 10  
np.linspace(5, 10, 3)


# In[5]:


# setting retstep to true will return step value 
ls =np.linspace(5, 20, 9, retstep = True)


# In[6]:


ls


# In[7]:


ls[1]


# In[9]:


# Create array of 10 values set to 0 
np.zeros(10)


# In[10]:


# Create array of 10 values set to 1
np.ones(10)


# In[11]:


# 5 rows 4 columns set to 0 
np.zeros((5,4))


# In[12]:


# 5 2d arrays, 4x3 
np.zeros((5,4,3))


# In[13]:


# create array of 11 elements that are of size 64bit
np.zeros(11, dtype='int64')


# In[15]:


np.zeros(11)


# 
