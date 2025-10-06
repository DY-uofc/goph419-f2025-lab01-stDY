import numpy as np
import matplotlib.pyplot as plt
from my_python_package.functions import *

# plot the graph of launch angle phi against the ve_v0, while holding alpha=0.25, tol_alpha=0.04 constant.
def plot_phi_vs_alpha():
    x=np.linspace(0.0,0.31,100)
    ymin=([])
    ymax=([])
    # since the program accept float only, and does not support directly input numpy arrays, we use this to convert it
    for xi in x:
        ymin.append(launch_angle_range(2,xi,0.04)[0])
        ymax.append(launch_angle_range(2,xi,0.04)[1])
    # generate the plot
    plt.xlabel("alpha(R⊕)")
    plt.ylabel("phi(rad)")
    plt.axhline(np.pi/2,label="π/2")
    plt.title("phi vs alpha, ve_v0=2, tol_alpha=0.04")
    plt.plot(x,ymin,label="min angle")
    plt.plot(x,ymax,label="max angle")
    plt.ylim(0,np.pi/2+0.1)
    plt.legend()
    plt.savefig("figures/phi_vs_alpha.png")
    plt.close()

# plot the graph of launch angle phi against the alpha, while holding ve_v0=2, tol_alpha=0.04 constant.
def plot_phi_vs_ve_v0():
    x=np.linspace(1.35,2.2,100)
    ymin=([])
    ymax=([])
    # since the program accept float only, and does not support directly input numpy arrays, we use this to convert it
    for xi in x:
        ymin.append(launch_angle_range(xi,0.25,0.04)[0])
        ymax.append(launch_angle_range(xi,0.25,0.04)[1])
    # generate the plot
    plt.xlabel("ve/v0")
    plt.ylabel("phi(rad)")
    plt.axhline(np.pi/2,label="π/2")
    plt.title("phi vs ve/v0, alpha=0.25, tol_alpha=0.04")
    plt.plot(x,ymin,label="min angle")
    plt.plot(x,ymax,label="max angle")
    plt.ylim(0,np.pi/2+0.1)
    plt.legend()
    plt.savefig("figures/phi_vs_ve_v0.png")
    plt.close()


def main():
    # test point at ve_v0=2.0, alpha=0.25, tol_alpha=0.
    print("angle min:"+str(launch_angle_range(2,0.25,0.02)[0])+"\nangle max:"+str(launch_angle_range(2,0.25,0.02)[1]))
    # generate plots
    plot_phi_vs_alpha()
    plot_phi_vs_ve_v0()

if __name__ == '__main__':
    main()