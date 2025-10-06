import numpy as np
import matplotlib.pyplot as plt
from my_python_package.functions import *

def main():
    x=np.linspace(0.0,0.31,100)
    y=([])
    for xi in x:
        y.append(launch_angle_range(2,xi,0.04))
    plt.plot(x,y)
    plt.show()
if __name__ == '__main__':
    main()