import numpy as np
from lectura_datos import gardar_spins, gardar_adx

#Número de spins: N2
N=50
#Posibles estados de spin
k=[]
q=2
for i in range(q):
    k.append(2*np.pi*i/q)


#Factor de interacción
J=1

#Definición do vector 1D cos spins
spins=np.random.choice(k, N*N)


def crea_adx(N):
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
adx = crea_adx(N)

gardar_adx(adx, 'adx')
gardar_spins(spins, 'configuracion_actual')
'''

