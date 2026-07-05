import os
import numpy as np
import glob
import matplotlib.pyplot as plt
import re
from observables import enerxia_por_spin, magnetizacion_por_spin, susceptibilidad_magnetica, helicity_modulus
from rede import Rede

# Analiza todos los archivos .npy dentro de una carpeta y sus subcarpetas.

def plot_helicity_vs_T(ruta_carpeta, L, q, J, guardar_csv=True):
    """Calcula la magnetización media por archivo de MEDIDA y grafica vs T.

    - Busca recursivamente archivos `*_medida.npy` (SOLO MEDIDA, no termalización).
    - Acumula temperaturas y magnetizaciones medias en arrays fuera del bucle.
    - Ordena por temperatura, guarda CSV opcionalmente y grafica.
    """
    # Buscar SOLO archivos de medida, excluir archivos de termalización
    archivos_medida = glob.glob(f"{ruta_carpeta}/**/*_medida.npy", recursive=True)
    if not archivos_medida:
        print("No se encontraron archivos de medida (_medida.npy) en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_medida)} archivos de MEDIDA")
    
    rede = Rede(L, q, J)
    Ts = []
    HMs = []
    errors = []
    
    for archivo in archivos_medida:
        # intentar extraer temperatura desde la carpeta padre o desde el nombre
        carpeta = os.path.basename(os.path.dirname(archivo))
        try:
            T = float(carpeta)
        except Exception:
            print(f"  No se pudo extraer temperatura de la carpeta '{carpeta}', intentando desde el nombre del archivo...")

        try:
            np.load(archivo, allow_pickle=True)
            print(f"OK: {archivo}")
        except Exception as e:
            print(f"ERROR en {archivo}: {e}")

        configs = np.load(archivo, allow_pickle=True)
        hms = []
        for spins in configs:
            rede.spins = spins
            H = helicity_modulus(rede, T)
            hms.append(H)
        hms = np.array(hms)
        hms = np.array_split(hms, 5)  # dividir en 5 bloques para estimar error
        mean_hm = float(np.mean(np.abs(hms)))
        std_hm = float(np.std(np.abs(hms)))

        errors.append(std_hm)

        Ts.append(T)
        HMs.append(mean_hm)

    # convertir a arrays y ordenar por temperatura
    Ts = np.array(Ts)
    HMs = np.array(HMs)
    errors = np.array(errors)
    order = np.argsort(Ts)
    Ts = Ts[order]
    HMs = HMs[order]
    errors = errors[order]

    # guardar CSV con los datos
    if guardar_csv:
        csv_path = os.path.join(ruta_carpeta, 'helicity_vs_temperatura.csv')
        np.savetxt(csv_path, np.column_stack((Ts, HMs, errors)), delimiter=',', header='T,mean_abs_HM,std_HM', comments='')
        print(' → Datos guardados en:', csv_path)
    '''
    csv_path = os.path.join(ruta_carpeta, 'helicity_vs_temperatura.csv')
    Ts, HMs = np.loadtxt(csv_path, delimiter=',',skiprows=1, unpack=True)
    '''
    temp = Ts[: round(len(Ts)/2)]
    y = (2 / np.pi)*temp
    # graficar
    plt.figure(figsize=(8,6))
    plt.errorbar(Ts, HMs, yerr=errors, marker='.', ls='', markersize = 12)
    plt.plot(temp, y)
    plt.xlabel('Temperatura')
    plt.ylabel('Helicity Modulus')
    plt.title('Helicity modulus vs Temperatura')
    plt.grid(True)
    salida = os.path.join(ruta_carpeta, 'helicity_vs_temperatura.png')
    plt.savefig(salida, dpi=200)
    plt.close()
    print(' → Gráfica resumen guardada en:', salida)

