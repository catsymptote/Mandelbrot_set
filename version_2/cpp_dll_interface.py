import os

# Mashaling with C++
from ctypes import *
dll_path = os.getcwd() + "\\version_2\\cpp\\pythonMandelbrotCpp.dll"
print(dll_path)
mydll = cdll.LoadLibrary(dll_path)
#mydll = cdll.LoadLibrary("cpp/pythonMandelbrotCpp")



#cake = [ctypes.c_float, ctypes.c_float]
print(mydll.sum_int(3, 7))


if_true_af = mydll.if_true
if_true_af.restype = c_bool
print(mydll.if_true(c_float(1.01)))
