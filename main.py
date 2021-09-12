#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import math
import task1
import task2
import task3
import task4
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_cl_1
from task4 import decorator_exception_class
from task4 import decorator_exception

#testing the first decorator (task1)
@decorator_1        
def pascal_triangle(n):    
    def next_string(a):    
        b = [0]
        for i in range(len(a)-1):
            b.append(a[i]+a[i+1])
        b.append(0)
        return(b)

    a = [0,1,0]

    for i  in range(n):
        print(a[1:len(a)-1])
        a = next_string(a)
        
@decorator_1
def quadratic_equation(a = 1,b = 2,c = 1):
    D = b*b - 4*a*c
    if a==0 :
        if b!=0: print -c/b
        else: print("No roots")
    else:
        if D>0:
            print("x_1 = ", (-b+sqrt(D))/(2*a), "x_2 = ",(-b-sqrt(D))/(2*a))
        elif D==0: print("x = ",-b/(2*a))
        else: print("No real decision")
            
pascal_triangle(6)
quadratic_equation()
quadratic_equation()
pascal_triangle(7)

#testing decorator from task 2
@decorator_2
def filter_new(list = [1,2,3,4,5],action = lambda i: i+1):
    '''Performs an action on the given list'''
    newList = []
    for item in list:
        newList.append(action(item))
    return newList

filter_new()


#testing decorator from the task 3. Check results in txt - file
@decorator_cl_1
def incrementer(n):
    return lambda a: a+n

#creating a rank table for the task3
incrementer(6)
@decorator_cl_1
def filter_new(list = [1,2,3,4,5],action = lambda i: i+1):
    '''Performs an action on the given list'''
    newList = []
    for item in list:
        newList.append(action(item))
    return newList
@decorator_cl_1
def func():
    return 52434*354
@decorator_cl_1
def fund():
    print(123*325-12*524-354)

incrementer(9)
filter_new()
func()
fund()
#printed rank table for several functions
task3.Rank_table()

#testing decorator from the task 4.  Check results in txt - file 
@decorator_exception_class
def filter_new(list = [1,2,3,4,5],action = lambda i: i+1):
    '''Performs an action on the given list'''
    newList = []
    for item in list:
        newList.append(action(item))
    return newList


filter_new(123,532,54)


# In[ ]:




