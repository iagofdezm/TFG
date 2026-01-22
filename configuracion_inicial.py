import numpy as np
from lectura_datos import gardar_rede

#Número de spins: N2
N=50
#Posibles estados de spin
k=[-1, 1]
#Temperatura
T=0.5
#Factor de interacción
J=1

#Definición do vector 1D cos spins
spins=np.random.choice(k, N*N)


def adyacencia(N):
    #Consideramos interaccións a primeiros veciños
    v=[[] for _ in range(N*N)]
    for i in range(N):
        for j in range(N):
            #k: índice no vector 1D
            k=i*N+j
            #Veciño arriba
            if i>0:
                v[k].append((i-1)*N+j)
            #Veciño abaixo
            if i<N-1:
                v[k].append((i+1)*N+j)
            #Veciño esquerda
            if j>0:
                v[k].append(i*N+(j-1))
            #Veciño dereita
            if j<N-1:
                v[k].append(i*N+(j+1))
    return v

#Vector de adyacencia
ady = adyacencia(N)

gardar_rede(spins, ady, 'configuracion_inicial')

