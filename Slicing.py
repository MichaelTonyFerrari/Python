
# coding: utf-8

# <h1>Slicing Arrays</h1>

# In[1]:


import numpy as np


# In[2]:


vec = np.array([-5, -2, 0, 12, 14, 15])


# In[3]:


vec


# In[4]:


vec[0]


# In[5]:


# Replace 
vec[0] = -12


# In[6]:


vec


# In[7]:


vec[-2]


# In[8]:


305 % 7


# In[9]:


vec[305 % 7]


# In[10]:


vec.size


# In[11]:


vec[305 % vec.size]


# In[12]:


305 % vec.size


# In[16]:


# Create shape of array to 6x5
arr = np.arange(30)
arr.shape = (6,5)
arr


# In[17]:


# Display row 2 
arr[2]


# In[18]:


# second to last row in array
arr[-2]


# In[20]:


# arr[row, column]
arr[4,2]


# In[21]:


# More practicle 
row = 4
column = 2
arr[row, column]


# In[23]:


arr[4][2]


# In[24]:


arr_3d = np.arange(70)
arr_3d.shape = (2, 7, 5)
arr_3d


# In[25]:


arr_3d[1]


# In[26]:


arr_3d[1,2]


# In[27]:


arr_3d[1,2,3]


# In[28]:


arr_3d[1,2,3] = 1111


# In[29]:


arr_3d[1,2]


# In[ ]:




