import os
import numpy as np
import yaml
from rede import Rede
from alg_wolff import algoritmo_wolff_prueba
from multiprocessing import Pool, cpu_count

def simulacion(cfg):
    L = cfg["L"]
    q = cfg["q"]
    J = cfg["J"]
    T = cfg["T"]
    pasos_equilibracion = cfg["pasos_equilibracion"]
    pasos_medida = cfg["pasos_medida"]
    frecuencia_medida = cfg["frecuencia_medida"]
    seed = cfg["seed"]

    rede = Rede(L, q, J, seed)
    mc = algoritmo_wolff_prueba(rede, T)

    # Enfriamiento gradual sólo si la temperatura objetivo es menor que la temperatura inicial
    pasos_enfriamiento = cfg.get("pasos_enfriamiento", 0)
    if pasos_enfriamiento > 0:
        T_inicio_enfriamiento = cfg.get("T_inicio_enfriamiento", max(5.0 * T, 2.0 * T))
        if T_inicio_enfriamiento > T:
            n_temperaturas_enfriamiento = cfg.get("n_temperaturas_enfriamiento", 10)
            temperaturas_enfriamiento = np.linspace(T_inicio_enfriamiento, T, n_temperaturas_enfriamiento)
            pasos_por_temperatura = max(1, pasos_enfriamiento // len(temperaturas_enfriamiento))

            print(
                f"Enfriando desde T={T_inicio_enfriamiento:.2f} hasta T={T:.2f} "
                f"en {n_temperaturas_enfriamiento} niveles de temperatura y {pasos_enfriamiento} barridos..."
            )
            for T_actual in temperaturas_enfriamiento:
                mc.T = T_actual
                mc.beta = 1.0 / T_actual
                for _ in range(pasos_por_temperatura):
                    mc.barrido()

            # Restaurar temperatura objetivo antes de la termalización
            mc.T = T
            mc.beta = 1.0 / T
        else:
            print(
                f"No se realiza enfriamiento porque T_inicio_enfriamiento={T_inicio_enfriamiento:.2f} "
                f"no es mayor que T={T:.2f}."
            )

    # Guardar configuraciones
    rexistro_spins_termalizacion = []

    # Termalización
    print(f"Termalizando para T={T:.2f}...")
    for paso in range(pasos_equilibracion):
        mc.barrido()
        if paso % frecuencia_medida == 0:
            rexistro_spins_termalizacion.append(rede.spins.copy())


    # Guardar configuraciones
    rexistro_spins = []
    print(f"Medición para T={T:.2f}...")
    for paso in range(pasos_medida):
        mc.barrido()
        if paso % frecuencia_medida == 0:
            rexistro_spins.append(rede.spins.copy())

    carpeta_resultados = os.path.join("resultados", f"{T:.2f}")
    os.makedirs(carpeta_resultados, exist_ok=True)

    np.save(os.path.join(carpeta_resultados, "configs_T{:.2f}_termalizacion.npy".format(T)), rexistro_spins_termalizacion)
    np.save(os.path.join(carpeta_resultados, "configs_T{:.2f}_medida.npy".format(T)), rexistro_spins)

    return np.array(rexistro_spins)



def run_T(cfg):
    T = cfg["T"]
    print(f"Ejecutando simulación para T={T:.2f}")
    simulacion(cfg)

def main():
    with open("config.yaml", "r", encoding="utf-8") as f:
        cfg_file = yaml.safe_load(f)

    base_cfg = {
        **cfg_file["rede"],
        **cfg_file["simulacion"],
        "J": cfg_file["parametros"]["J"],
        "seed": cfg_file["random"]["seed"],
    }

    # Crear una lista de configuraciones, una por temperatura
    cfgs = []
    for T in cfg_file["parametros"]["temperaturas"]:
        cfg = {**base_cfg, "T": T}
        cfgs.append(cfg)

    # Número de procesos = número de cores disponibles
    nproc = cpu_count()

    print(f"Ejecutando en paralelo con {nproc} procesos")

    with Pool(processes=nproc) as pool:
        pool.map(run_T, cfgs)

if __name__ == "__main__":
    main()


