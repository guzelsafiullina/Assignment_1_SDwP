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
        with contextlib.redirect_stdout(io.StringIO()) as f:
            start = time.time()
            result = self.fun(*args,**kwargs)
            end = time.time()
            output = f.getvalue()
            
        
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

def Rank_table():
    rank_table = dict(sorted(table.items(), key=lambda item: item[1]))
    print("PROGRAM|RANK|TIME ELAPSED")
    n = 1
    for i in rank_table:
        print(i,"\t", n, "\t", rank_table[i])
        n+=1