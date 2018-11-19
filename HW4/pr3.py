import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import numpy as np
import math


a = 2
n0 = 1
lam = 0.1
beta = 0.0065
bol = 10
l = beta / bol


def rho_t(t):
    """Get rho as function of t
    """

    t1 = a / (n0 + a*t)
    t2 = beta*(1-math.exp(-lam*t)) / lam

    return t1*(l + t2)

times = np.linspace(0, 100, 1000)

rho = []
for t in times:
    rho.append(rho_t(t))

fig = plt.figure()
plt.plot(times, rho)
plt.title(r'Required reactivity insertion such that: n(t) = $n_0$ + at')
plt.xlabel('time [s]')
plt.ylabel('n(t) [-]')
plt.savefig('pr3.png')

