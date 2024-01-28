#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sort ,search & counting function


# In[2]:


import numpy as np


# In[5]:


arr= np.array([5,2,4,1,6])


# In[6]:


arr


# In[7]:


np.sort(arr)


# In[9]:


np.searchsorted(arr,3) #it will give the idx of the array ,if we put in it ,the array remains the same as sorted.


# In[10]:


arr1 = np.array([0,23,42,24,56,2,5,11,45,0,0])


# In[11]:


np.count_nonzero(arr1)


# In[13]:


np.count_nonzero(arr1)


# In[14]:


np.where(arr1>0) #it will give the idx number where arr1>0


# In[15]:


np.extract(arr1>40,arr1) #it will give the element where arr1>40


# In[16]:


#numpy - byte swapping


# In[17]:


arr1


# In[18]:


arr1.byteswap()


# In[19]:


#numpy - copies and views


# In[20]:


a = np.copy(arr1)


# In[21]:


b = arr1.view() #swallow copy


# In[22]:


b


# In[23]:


b[0]= 1


# In[24]:


b


# In[25]:


arr1


# In[26]:


#numpy - matrixlibrary


# In[27]:


import numpy.matlib as nm


# In[28]:


nm.zeros((3,4))


# In[29]:


nm.eye(4)


# In[30]:


#numpy - linear alegebra


# In[31]:


arr1 = np.random.randint([[2,3],[4,5]])


# In[32]:


arr2 = np.random.randint([[5,3],[2,5]])


# In[33]:


arr1


# In[34]:


arr2


# In[35]:


arr1.dot(arr2)


# In[36]:


arr1@arr2 #dot product is matrix multiplication


# In[ ]:




