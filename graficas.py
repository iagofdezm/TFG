import numpy as np
import matplotlib.pyplot as plt

magnetizacions={}
for i in range(3):
    magnetizacions[f't_{i+1}']= np.loadtxt(f"t{i+1}.csv", delimiter=",")

tempo=np.loadtxt('tempo.csv')

for i in range(3):
    plt.plot(tempo, magnetizacions[f't_{i+1}'], label=f't_{i+1}')
plt.xlabel('Pasos temporais')
plt.ylabel('Enerxía/Enerxía máxima')
plt.legend()
plt.show()
