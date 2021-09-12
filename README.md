# Assignment_1_SDwP
This is the solution of the first assignmnet for Software Design with Python course. In this repository contains different implementations of functions decorators.
This repository includes 5 files: task1.py-task4.py and main.py.
task1.py includes implementation of a function decorator that calculates function execution time and the number of times the decorated function was called (function call trace). It works for multiple functions.
task2.py extend previous implementation so that the decorator could dump original source code of the function. 
task3.py contains the implementation of the decorator behavior in tasks 1 & 2 using a class decorator. All the program output (from the decorator) are dumped into a .txt file.
task4.py extends function and class decorators so that if a decorated function encounters an error it wouldn’t put it back into stdout. Instead, it pipes the error stream into a log file together with a timestamp. 
main.py contains the test functions and the application of all the decorators from the previous files with comments
