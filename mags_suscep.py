import os
import glob
import numpy as np
import matplotlib.pyplot as plt

def plot_magnetizacion_vs_T(ruta_carpeta):
    """Calcula la magnetización media por archivo de MEDIDA y grafica vs T.

    - Busca recursivamente archivos `*_medida.npy` (SOLO MEDIDA, no termalización).
    - Acumula temperaturas y magnetizaciones medias en arrays fuera del bucle.
    - Ordena por temperatura, guarda CSV opcionalmente y grafica.
    """
    # Buscar SOLO archivos de medida, excluir archivos de termalización
    archivos_mags = glob.glob(f"{ruta_carpeta}/**/resultados/magnetizacion_vs_temperatura.csv", recursive=True)
    archivos_suscep = glob.glob(f"{ruta_carpeta}/**/resultados/suscetibilidad_vs_temperatura.csv", recursive=True)

    if not archivos_mags:
        print("No se encontraron archivos de magnetización en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_mags)} archivos de MAGNETIZACIÓN")
    print(f"Encontrados {len(archivos_suscep)} archivos de Susceptibilidad")

    
    Ts = []
    Ms = []

    # graficar
    plt.figure(figsize=(8,6))

    for archivo in archivos_mags:
        carpeta = os.path.dirname(os.path.dirname(archivo)).split(os.sep)[-1]
        carpeta = carpeta[0] + '=' + carpeta[1]
        try:
            Ts, Ms = np.loadtxt(archivo, delimiter=',', skiprows=1, unpack=True)
            plt.plot(Ts, Ms, marker='.', ls='-', label=carpeta)
            print(f"OK: {archivo}")
        except Exception as e:
            print(f"ERROR en {archivo}: {e}")

    plt.xlabel('Temperatura')
    plt.ylabel('Magnetización media (|M|)')
    plt.title('Magnetización media vs Temperatura')
    plt.legend()
    plt.grid(True)
    salida = os.path.join(ruta_carpeta, 'magnetizacion_vs_temperatura.png')
    plt.savefig(salida, dpi=200)
    plt.close()
    print(' → Gráfica resumen guardada en:', salida)


def plot_susceptibilidad_vs_T(ruta_carpeta):
    """Calcula la susceptibilidad media por archivo de MEDIDA y grafica vs T.

    - Busca recursivamente archivos `*_medida.npy` (SOLO MEDIDA, no termalización).
    - Acumula temperaturas y magnetizaciones medias en arrays fuera del bucle.
    - Ordena por temperatura, guarda CSV opcionalmente y grafica.
    """
    # Buscar SOLO archivos de medida, excluir archivos de termalización
    archivos_suscep = glob.glob(f"{ruta_carpeta}/**/resultados/susceptibilidad_vs_temperatura.csv", recursive=True)

    if not archivos_suscep:
        print("No se encontraron archivos de susceptibilidad en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_suscep)} archivos de Susceptibilidad")

    
    Ts = []
    Suscep = []

    # graficar
    plt.figure(figsize=(8,6))

    for archivo in archivos_suscep:
        carpeta = os.path.dirname(os.path.dirname(archivo)).split(os.sep)[-1]
        carpeta = carpeta[0] + '=' + carpeta[1]
        try:
            Ts, Suscep = np.loadtxt(archivo, delimiter=',', skiprows=1, unpack=True)
            plt.plot(Ts, Suscep, marker='.', ls='-', label=carpeta)
            print(f"OK: {archivo}")
        except Exception as e:
            print(f"ERROR en {archivo}: {e}")

    plt.xlabel('Temperatura')
    plt.ylabel('Susceptibilidade media (χ)')
    plt.title('Susceptibilidade media vs Temperatura')
    plt.legend()
    plt.grid(True)
    salida = os.path.join(ruta_carpeta, 'susceptibilidad_vs_temperatura.png')
    plt.savefig(salida, dpi=200)
    plt.close()
    print(' → Gráfica resumen guardada en:', salida)

def plot_suscep_total_error(ruta_carpeta):

# Buscar SOLO archivos de medida, excluir archivos de termalización
    archivos_suscep = glob.glob(f"{ruta_carpeta}/**/resultados/susceptibilidad_vs_temperatura.csv", recursive=True)

    if not archivos_suscep:
        print("No se encontraron archivos de susceptibilidad en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_suscep)} archivos de Susceptibilidad")

    
    Ts = []
    susceps = []
    erros = []

    # graficar
    plt.figure(figsize=(8,6))

    for archivo in archivos_suscep:
        carpeta = os.path.dirname(os.path.dirname(archivo)).split(os.sep)[-1]
        carpeta = carpeta[0] + '=' + carpeta[1:]
        try:
            Ts, susceps, erros = np.loadtxt(archivo, delimiter=',', skiprows=1, unpack=True)
            plt.errorbar(Ts, susceps, yerr=erros, marker='.', markersize= 5, ls='-', linewidth=0.3, elinewidth=1, label=carpeta)
            print(f"OK: {archivo}")
        except Exception as e:
            print(f"ERROR en {archivo}: {e}")

    plt.xlabel('Temperatura')
    plt.ylabel('Susceptibilidade magnética')
    plt.title('Susceptibilidade magnética vs Temperatura')
    plt.legend()
    plt.grid(True)
    salida = os.path.join(ruta_carpeta, 'susceptibilidade_vs_temperatura_wolff.png')
    plt.savefig(salida, dpi=200)
    plt.close()
    print(' → Gráfica resumen guardada en:', salida)

def plot_helicity_total_error(ruta_carpeta):

    # Buscar SOLO archivos de medida, excluir archivos de termalización
    archivos_helicity = glob.glob(f"{ruta_carpeta}/**/resultados/helicity_vs_temperatura.csv", recursive=True)

    if not archivos_helicity:
        print("No se encontraron archivos de helicidad en", ruta_carpeta)
        return

    print(f"Encontrados {len(archivos_helicity)} archivos de Helicity")

    
    Ts = []
    HMs = []
    errors = []

    # graficar
    plt.figure(figsize=(8,6))

    for archivo in archivos_helicity:
        carpeta = os.path.dirname(os.path.dirname(archivo)).split(os.sep)[-1]
        carpeta = carpeta[0] + '=' + carpeta[1:]
        try:
            Ts, HMs, errors = np.loadtxt(archivo, delimiter=',', skiprows=1, unpack=True)
            plt.errorbar(Ts, HMs, yerr=errors, marker='.', markersize= 5, ls='-', linewidth=0.3, elinewidth=1, label=carpeta)
            print(f"OK: {archivo}")
        except Exception as e:
            print(f"ERROR en {archivo}: {e}")
    plt.plot(Ts, (2 / np.pi)*Ts, 'k--', label='y = (2/π)T')
    plt.xlabel('Temperatura')
    plt.ylabel('Helicity Modulus')
    plt.title('Helicity modulus vs Temperatura')
    plt.legend()
    plt.grid(True)
    salida = os.path.join(ruta_carpeta, 'helicity_vs_temperatura_wolff.png')
    plt.savefig(salida, dpi=200)
    plt.close()
    print(' → Gráfica resumen guardada en:', salida)


if __name__ == "__main__":
    ruta_carpeta = "resultados_wolff"
    plot_suscep_total_error(ruta_carpeta)
    #plot_helicity_total_error(ruta_carpeta)

