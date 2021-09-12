#!/usr/bin/env python
# coding: utf-8

# In[81]:


import time
import inspect
from inspect import signature
from datetime import datetime
import contextlib
import io

global table
table = {}

class decorator_exception_class:
    def __init__(self, fun):        
        self.fun = fun
        self.arguments = []
        self.count = 0
        
    def __call__(self, *args, **kwargs):

        text = []
        try:
            with contextlib.redirect_stdout(io.StringIO()) as f:
                start = time.time()
                result = self.fun(*args,**kwargs)
                end = time.time()
                output = f.getvalue()

        except Exception as err:
                with open(self.fun.__name__+"_log.txt","w") as errors:
                    errors.write("Sorry, there are some errors: {}\t".format(err) + str(datetime.fromtimestamp(start)))


        self.count += 1
        self.arguments = args
        with open(self.fun.__name__+"_result.txt", 'w') as result:
            result.write(self.fun.__name__ + " call " + str(self.count) + " execution time " + str(end - start) + "\n")
        
            result.write("Name:   "+str(self.fun.__name__)+"\n")
            result.write("Type:   " + str(type(self.fun)) + "\n")
            result.write("Sign:   "+ str(signature(self.fun))+"\n")
            result.write("Args:   " +"positional\t" + str(self.fun.__defaults__) + "\n" + 
                         "named\t" + str(self.fun.__kwdefaults__)+"\n")
            result.write("Doc:   " + str(self.fun.__doc__ )+ "\n")
            result.write("Source:   \n" + inspect.getsource(self.fun) + "\n")
            result.write("Output:   "+str(output)+"\t"+str(self.fun(*args,**kwargs)) + "\n") 
        #return self.fun(*args,**kwargs)

def decorator_exception(fun):

    def wrapper(*args, **kwargs):
        #nonlocal count
        #count+=1
        wrapper.counter += 1
        start = time.time()
        try:
            with contextlib.redirect_stdout(io.StringIO()) as f:
                result = fun(*args, **kwargs)
                output = f.getvalue()
        except Exception as err:
            with open(fun.__name__+"_log.txt","w") as errors:
                errors.write("Sorry, there are some errors: {}\t".format(err) + str(datetime.fromtimestamp(start)))

        end = time.time()
        
        print(fun.__name__, "call", wrapper.counter, "execution time", end - start)
        
        print("Name:   ",fun.__name__,"\n"
             "Type:   ", type(fun), "\n"
             "Sign:   ", signature(fun),"\n"
             "Args:   positional", fun.__defaults__, "\t keyworded", fun.__kwdefaults__, "\n"
             "Doc:   ",fun.__doc__,"\n"
             "Source:   ","\n",inspect.getsource(fun),"\n"
             "Output:   ", output, "\t", result,"\n")
        return fun(*args, **kwargs)
    wrapper.counter = 0
    return wrapper


# In[ ]:




