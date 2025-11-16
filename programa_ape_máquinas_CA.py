## APE - Princípios da Máquina CA ## 

## Aluno: Vitor Augusto Tibério - 14658834 ## 

## Prof. Elmer Pablo Tito Cari ## 

## ----------------------------------------------------------- ## 

## Importando as Bibliotecas: ## 

import numpy as np

# Define-se o produto N*Im como 1.0 para normalizar. 
# O resultado da magnitude será um múltiplo de (NI_m).
NI_m = 1.0

# Eixos das bobinas em graus (conforme Fig. 1: a=0, c=120, b=240): 
eixo_a_deg = 0.0
eixo_b_deg = 240.0
eixo_c_deg = 120.0

# Convertendo eixos para radianos: 
eixo_a_rad = np.deg2rad(eixo_a_deg)
eixo_b_rad = np.deg2rad(eixo_b_deg)
eixo_c_rad = np.deg2rad(eixo_c_deg)

# Criando os vetores de direção (fasores) para cada eixo
# vec = cos(theta) + j*sin(theta)
vec_eixo_a = np.exp(1j * eixo_a_rad)
vec_eixo_b = np.exp(1j * eixo_b_rad)
vec_eixo_c = np.exp(1j * eixo_c_rad)

# Instantes de tempo (ωt) em graus
instantes_deg = [0, 60, 120, 180, 240, 300] #lista com os valores que devem ser calculados

print("\n")
print("--- Calculando a Fmm Resultante ---")

for wt_deg in instantes_deg:
    # Converter instante ωt para radianos
    wt_rad = np.deg2rad(wt_deg)

   # Calculando a Magnetude das Fases ## 
    mag_fmm_a = NI_m * np.cos(wt_rad)
    mag_fmm_b = NI_m * np.cos(wt_rad - np.deg2rad(120))
    mag_fmm_c = NI_m * np.cos(wt_rad - np.deg2rad(240))

    # Calculando a FMM de cada Bobina 
    fmm_a = mag_fmm_a * vec_eixo_a
    fmm_b = mag_fmm_b * vec_eixo_b
    fmm_c = mag_fmm_c * vec_eixo_c

    # Calculando a FMM resultante 
    fmm_resultante = fmm_a + fmm_b + fmm_c
    magnitude = np.abs(fmm_resultante)
    angulo_deg = np.rad2deg(np.angle(fmm_resultante))

    # Resultados 
    print(f"\nPara ωt = {wt_deg}°:")
    print(f"  Magnitude: {magnitude:.2f} * (NI_m)")
    print(f"  Direção:   {np.round(angulo_deg, 1)}°")

print("\n--- Fim do Cálculo ---")