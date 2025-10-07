import numpy as np
import matplotlib.pyplot as plt
from my_python_package.functions import *

# Testing sqrt function,
# as equation 17 is just a constant times that square root function for calculation 
# when alpha is constant we just need to test the square root
def testsqrt():
    #test within its bound and find its true error
    x=np.linspace(0,2.5,100)
    true_error=([])
    sqrtx=([])
    for xi in x:
        true_error.append([sqrt(xi)-np.sqrt(xi)])
        sqrtx.append([sqrt(xi)])
    plt.plot(x,np.sqrt(x),label="expected output")
    plt.plot(x,sqrtx,label="resulting curve")
    plt.plot(x,true_error,label="true error")
    plt.legend()
    plt.xlabel("input")
    plt.ylabel("output")
    plt.show()
    return true_error

# to test the sqrt function and plot it along with true error
# due to the hard coded bound between 0<=x<=2.5 outof bound situation will not be accounted 
# especially when we cannot draw compairson with imaginary numbers and the real outout 
# (if a is real in the taylor series)
testsqrt()

