import numpy as np
from lectura_datos import ler_adx, ler_spins
from enerxias import magnetizacion, enerxia_total
import matplotlib.pyplot as plt


adx = ler_adx('adx.npz')

temperaturas=np.linspace(0.00001, 3, 20)

ms = {}

for T in temperaturas:
    #Vector con todos os microestados gardados para unha T dada
    spins = ler_spins(f'spins_{T:.1f}.npz')
    tempo = np.loadtxt(f"tempo_{T:.1f}.npz")
    m = np.zeros(len(spins))

    for i in range(len(spins)):
        vm = magnetizacion(spins[i], adx, J=1)
        m[i] = vm[2]
    
    ms[f'temp_{T:.1f}'] = m
i=0
for nombre, valores in ms.items():
    i=i+1
    if i%4==0:
        plt.plot(valores, label=nombre)
plt.xlabel('Tempo')
plt.ylabel('Magnetización')
plt.legend()
plt.show()    

