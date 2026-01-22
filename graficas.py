import numpy as np
import matplotlib.pyplot as plt

magnetizacions={}
for i in range(1):
    #magnetizacions[f't_{i}']= np.loadtxt(f"t{i}.csv", delimiter=",")
    magnetizacions['t-1']= np.loadtxt("t-1.csv", delimiter=",")

tempo=np.loadtxt('tempo.csv')

for i in range(1):
    #plt.plot(tempo, magnetizacions[f't_{i}'], label=f't_{i}')
    plt.plot(tempo, magnetizacions['t-1'], label='t-1')
plt.xlabel('Pasos temporais')
plt.ylabel('Enerxía')
plt.legend()
plt.show()
