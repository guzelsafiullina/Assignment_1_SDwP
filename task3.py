import time
import inspect
from inspect import signature
import contextlib
import io

global table
table = {}

class decorator_cl_1:
    def __init__(self, fun):        
        self.fun = fun
        self.arguments = []
        self.count = 0
        self.execution_time = 0
        
    def __call__(self, *args, **kwargs):

        text = []
        self.count += 1
        self.arguments = args
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            result = self.fun(*args,**kwargs)
            output = f.getvalue()
        
        end = time.time()
        table[self.fun.__name__ ] = end - start
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
        return self.fun(*args,**kwargs)

