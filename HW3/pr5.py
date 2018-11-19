import matplotlib.pyplot as plt
import numpy as np
import math

n0 = 1
lam = 0.1

times = np.linspace(0, 20, 1000)
n_t = np.zeros(len(times))

def calc_roots(beta, rho, lam, l):
    """Calculate the roots of the inhour equation.
    """

    term1 = -(beta - rho - lam*l)
    term2 = math.sqrt((beta-rho + lam*l)**2 + 4*l*lam*rho)

    w_1 = (1/(2*l))*(term1 + term2)
    w_2 = (1/(2*l))*(term1 - term2)

    return w_1, w_2

def calc_n_t(n0, rho, t):
    """Calculate neutron population as function of time and reactor state.
    """
    
    lead_term = n0 / (rho - 1) 
    exp_term = math.exp(10*(rho-1)*t)

    exp2_term = math.exp(-lam*rho*t / (rho - 1))

    return lead_term*(rho*exp_term - exp2_term)

def calc_pop(times, lam, n0, rho_ins):
    """
    """
    rho = 0
    t0 = 0
    for i, t in enumerate(times):
        
        if t > 0 and rho == 0:
            rho = 0.5
            n0 = n_t[i-1]
            t0 = t
        if t > 10 and rho == 0.5:
            rho = rho_ins 
            n0 = n_t[i-1]
            t0 = t
        
        n_t[i] = calc_n_t(n0, rho, t-t0)
    
    plt.plot(times, n_t)
    plt.title(r"Neutron Pop: $\rho\beta$ = {0}".format(rho_ins))
    plt.xlabel(r"Time [s]")
    plt.ylabel(r"Neutron Population [-]")
    plt.savefig("{0}.png".format(rho_ins))
    plt.close()

calc_pop(times, lam, n0,  0.75)
calc_pop(times, lam, n0, -0.25)
calc_pop(times, lam, n0,  0)
