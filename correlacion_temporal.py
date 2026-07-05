import numpy as np
import matplotlib.pyplot as plt
from rede import Rede
from observables import magnetizacion_por_spin
import glob
import os

def correlacion_temporal_magnetizacion(ruta_carpeta, L, q, J, guardar_csv=True):
    # Buscar SOLO archivos de medida, excluir archivos de termalización
    archivos_medida = glob.glob(f"{ruta_carpeta}/**/*_medida.npy", recursive=True)
    #archivos_medida = os.path.join(ruta_carpeta, '**', '*_medida.npy')
    if not archivos_medida:
        print("No se encontraron archivos de medida (_medida.npy) en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_medida)} archivos de MEDIDA")
    
    rede = Rede(L, q, J)

    for archivo in archivos_medida:
        try:
            np.load(archivo, allow_pickle=True)
            print(f"OK: {archivo}")
        except Exception as e:
            print(f"ERROR en {archivo}: {e}")

        configs = np.load(archivo, allow_pickle=True)

        #Serie temporal de magnetización por spin
        mags = []
        for spins in configs:
            rede.spins = spins
            M = magnetizacion_por_spin(rede)
            mags.append(M)
        mags = np.array(mags)
        tempo = len(mags)
        # media de la magnetización de la serie temporal
        mean_mag = float(np.mean(np.abs(mags)))

        # Correlación no normalizada
        C = np.zeros(50, dtype=float)
        for tau in range(50):
            if tempo - tau > 0:
                C[tau] = np.mean((mags[:tempo-tau] - mean_mag) * (mags[tau:] - mean_mag))
        # Normalizar por C(0)
        C /= C[0]


        # intentar extraer temperatura desde la carpeta padre o desde el nombre
        carpeta = os.path.basename(os.path.dirname(archivo))
        try:
            T = float(carpeta)
        except Exception:
            print(f"  No se pudo extraer temperatura de la carpeta '{carpeta}', intentando desde el nombre del archivo...")

        # guardar CSV con los datos
        if guardar_csv:
            csv_path = os.path.join(ruta_carpeta, carpeta, 'corr_temp_mag.csv')
            np.savetxt(csv_path, C, delimiter=',', header='Correlación temporal da magnetización', comments='')
            print(' → Datos guardados en:', csv_path)

        # graficar
        plt.figure(figsize=(8,6))
        plt.plot(range(len(C)), C, marker='.', ls='-')
        plt.xlabel('Tempo')
        plt.ylabel('Correlación temporal da magnetización')
        plt.title('Correlación temporal da magnetización a T={:.2f}'.format(T))
        plt.grid(True)
        salida = os.path.join(ruta_carpeta, carpeta, 'corr_temp_mag.png')
        plt.savefig(salida, dpi=200)
        plt.close()
        print(' → Gráfica resumen guardada en:', salida)

def grafica_correlacions_xuntas(ruta_carpeta):

    # Buscar SOLO archivos de medida, excluir archivos de termalización
    archivos_medida = glob.glob(f"{ruta_carpeta}/**/*corr_temp_mag.csv", recursive=True)
    if not archivos_medida:
        print("No se encontraron archivos de medida (_medida.npy) en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_medida)} archivos de MEDIDA")
    
    plt.figure(figsize=(10,6))

    for archivo in archivos_medida:
        # intentar extraer temperatura desde la carpeta padre o desde el nombre
        carpeta = os.path.basename(os.path.dirname(archivo))
        try:
            temp = float(carpeta)
        except Exception:
            print(f"  No se pudo extraer temperatura de la carpeta '{carpeta}', intentando desde el nombre del archivo...")

        try:
            corr = np.loadtxt(archivo, delimiter=',', skiprows=1)
            plt.plot(range(len(corr)), corr, marker='.', ls='-', label=f'T = {temp}')
            print(f"OK: {archivo}")
            print(f"OK: {archivo}")
        except Exception as e:
            print(f"ERROR en {archivo}: {e}")


        
    print(f"Encontrados {len(archivos_medida)} archivos de correlación temporal")


    plt.xlabel('Tempo')
    plt.ylabel('Correlación temporal da magnetización')
    plt.title('Correlación temporal da magnetización no Modelo de Ising')
    plt.legend()
    plt.grid(True)
    salida = os.path.join(ruta_carpeta, 'corr_temp_mag_comparativa.png')
    plt.savefig(salida, dpi=200)
    plt.close()
    print(' → Gráfica comparativa guardada en:', salida)

if __name__ == "__main__":
    # Parámetros (deben coincidir con los usados en la simulación)
    L = 50
    q = 2
    J = 1.0


    
    ruta_carpeta = "correlacion/resultados"

    print(f"\nAnalizando correlación temporal...")
    #correlacion_temporal_magnetizacion(ruta_carpeta, L, q, J)
    grafica_correlacions_xuntas(ruta_carpeta)