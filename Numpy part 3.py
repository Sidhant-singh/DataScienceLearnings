#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#numpy -  array manipulation


# In[5]:


arr = np.random.randint(1,10,(4,4))


# In[6]:


arr


# In[7]:


arr.reshape(2,8)


# In[8]:


arr.T


# In[9]:


arr.flatten() #puts the data into the single list


# In[10]:


arr


# In[14]:


np.expand_dims(arr,axis=1) #it expands the dimension


# In[15]:


data = np.array([[1],[2],[3]])


# In[16]:


np.squeeze(data)


# In[18]:


np.repeat(data,2) #it repeat the data


# In[20]:


np.roll(data,2)  #it rotate the element by given idx.


# In[21]:


np.diag(np.array([1,2,3,4])) # it create a diagnonal array.


# In[22]:


#numpy - binaryoperation


# In[23]:


arr1 = np.random.randint(1,10,(3,4))
arr2 = np.random.randint(1,10,(3,4))


# In[24]:


arr1


# In[25]:


arr2


# In[26]:


arr1+arr2


# In[27]:


arr1-arr2


# In[28]:


arr1*arr2


# In[30]:


arr1/arr2


# In[31]:


arr1**arr2


# In[32]:


~arr1


# In[33]:


arr1>arr2


# In[34]:


arr3 = np.array(["siddhant" , "singh"])


# In[35]:


arr3


# In[36]:


np.char.upper(arr3)


# In[37]:


np.char.capitalize(arr3)


# In[38]:


#numpy - mathematical functions


# In[39]:


arr1


# In[40]:


np.sin(arr1)


# In[41]:


np.cos(arr1)


# In[42]:


np.tan(arr1)


# In[43]:


np.log10(arr1)


# In[44]:


np.exp(arr1)


# In[45]:


np.power(arr1,2)


# In[46]:


np.mean(arr1)


# In[47]:


np.median(arr1)


# In[48]:


np.std(arr1)


# In[49]:


np.var(arr1)


# In[50]:


np.min(arr1)


# In[51]:


np.max(arr1)


# In[52]:


#numpy - arithmetic operations


# In[53]:


arr1


# In[54]:


arr2


# In[56]:


np.subtract(arr1,arr2)


# In[57]:


np.multiply(arr1,arr2)


# In[58]:


np.mod(arr1,arr2)


# In[59]:


np.power(arr1,arr2)


# In[ ]:




