#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[5]:


print("K-nearest neighbor")


# In[14]:


train_data=np.load('hw2_data/knn/train_data.npy')
train_data[0]


# In[15]:


len(train_data)


# In[21]:


train_labels = np.load('hw2_data/knn/train_labels.npy')
print(len(train_labels))
train_labels


# In[24]:


test_data = np.load('hw2_data/knn/test_data.npy')
print(len(test_data))
test_data[0]


# In[25]:


test_labels = np.load('hw2_data/knn/test_labels.npy')
test_labels


# In[ ]:




