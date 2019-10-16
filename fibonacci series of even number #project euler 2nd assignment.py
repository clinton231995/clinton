#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=0
b=1
c=1
temp=0
n=20
print('Series is as follows : \n')
for i in range(0,n-1):
    temp=a+b
    if temp%2==0:
        print(temp)
    a=b
    b=temp
    temp=0

