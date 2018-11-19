import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import numpy as np
import math


beta = 0.0079
lam = 0.07
l = 1e-4

data = {'1g' : {'w' : [0, -79.077],
                'B' : [0.00097, 0.99903]
               },
        '6g' : {'w' : [0, -0.01433, -0.0682, -0.1947, -1.023, -2.896, -79.4],
                'B' : [0.00097, 0.000091, 0.000664, 0.000901, 0.001282,
                       0.001292, 0.9948]
               }
       }

def neut_pop(t, lam):

    i_6 = np.multiply(data['6g']['B'], np.exp(np.multiply(data['6g']['w'], t)))
    i_1 = (1 / (beta + lam*l))*(lam*l + beta*math.exp(-(lam + beta/l)*t))
    
    i_6 = sum(i_6)

    return i_6, i_1


def plot(lam):
    times = np.linspace(0, 1, 100)

    n1s = []
    n6s = []

    for t in times:
        n6, n1 = neut_pop(t, lam)
        n1s.append(n1)
        n6s.append(n6)

    fig = plt.figure()
    plt.plot(times, n1s, label='1 Group')
    plt.plot(times, n6s, label='6 Group')
    plt.legend()
    plt.title(r'$\lambda$={0} [1/s]'.format(lam))
    plt.xlabel('time [s]')
    plt.ylabel('i(t) [-]')
    plt.yscale('log')
    plt.savefig('pr2_l_{0}.png'.format(lam))

plot(0.0767)
plot(0.405)
