#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


list(range(5))


# In[3]:


list(range(10))


# In[8]:


list(range(0.4,10.4))


# In[9]:


#arange - here we have'nt mention the number of elements in the arrays but in linspace we did that.
np.arange(0.4,10.4,0.3)


# In[6]:


np.linspace(1,5,20) #divide the entire scale into 20 division 


# In[11]:


np.logspace(1,5,10,base=2)


# In[12]:


np.zeros(5) #it will generate the arrays of zeros of the guven size


# In[13]:


np.zeros((3,4))


# In[14]:


np.zeros((3,4,2)) ## it will generate 3 matrixes of 4 X 2 matrix


# In[15]:


np.ones(5)


# In[21]:


arr = np.ones((3,4))


# In[22]:


arr+5


# In[27]:


arri = np.eye(5) #it helps us to create a identity matrix


# In[24]:


np.identity(3)


# In[25]:


import pandas as pd


# In[29]:


pd.DataFrame(arri)


# In[30]:


np.random.rand(2,3) #it generate the random float no. in the given range


# In[31]:


np.random.randn(2,3) #it will generate that data where mean = 0 and standard deviation =1.


# In[39]:


arr3 = np.random.randint(1,10,(3,4))


# In[42]:


arr3.size


# In[43]:


arr3.shape


# In[44]:


arr3.reshape(2,6)


# In[47]:


arr3.reshape((2,2,3))


# In[48]:


arr4 = np.random.randint(1,10,(5,6))


# In[49]:


arr4


# In[50]:


arr4>5


# In[51]:


arr4[arr4>5]


# In[52]:


arr4


# In[54]:


arr4[0,[0,1]]


# In[55]:


arr4[2:4,[2,3]]


# In[56]:


arr5 = np.random.randint(1,3,(3,3))
arr6 = np.random.randint(1,3,(3,3))


# In[57]:


arr5


# In[58]:


arr6


# In[59]:


arr5+arr6


# In[60]:


arr5-arr6


# In[61]:


arr5*arr6 #indexwise multiplication


# In[62]:


arr5@arr6 #matrix multiplication


# In[64]:


arr5/arr6


# In[65]:


arr5/0


# ## Numpy - broadcasting

# In[66]:


arr7 = np.zeros((3,4))


# In[67]:


arr7+5 #broadcasting 5 into array


# In[68]:


a = np.array([1,2,3,4])


# In[69]:


arr7+a


# In[70]:


b = np.array([[3,4,5]])


# In[74]:


arr8 = arr7+b.T


# In[73]:


b.T #transpose


# In[75]:


np.sqrt(arr8)


# In[76]:


np.log10(arr8)


# In[77]:


np.exp(arr8)


# In[78]:


np.min(arr8)


# In[79]:


np.max(arr8)


# In[ ]:




