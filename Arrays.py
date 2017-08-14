
# coding: utf-8

# <h1>Create NumPy arrays using Python's "array like" data types</h1>
# 

# In[1]:


import numpy as np


# In[2]:


print(np.__version__)


# In[9]:


list_a = [-5, 0, 4, 6, 10]

li = np.array(list_a)
li


# In[10]:


#quick multiply all values in array
li * 5


# In[13]:


#promoted to last value in array 
my_tuple = (12, -2.3, 4+5j)
np.array(my_tuple)


# ### Difference between python and numpy data structures 

# In[14]:


# prints 6 times 
my_tuple * 6


# In[16]:


# multiply values by 6
np.array(my_tuple) * 6


# In[ ]:




