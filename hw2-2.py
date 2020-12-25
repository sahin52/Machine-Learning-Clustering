#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import time
import matplotlib.pyplot as plt
import math


# In[2]:


clustering1 = np.load('hw2_data/kmeans/clustering1.npy')
clustering2 = np.load('hw2_data/kmeans/clustering2.npy')
clustering3 = np.load('hw2_data/kmeans/clustering3.npy')
clustering4 = np.load('hw2_data/kmeans/clustering4.npy')


# In[3]:


plt.plot(clustering1[:,0],clustering1[:,1],'ok')
plt.show()
plt.plot(clustering2[:,0],clustering2[:,1],'ok')
plt.show()
plt.plot(clustering3[:,0],clustering3[:,1],'ok')
plt.show()
plt.plot(clustering4[:,0],clustering4[:,1],'ok')
plt.show()


# In[4]:


def getRandomCenters(howManyCenters,clustering):#DONE
    """
    returns an array of length howManyCenters from clustering, it is better to return different points but not important

    """
    res: np.ndarray = np.zeros((howManyCenters,2),float)
    for i in range(0,howManyCenters):
        res[i] = clustering[random.randint(0,len(clustering)-1)]
    return res


# In[5]:


def findNearestCenterToEveryPoint(clusterCenters,clustering):#DONE needs #TEST
    """ 
    returns an array of length len(clustering). 
    In this array, every number(which is int), 
    represents the nearest cluster center to the point in clustering

    """
    res = np.zeros(len(clustering),int)
    for i in range (0,len(res)):
        distances: list = []        
        for j in range (0,len(clusterCenters)):
            distances.append(eucledien(clusterCenters[j],clustering[i]))
        #print(distances)
        #print("^^ distances")
        res[i] = distances.index(min(distances))
        
    return res


# In[6]:


def findNewClusterCenters(howManyCenters: int,nearestCenters: list,clustering: list)->list:#DONE NEEDS TESTING
    """ 
    merkezi ayni olan noktalarin ortalamasini bulacaksin
    returns an array of length howManyCenters, which will carry the new Center's
    """
    res = np.zeros((howManyCenters,2),float)
    for i in range (0,howManyCenters):
        pointsNearToThisCenter = np.zeros((1,2))
        for j in range(0,len(nearestCenters)):
            k = nearestCenters[j]
            if(i == k):
                pointsNearToThisCenter = np.concatenate([pointsNearToThisCenter,[clustering[j]]  ])
        a = getCenterOfThePoints(pointsNearToThisCenter)
        b= np.array([a])#possible error
        res[i] =b


    return res


# In[7]:


def findDifferenceBetweenOldAndNewClusterCenters(clusterCenters,newClusterCenters):
    """
    returns sum of differences of the center points one to one
    """
    res = 0.
    for i in range(0,len(clusterCenters)):
        res+=eucledien(clusterCenters[i],newClusterCenters[i])

    return res


# In[8]:


def sumOfDistancesToClusterCenters(clustering,newClusterCenters,howManyCenters):#DONE needs test
    """
    returns the sum of the distances of points and their cluster centers
    """
    nearests = findNearestCenterToEveryPoint(newClusterCenters,clustering)
    res = 0.

    for j in range(0,len(nearests)):
        nearestCenterIndex = nearests[j]
        point = clustering[j]
        nearestCenter = newClusterCenters[nearestCenterIndex]
        res+=eucledien(nearestCenter,point)
        

    return res
def eucledien(point1:list,point2:list)-> float:#DONE
    """ Gives distance between two points """
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
def getCenterOfThePoints(points):#DONE needs test
    #if(len(points[:0])==0):
        #zero = getRandomCenters(1,clustering)
    zero = sum(points[:,0]) / len(points)
    one = sum(points[:,1]) / len(points)
    res = np.zeros(2)
    res = [zero,one]
    return res


# In[15]:


def MAINfindSumOfDistancesToClusterCenters(clustering,howManyCenters):
    threshold = 0.01
    #for 10 times
    howManyTimes = 30
    clusterCenters = getRandomCenters(howManyCenters,clustering)
    while(True):
        print("running "+str(howManyTimes)+" many times, with "+str(howManyCenters)+" centers")
        howManyTimes-=1
        nearestCenters = findNearestCenterToEveryPoint(clusterCenters,clustering)
        newClusterCenters = findNewClusterCenters(howManyCenters,nearestCenters,clustering)
        #plt.plot(clustering[:,0],clustering[:,1],'ok',clusterCenters[:,0],clusterCenters[:,1],'vb',newClusterCenters[:,0],newClusterCenters[:,1],'rs')
        #plt.show()
        if(findDifferenceBetweenOldAndNewClusterCenters(clusterCenters,newClusterCenters)<threshold or howManyTimes==0):
            plt.plot(clustering[:,0],clustering[:,1],'ok',clusterCenters[:,0],clusterCenters[:,1],'vb')
            for yy in range(0,len(newClusterCenters)):
                plt.plot(newClusterCenters[yy][0],newClusterCenters[yy][1],'rs')
            plt.show()
            print("DONE")
            return sumOfDistancesToClusterCenters(clustering,newClusterCenters,howManyCenters)
        clusterCenters = newClusterCenters
    
    return


# In[ ]:


results = []

for i  in range(1,11):
    results.append(MAINfindSumOfDistancesToClusterCenters(clustering1,i))
    print(results[i-1])
print("DONE! result is")
xAxis = list(range(1,len(results)+1))
plt.plot(xAxis,results,marker = 'o')
print(results)


# In[ ]:





# In[ ]:


results = []

for i  in range(1,11):
    results.append(MAINfindSumOfDistancesToClusterCenters(clustering2,i))
    print(results[i-1])
print("DONE! result is")
print(results)
xAxis = list(range(1,len(results)+1))
plt.plot(xAxis,results,marker = 'o')
plt.show()


# In[16]:


results = []

for i  in range(1,11):
    results.append(MAINfindSumOfDistancesToClusterCenters(clustering3,i))
    print(results[i-1])
print("DONE! result is")
print(results)
xAxis = list(range(1,len(results)+1))
plt.plot(xAxis,results,marker = 'o')
plt.show()


# In[ ]:


results = []

for i  in range(1,11):
    results.append(MAINfindSumOfDistancesToClusterCenters(clustering4,i))
    print(results[i-1])
print("DONE! result is")
print(results)
xAxis = list(range(1,len(results)+1))
plt.plot(xAxis,results,marker = 'o')
plt.show()


# In[14]:


list(range(1,11))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




