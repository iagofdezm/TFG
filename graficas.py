import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

plt.close('all')

temperaturas=np.linspace(0.001, 3, 5)
q='datos\\q2'


for T in temperaturas:
    #archivom = f"magnetizacion_{T:.1f}.npz"
    #rutam = os.path.join(q, archivom)


    
    archivoe = f"enerxia_{T:.1f}.npz"
    rutae = os.path.join(q, archivoe)
    
    archivot = f"tempo_{T:.1f}.npz"
    rutat = os.path.join(q, archivot)
    
    #m = np.loadtxt(rutam, delimiter=",")
    e = np.loadtxt(rutae, delimiter=",")



    #np.loadtxt(rutae, delimiter=",")
    t = np.loadtxt(rutat, delimiter=",")

    plt.plot(t, e, label=round(T, 1))


plt.xlabel('Tempo')
plt.ylabel('Enerxía')
plt.title('Evolución da enerxía na equilibración')
plt.legend()
plt.show()

