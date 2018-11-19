import matplotlib.pyplot as plt
import numpy as np
import math

# neutron speed at 20 degrees C
v = 2200
# source strength
S_o = 2e8
# initial flux
phi_o = 1e11
# extrapolated slab thickness
a = 25.48
# material buckling
B = 0.12329

def get_data(x, t):
   """Generate flux profiles for various times
   """
   integral = (2/a) * 2*math.sin(a*B)/B + 2*v*S_o*t/a

   return np.multiply(np.cos(np.multiply(x, B)), integral)



x = np.linspace(-a/2, a/2, 1e4)
times = [1e-3, 10, 100]

figs, ax = plt.subplots(1,3, figsize=(8,6), sharey=False)

for idx, t in enumerate(times):
    y = get_data(x, t)
    ax[idx].plot(x, y, label=t)
    ax[idx].set_xlabel('x [cm]')
    ax[idx].set_ylabel('flux [n/s]')
    ax[idx].set_title('{0} [s]'.format(t))

plt.tight_layout(pad=0.4, h_pad=1)
plt.savefig('3_subfigs.svg', format='svg', dpi=1000)

fig = plt.figure()
# make log plot with all three
for t in times:
    y = get_data(x, t)
    plt.plot(x, y, label=t)

plt.title('1D Flux Comparison After Source Insertion [s]')
plt.xlabel('x [cm]')
plt.ylabel('flux [n/s]')
plt.yscale('log')
plt.legend()
plt.savefig('3_log.svg', format='svg', dpi=1000)

