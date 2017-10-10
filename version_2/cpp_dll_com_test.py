import os
import numpy
import ctypes
from numpy.ctypeslib import ndpointer

# Mashaling with C++
from ctypes import *
dll_path = os.getcwd() + "\\version_2\\cpp\\pythonMandelbrotCpp.dll"
print(dll_path)
mydll = cdll.LoadLibrary(dll_path)
#mydll = cdll.LoadLibrary("cpp/pythonMandelbrotCpp")



#cake = [ctypes.c_float, ctypes.c_float]
print(mydll.sum_int(3, 7))

"""
sum_float = mydll.sum_float
sum_float.restype = c_float
mydll.sum_float.restype = c_float
print(mydll.sum_float(c_float(0.8), c_float(1.4)))
"""

if_true_af = mydll.if_true
if_true_af.restype = c_bool
print(mydll.if_true(c_float(1.01)))



"""
mydll.array_test()
ArrayType = ctypes.c_double*10
array_pointer = ctypes.cast(mydll, ctypes.POINTER(ArrayType))
print(numpy.frombuffer(array_pointer.contents))
"""

mydll.array_test.restype = ndpointer(dtype=ctypes.c_int, shape=(10))

res = mydll.array_test()
print(res)
