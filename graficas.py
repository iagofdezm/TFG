import numpy as np
import matplotlib.pyplot as plt

magnetizacions={}
for i in range(5):
    magnetizacions[f't_{i}']= np.loadtxt(f"t{i}.csv", delimiter=",")

tempo=np.loadtxt('tempo.csv')

for i in range(5):
    plt.plot(tempo, magnetizacions[f't_{i}'], label=f't_{i}')
plt.xlabel('Pasos temporais')
plt.ylabel('Magnetización')
plt.legend()
plt.show()
