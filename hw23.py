#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import time
import matplotlib.pyplot as plt
import math


# In[2]:


data1 = np . load ( 'hw2_data/hac/data1.npy' )
data2 = np . load ( 'hw2_data/hac/data2.npy' )
data3 = np . load ( 'hw2_data/hac/data3.npy' )
data4 = np . load ( 'hw2_data/hac/data4.npy' )


# In[3]:


plt.plot(data1[:,0],data1[:,1],'ok')
plt.show()
plt.plot(data2[:,0],data2[:,1],'ok')
plt.show()
plt.plot(data3[:,0],data3[:,1],'ok')
plt.show()
plt.plot(data4[:,0],data4[:,1],'ok')
plt.show()


# In[4]:


def eucledien(point1:list,point2:list)-> float:#DONE
    """ Gives distance between two points """
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


# In[5]:


#Single Linkage
smallestDist = eucledien(data1[0],data1[1])
smallest1 = 1
smallest2 = 0
data = data1


# In[6]:


for i in range(0,len(data1)):
    for j in range(i+1,len(data1)):
        dist =eucledien(data1[i],data1[j])
        if(dist < smallestDist):
            smallestDist = dist
            smallest1 = i
            smallest2 = j


# In[7]:


plt.plot(data1[:,0],data1[:,1],'ok',data[smallest1][0],data[smallest1][1],'vb',data1[smallest2][0],data[smallest2][1],'vb')


# In[8]:


numberOfClusters = 2  #1-2-3 icin 2 cluster var, 4 icin 4 tane


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


def generateClusters(data):
    res = []
    lendata = len(data)
    for i in range(0,lendata):
        res.append([data[i]])
    return res



def centre(c):
    cx = 0
    cy = 0
    for i in range(0,len(c)):
        cx +=c[i][0]
        cy +=c[i][1]
    cx = cx/len(c)
    cy = cy/len(c)
    return [cx,cy]
def getNearestDistanceBetweenTwoClusters(c1,c2,typeOfClustering):
    if(typeOfClustering=="nearest"):
        res = eucledien(c1[0],c2[0])
        for i in range (0,len(c1)):
            for j in range (0,len(c2)):
                temp = eucledien(c1[i],c2[j])
                if(temp<res):
                    res = temp
        return res
    if(typeOfClustering == "farthest"):
        res = eucledien(c1[0],c2[0])
        for i in range (0,len(c1)):
            for j in range (0,len(c2)):
                temp = eucledien(c1[i],c2[j])
                if(temp>res):
                    res = temp
        return -res
    if(typeOfClustering == "average"):
        
        return 0.
    if(typeOfClustering == "centroid"):
        
        return eucledien(centre(c1),centre(c2))
    else:
        return 0.
    


# In[32]:


def getNearestClusters(clusters,typeOfClustering):
    nearest = eucledien(clusters[0][0],clusters[1][0])
    if(typeOfClustering=="fartest"):
        nearest = -nearest
    resI = 0
    resJ = 1
    for i in range(0,len(clusters)):
        for j in range(i+1,len(clusters)):
            temp = getNearestDistanceBetweenTwoClusters(clusters[i],clusters[j],typeOfClustering)
            if(temp<nearest):
                nearest = temp
                resI = i
                resJ = j
                
    return resI,resJ


# In[27]:


def concat(clusters,i,j):
    for k in range(0,len(clusters[j])):
        clusters[i].append(clusters[j][k])
    return clusters


# In[28]:


def remove(clusters,j):
    clusters.pop(j)
    return clusters

# In[29]:


colors = ['ok','hr','pc','vg']
def mein(data,numberOfClusters,typeOfClustering):
    clusters = generateClusters(data)
    while(True):
        if(len(clusters)<=numberOfClusters):
            break
        print("On it")
        i,j = getNearestClusters(clusters,typeOfClustering)
        clusters = concat(clusters,i,j)
        clusters = remove(clusters,j)
    return clusters


# In[16]:


clusters = mein(data1,2,"nearest")


# In[17]:



for i in range(0,len(clusters)):
    ci = clusters[i]
    for j in ci:
        plt.plot(j[0],j[1],colors[i])
plt.show()


# In[18]:


def plotclusters(clusters):
    for i in range(0,len(clusters)):
        ci = clusters[i]
        for j in ci:
            plt.plot(j[0],j[1],colors[i])
    plt.show()


# In[19]:


clusters = mein(data2,2,"nearest")


# In[20]:


plotclusters(clusters)


# In[21]:


clusters3 = mein(data3,2,"nearest")


# In[22]:


plotclusters(clusters3)


# In[23]:


clusters4 = mein(data4,4,"nearest")
plotclusters(clusters4)


# In[33]:


clusters4farthest = mein(data4,4,"farthest")
plotclusters(clusters4farthest)


# In[34]:


clusters3farthest = mein(data3,2,"farthest")
plotclusters(clusters3farthest)


# In[35]:


clusters2farthest = mein(data2,2,"farthest")
plotclusters(clusters2farthest)


# In[36]:


clusters1farthest = mein(data1,2,"farthest")
plotclusters(clusters1farthest)


# In[40]:


centroid1 = mein(data1,2,"centroid")
plotclusters(centroid1)


# In[41]:


centroid2 = mein(data2,2,"centroid")
plotclusters(centroid2)
centroid3 = mein(data3,2,"centroid")
plotclusters(centroid3)
centroid4 = mein(data4,4,"centroid")
plotclusters(centroid4)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




