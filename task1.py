#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import contextlib
import io

count = 0
def decorator_1(fun):
    count = 0
    def wrapper(*args):
        #nonlocal count
        #count+=1
        wrapper.counter += 1
        start = time.time_ns()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            fun(*args)
        end = time.time_ns()
        s = f.getvalue()
        
        print(fun.__name__, "call", wrapper.counter, "execution time", end - start)
        return fun(*args)
    wrapper.counter = 0
    return wrapper

