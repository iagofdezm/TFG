import numpy as np

class algoritmo_wolff_prueba:

    def __init__(self, rede, T):
        self.rede = rede
        self.T = T
        self.beta = 1.0 / T
        self.J = rede.J
        self.q = rede.q

    def angle(self, s):
        return 2 * np.pi * s / self.q

    def state_from_angle(self, theta):
        """
        Proyecta un ángulo theta (con pequeño error numérico) al estado discreto k ∈ {0,…,q−1}
        más cercano, de forma que ángulos como 0−, 0 y 0+ se asignen al mismo estado.

        Estrategia:
        1. Normalizar theta a [0, 2π).
        2. Desplazar el ángulo medio sector (π/q) para que cada estado quede en el centro
        de su intervalo de asignación.
        3. Volver a tomar módulo 2π tras el desplazamiento.
        4. Convertir a fracción de vuelta y usar floor() para obtener el índice de sector.
        """
        theta_norm = theta % (2*np.pi)
        # Desplazamos medio sector para que el redondeo sea "al más cercano"
        theta_shifted = (theta_norm + np.pi / self.q) % (2*np.pi)
        frac = theta_shifted / (2*np.pi)
        return int(np.floor(frac * self.q)) % self.q

    
    def reflexo(self, theta, phi, i):
        '''
        phi: ángulo do plano respecto do OX positivo
        alfa: distancia angular entre o spin e o plano de reflexión
        i: índice do nodo
        theta: ángulo do spin do nodo a reflexar
        '''
        alfa = phi - theta
        theta_n = (theta + 2*alfa) % (2*np.pi)
        spins = self.rede.spins
        spins[i] = self.state_from_angle(theta_n)
        return theta_n

    def paso(self):
        N = self.rede.N
        spins = self.rede.spins
        q = self.q

        
        # Primeiro nodo no stack
        seed = np.random.randint(0, N)

        in_cluster = np.zeros(N, dtype=bool)
        in_cluster[seed] = True
        stack = [seed]
        cluster = [seed]

        #Definición dun plano de reflexión. 
        m = np.random.randint(0, q)

        phi = np.pi * m / q

        r = np.pi * m / q + np.pi / 2
        

        # 5. Crecimiento del clúster (embedding Wolff)
        while stack:
            i = stack.pop()
            # Ángulo do nodo do stack
            si = spins[i]
            thetai = self.angle(si)
            thetai = self.reflexo(thetai, phi, i)

            # Diferencia angular entre o spin do stack e o eixo r (normal ao plano de reflexión)
            Delta_ir = thetai - r

            proj_ir = np.cos(Delta_ir)

            for j in self.rede.veciños[i]:
                if in_cluster[j]:
                    continue
                # Ángulo do spin do veciño candidato a formar parte do cluster
                sj = spins[j]
                thetaj = self.angle(sj)

                # Diferencia angular co eixo r (normal ao plano de reflexión)
                Delta_jr = thetaj - r

                proj_jr = np.cos(Delta_jr)
                factor = min(0, 2*self.beta * self.J * proj_ir * proj_jr)
                p_add = 1 - np.exp(factor)

                if np.random.rand() < p_add:
                    in_cluster[j] = True
                    stack.append(j)
                    cluster.append(j)
                    #self.reflexo(thetaj, phi, j)

        return len(cluster)

    def barrido(self, n=1):
        for _ in range(n):
            self.paso()