def plot_magnetizacion_vs_T(ruta_carpeta, L, q, J, guardar_csv=True):
    """Calcula la magnetización media por archivo de MEDIDA y grafica vs T.

    - Busca recursivamente archivos `*_medida.npy` (SOLO MEDIDA, no termalización).
    - Acumula temperaturas y magnetizaciones medias en arrays fuera del bucle.
    - Ordena por temperatura, guarda CSV opcionalmente y grafica.
    """
    # Buscar SOLO archivos de medida, excluir archivos de termalización
    archivos_medida = glob.glob(f"{ruta_carpeta}/**/*_medida.npy", recursive=True)
    if not archivos_medida:
        print("No se encontraron archivos de medida (_medida.npy) en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_medida)} archivos de MEDIDA")
    
    rede = Rede(L, q, J)
    Ts = []
    Ms = []
    mags_errors = []
    for archivo in archivos_medida:
        try:
            np.load(archivo, allow_pickle=True)
            print(f"OK: {archivo}")
        except Exception as e:
            print(f"ERROR en {archivo}: {e}")

        configs = np.load(archivo, allow_pickle=True)
        mags = []
        for spins in configs:
            rede.spins = spins
            M = magnetizacion_por_spin(rede)
            mags.append(M)

        mean_mag = float(np.mean(np.abs(mags)))

        # intentar extraer temperatura desde la carpeta padre o desde el nombre
        carpeta = os.path.basename(os.path.dirname(archivo))
        try:
            T = float(carpeta)
        except Exception:
            print(f"  No se pudo extraer temperatura de la carpeta '{carpeta}', intentando desde el nombre del archivo...")

        Ts.append(T)
        Ms.append(mean_mag)

    # convertir a arrays y ordenar por temperatura
    Ts = np.array(Ts)
    Ms = np.array(Ms)
    order = np.argsort(Ts)
    Ts = Ts[order]
    Ms = Ms[order]

    # guardar CSV con los datos
    if guardar_csv:
        csv_path = os.path.join(ruta_carpeta, 'magnetizacion_vs_temperatura.csv')
        np.savetxt(csv_path, np.column_stack((Ts, Ms)), delimiter=',', header='T,mean_abs_M', comments='')
        print(' → Datos guardados en:', csv_path)

    # graficar
    plt.figure(figsize=(8,6))
    plt.plot(Ts, Ms, marker='.', ls='', markersize = 12)
    plt.xlabel('Temperatura')
    plt.ylabel('Magnetización media (|M|)')
    plt.title('Magnetización media vs Temperatura')
    plt.grid(True)
    salida = os.path.join(ruta_carpeta, 'magnetizacion_vs_temperatura.png')
    plt.savefig(salida, dpi=200)
    plt.close()
    print(' → Gráfica resumen guardada en:', salida)


def plot_susceptibilidad_vs_T(ruta_carpeta, L, q, J, guardar_csv=True):
    """Calcula la susceptibilidad magnética por temperatura y la grafica."""
    archivos_medida = glob.glob(f"{ruta_carpeta}/**/*_medida.npy", recursive=True)
    if not archivos_medida:
        print("No se encontraron archivos de medida (_medida.npy) en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_medida)} archivos de MEDIDA")

    rede = Rede(L, q, J)
    Ts = []
    chis = []
    chiserrores = []

    for archivo in archivos_medida:
        configs = np.load(archivo, allow_pickle=True)
        mags = []
        for spins in configs:
            rede.spins = spins
            M = magnetizacion_por_spin(rede)
            mags.append(M)
        mags = np.array(mags)
        mags = np.array_split(mags, 5)  # dividir en 5 bloques para estimar error
        # intentar extraer temperatura desde la carpeta padre o desde el nombre
        carpeta = os.path.basename(os.path.dirname(archivo))
        try:
            T = float(carpeta)
        except Exception:
            print(f"  No se pudo extraer temperatura de la carpeta '{carpeta}', intentando desde el nombre del archivo...")
            match = re.search(r'T(\d+\.\d+)', archivo)
            if match:
                T = float(match.group(1))
            else:
                raise ValueError(f"No se pudo extraer la temperatura de {archivo}")
        
        chimedia = 0
        chierror = 0
        for bloque in mags:
            chi = susceptibilidad_magnetica(bloque, T, rede.N)
            chimedia += chi
            chierror += chi**2 #suma dos cadrados das chi, despois engádense os demais termos
        chimedia /= len(mags)
        chierror = np.sqrt(chierror / len(mags) - chimedia**2)

        Ts.append(T)
        chis.append(chimedia)
        chiserrores.append(chierror)
    Ts = np.array(Ts)
    chis = np.array(chis)
    chiserrores = np.array(chiserrores)
    order = np.argsort(Ts)
    Ts = Ts[order]
    chis = chis[order]
    chiserrores = chiserrores[order]

    if guardar_csv:
        csv_path = os.path.join(ruta_carpeta, 'susceptibilidad_vs_temperatura.csv')
        np.savetxt(csv_path, np.column_stack((Ts, chis, chiserrores)), delimiter=',', header='T,chi,chi_error', comments='')
        print(' → Datos guardados en:', csv_path)

    plt.figure(figsize=(8,6))
    plt.errorbar(Ts, chis, yerr=chiserrores, marker='.', ls='-', capsize=5)
    plt.xlabel('Temperatura')
    plt.ylabel('Susceptibilidad magnética')
    plt.title('Susceptibilidad magnética vs Temperatura')
    plt.grid(True)
    salida = os.path.join(ruta_carpeta, 'susceptibilidad_vs_temperatura.png')
    plt.savefig(salida, dpi=200)
    plt.close()
    print(' → Gráfica de susceptibilidad guardada en:', salida)


if __name__ == "__main__":
    # Parámetros (deben coincidir con los usados en la simulación)
    L = 50
    q = 12
    J = 1.0

    
    ruta_carpeta = "resultados_wolff/q12/resultados"
    #print(f"\nAnalizando magnetización vs temperatura...")
    #plot_magnetizacion_vs_T(ruta_carpeta, L, q, J)
    #print(f"\nAnalizando susceptibilidad magnética vs temperatura...")
    plot_susceptibilidad_vs_T(ruta_carpeta, L, q, J)
    print(f"\nAnalizando helicidad vs temperatura...")
    #plot_helicity_vs_T(ruta_carpeta, L, q, J)