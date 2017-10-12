######################################
## Library for Complex Number Maths ##
######################################


from math import *
from math import exp, expm1


## l_complex_1 + l_complex_2
def complex_add(l_complex_1, l_complex_2):
    ## l_1 and l_2 has [a, b] for a+ib
    real = l_complex_1[0] + l_complex_2[0]
    imag = l_complex_1[1] + l_complex_2[1]
    l_result = [real, imag]
    return l_result


## l_complex_1 ^ l_complex_2
def complex_square(l_complex):
    ## l_1 and l_2 has [a, b] for a+ib
    real = l_complex[0]**2 - l_complex[1]**2
    imag = 2 * l_complex[0] * l_complex[1]
    l_result = [real, imag]
    return l_result

def complex_length(l_complex):
    #output = (l_complex[0]**2 + l_complex[1]**2)**0.5
    output = sqrt(l_complex[0]**2 + l_complex[1]**2)
    return output
