from scipy.optimize import minimize_scalar
import numpy as np

nu = 2.432
ph_beta = [0.05e-5, 0.103e-5, 0.323e-5, 2.34e-5, 2.07e-5, 3.36e-5, 7e-5,
           20.4e-5, 65.1e-5]

ph_lam  = [6.26e-7, 3.63e-6, 4.37e-5, 1.17e-4, 4.28e-4, 1.5e-3, 4.81e-3, 1.69e-2,
           2.77e-1]

n_beta = [0.00052, 0.00346, 0.0031, 0.00624, 0.00182, 0.00066]
n_lam  = [0.0124, 0.0305, 0.111, 0.301, 1.14, 3.01]

def sum_lam_beta(beta, lam, w):
    """
    """

    return sum(np.divide(beta, np.add(w, lam)))

def func(w, l, rho, beta, lam):
    """
    """
    
    sum = sum_lam_beta(beta, lam, w)
    t1 = w*l / (1 + w*l)
    t2 = w / (1+w*l)
    
    return ((t1 + t2*sum) - rho)**2


def find_omega(beta, lam, rho, l):
    """
    """
    beta_frac = sum(beta) / nu
    print(beta_frac)
    dollars = rho * beta_frac

    res = minimize_scalar(func, bounds=(0, 1), args=(l, dollars, beta, lam),
                          method='Bounded', options={'xatol': 1e-10})
    
    return res.x

l = 5e-4
tot_beta = n_beta + ph_beta
tot_lam = n_lam + ph_lam

w = find_omega(tot_beta, tot_lam, 0.1, l)
print("Stable Period with photoneutrons: {0} [s]".format(1/w))

w = find_omega(n_beta, n_lam, 0.1, l)
print("Stable Period without photoneutrons: {0} [s]".format(1/w))    
