import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

plt.close('all')

ruta = os.path.join('datos', 'q2')

temperaturas = np.loadtxt(f'{ruta}\\temperaturas.npy')

#Gráficas de magnitudes a diferentes temperaturas

vm = np.loadtxt(f'{ruta}\\vm.csv')
vm2 = np.loadtxt(f'{ruta}\\vm2.csv')
ve = np.loadtxt(f'{ruta}\\ve.csv')
ve2 = np.loadtxt(f'{ruta}\\ve2.csv')
#susceptibilidade = np.loadtxt(f'{ruta}\\susceptibilidade.csv')
N=50
susceptibilidade = N*(vm2-vm*vm)/temperaturas


plt.plot(temperaturas, vm, '.')
plt.xlabel('Temperatura')
plt.ylabel('Magnetización')
plt.title('Magnetización promedio por spin fronte á temperatura')
plt.legend()
plt.show()


#Gráficas da evolución de magnitudes na equilibración
'''
for T in temperaturas:
    plt.close('all')
    enerxia = np.load(f'{ruta}\\T={T}\\enerxia_equilibracion_{T}.npy')
    magnetizacion = np.load(f'{ruta}\\T={T}\\magnetizacion_equilibracion_{T}.npy')
    tempo = np.linspace(0, 1, len(enerxia))
    plt.plot(tempo, magnetizacion)
    plt.xlabel('Tempo')
    plt.ylabel('Magnetización')
    plt.ylim(0, 1.1) #Fixación do eixo para a magnetización
    plt.title('Evolución da magnetización na equilibración')
    plt.legend()
    plt.savefig(f'{ruta}\\T={T}\\evolucion_magnetización_equilibracion.png')
'''


