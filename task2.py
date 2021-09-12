import time
import contextlib
import io
import inspect
from inspect import signature



count = 0 


def decorator_2(fun):
    count = 0
    def wrapper(*args, **kwargs):
        #nonlocal count
        #count+=1
        wrapper.counter += 1
        start = time.time_ns()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            result = fun(*args, **kwargs)
            output = f.getvalue()
        end = time.time_ns()
        
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