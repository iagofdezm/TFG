import numpy as np
from lectura_datos import gardar_spins, gardar_ady

#Número de spins: N2
N=50
#Posibles estados de spin
k=[0, np.pi]

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
            v[k].append(((i-1)%N)*N+j)
            #Veciño abaixo
            v[k].append(((i+1)%N)*N+j)
            #Veciño esquerda
            v[k].append(i*N+(j-1)%N)
            #Veciño dereita
            v[k].append(i*N+(j+1)%N)
    return v

#Vector de adyacencia
'''
ady = adyacencia(N)

gardar_ady(ady, 'adyacencia')
gardar_spins(spins, 'configuracion_actual')
'''

