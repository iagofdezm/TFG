import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

plt.close('all')

ruta = os.path.join('datos', 'q2')

temperaturas = np.loadtxt(f'{ruta}\\temperaturas.npy')
vm = np.loadtxt(f'{ruta}\\vm.csv')
vm2 = np.loadtxt(f'{ruta}\\vm2.csv')
ve = np.loadtxt(f'{ruta}\\ve.csv')
ve2 = np.loadtxt(f'{ruta}\\ve2.csv')

plt.plot(temperaturas, vm, '.')
plt.xlabel('Temperatura')
plt.ylabel('Magnetización')
plt.title('Magnetización promedio fronte á temperatura')
plt.legend()
plt.show()

