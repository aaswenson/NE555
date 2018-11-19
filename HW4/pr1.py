import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import numpy as np
import math

beta = 0.00649
lam = 0.1
l = 0.001
n0 = 1000
n1 = 2000
dn = n1 - n0

def neutron_pop(t, q):
    """
    """
    
    if t < 0:
        return 0

    t1 = l*q / (beta + lam*l)
    t2 = (beta / (beta + lam*l)) * (1 - math.exp(-(lam + beta/l)*t))
    
    n = t1*(lam*t + t2)

    return n

def func(t, q):
    """
    """

    n = neutron_pop(t, q)

    return (n - dn)**2

def find_t(q):
    """
    """
    res = minimize_scalar(func, bounds=(0, 1e6), args=(q),
                          method='Bounded', options={'xatol': 1e-10})
    
    return res.x

def plot(qs):
    """
    """
    
    times = np.linspace(-1,1, 1000)
    fig = plt.figure()
    
    time_to_n1 = []

    for q in qs:
        print(q, find_t(q))
        time_to_n1.append(find_t(q))
        n = []
        for t in times:
            n.append(n0 + neutron_pop(t, q))
        plt.plot(times, n, label=q)
     
    plt.title('N(t) with Constant Sources')

    plt.ylim(990, max(n)+5)
    plt.legend()
    plt.xlabel('time [s]')
    plt.ylabel('n [-]')
    plt.savefig('pr1.png')

#    plt.show()
    
    fig = plt.figure()
    plt.scatter(qs, time_to_n1)
    plt.show()

#plot([10, 50, 100, 500, 1000, 10000])
plot([10, 50, 100])
